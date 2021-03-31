export interface Course {
    id: string;
    title: string;
    prerequisites: {skillId: string, level: number}[];
    outcomes: string[];
}
