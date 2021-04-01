import {UserProfile} from "../model/UserProfile";
import {Skill} from "../model/Skill";

export default class SkillsService {
    static async getSkills(): Promise<Skill[]> {
        return await fetch("/api/skill-list").then(res => res.json());
    }
}
