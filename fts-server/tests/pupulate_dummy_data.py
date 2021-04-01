from tests.words import make_sentence, SKILLS
from app.database.MongoDB import MongoDb
from app.database.mongo import MongoDatabase
from app.model.Skill import Skill
from app.model.TrainingEvent import TrainingEvent
from app.repository.AuthenticatedUserRepository import AuthenticatedUserRepository
from app.repository.BookingRepository import BookingRepository
from app.repository.SkillRepository import SkillRepository
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.repository.UserRepository import UserRepository
from app.service.AuthService import AuthService
from app.service.SkillService import SkillService
from app.service.TrainingEventService import TrainingEventService
from datetime import datetime
import time
import random

db: MongoDatabase
users: UserRepository
auth_repo: AuthenticatedUserRepository
auth_users: AuthService
event_service: TrainingEventService
event_repo: TrainingEventRepository
skills: SkillService
bookings: BookingRepository


def init():
    global db, users, auth_users, auth_repo, event_repo, event_service, skills, bookings
    db = MongoDatabase()
    users = UserRepository(db)
    auth_repo = AuthenticatedUserRepository(db)
    auth_users = AuthService(auth_repo)
    skills = SkillService(SkillRepository(db))
    bookings = BookingRepository(db)
    event_repo = TrainingEventRepository(db)
    event_service = TrainingEventService(event_repo, AuthService(auth_repo), users)


def clear_all():
    for col in MongoDb.collection_names():
        MongoDb.drop(col)


def populate_users():
    auth_users.register("test@test.test", "test", login=False)
    user = users.find_user_by_email("test@test.test")
    user.name = "Baz"
    user.competencies = ["javascript", "python"]
    user.interests = ["c++"]
    users.update(user)

    auth_users.register("user@test.test", "test", login=False)
    user = users.find_user_by_email("user@test.test")
    user.name = "Bill Paxton"
    user.competencies = ["wrestling", "python"]
    user.interests = ["photography"]
    users.update(user)

    manager_id = auth_users.register("manager@test.test", "test", login=False)["id"]
    user = users.find_user_by_email("manager@test.test")
    user.name = "Chris Basildon"
    user.competencies = ["chess", "ukulele"]
    user.interests = ["cheese_rolling"]
    users.update(user)
    return manager_id


def populate_skills():
    skills.add_skill("C++", ["cpp", "c++"])
    skills.add_skill("JavaScript", ["js", "javascript"])
    skills.add_skill("Python", ["python"])
    skills.add_skill("Cheese Rolling")
    skills.add_skill("wrestling")
    skills.add_skill("photography")
    skills.add_skill("ukulele")
    skills.add_skill("chess")


def generate_random_courses(manager_id):
    now = int(round(time.time() * 1000))
    ONE_DAY = 86400000

    for i in range(100):
        event = TrainingEvent(title=make_sentence(5))
        event.synopsis = make_sentence(30)
        event.start_time = now + ONE_DAY * random.randint(-7, 50)
        for i in range(random.randint(0, 3)):
            event.outcomes.append(random.choice(SKILLS))
        for i in range(random.randint(0, 3)):
            event.prerequisites.append(random.choice(SKILLS))

        event.outcomes = list(set(event.outcomes))
        event.prerequisites = list(set(event.prerequisites))
        event.training_manager_id = manager_id
        event_repo.insert(event)


def populate_events(manager_id: str):
    ONE_DAY = 86400000
    ONE_HALF_DAY = ONE_DAY / 2
    ONE_WEEK = ONE_DAY * 7
    now = int(round(time.time() * 1000))

    in2Days = TrainingEvent(title="Starts in 2 days")
    in2Days.synopsis = "This event is happening in 2 days time. You will have no trouble booking it."
    in2Days.start_time = now + ONE_DAY * 2
    in2Days.outcomes = ["python", "c++"]
    in2Days.prerequisites = ["ukulele"]
    in2Days.training_manager_id = manager_id

    lt24Hours = TrainingEvent(title="Less Than 24 hours")
    lt24Hours.synopsis = "This is happening too soon to book. Less than 24 hours to go. Soz!"
    lt24Hours.start_time = now + ONE_HALF_DAY
    lt24Hours.outcomes = ["photography", "cheese_rolling"]
    lt24Hours.prerequisites = ["c++"]
    lt24Hours.training_manager_id = manager_id

    yesterday = TrainingEvent(title="Event Was Yesterday")
    yesterday.synopsis = "This event happened yesterday. You can still view it but you are unable to make a booking"
    yesterday.start_time = now - ONE_DAY
    yesterday.outcomes = ["wrestling", "chess"]
    yesterday.prerequisites = ["javascript"]
    yesterday.training_manager_id = manager_id

    over_a_week_ago = TrainingEvent(title="Over a week ago")
    over_a_week_ago.synopsis = "This event is old. You shouldn't even see it"
    over_a_week_ago.start_time = now - ONE_WEEK
    over_a_week_ago.outcomes = []
    over_a_week_ago.prerequisites = ["wrestling", "chess"]
    over_a_week_ago.training_manager_id = manager_id

    event_repo.insert(in2Days)
    event_repo.insert(lt24Hours)
    event_repo.insert(yesterday)
    event_repo.insert(over_a_week_ago)


def start(credentials, port):
    MongoDb.set_credentials(credentials, port)
    clear_all()
    init()
    populate_skills()
    manager_id = populate_users()
    populate_events(manager_id)
    generate_random_courses(manager_id)


if __name__ == "__main__":
    start("root:password@localhost", 27018)
