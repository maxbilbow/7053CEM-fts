import {SkillLevel} from "./Skill";
import {Course} from "./Course";

interface CourseHistory {
    courses: { course: Course, date: number }[];
}

export interface UserProfile {
    name: string;
    email: string;
    competencies: string[];
    interests: string[];
}

