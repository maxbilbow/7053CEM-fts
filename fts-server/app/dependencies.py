from injector import singleton

# Import rest endpoints
import app.rest.TrainingEventResource
import app.rest.IndexController
import app.rest.AuthController
import app.rest.SkillResource
import app.rest.UserResourse
from app.database.Database import Database
from app.database.mongo import MongoDatabase


def configure(binder):
    # binder.bind(MyService, to=MyService, scope=singleton)
    binder.bind(Database, to=MongoDatabase, scope=singleton)
    print("Hello!")
