export interface Course {
    id: string;
    trainingManagerId?: string;
    title: string;
    synopsis: string;
    startTime: number;
    prerequisites: string[];
    outcomes: string[];
    relevance: number;
}
