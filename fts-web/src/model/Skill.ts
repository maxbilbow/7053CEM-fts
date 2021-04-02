export enum SkillLevel {
    Low = 0,
    Medium = 1,
    High = 2
}

export class Skill {
    constructor(public id: string, public displayName: string) {
    }
}