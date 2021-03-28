export interface Course {
    id: string;
    title: string;
    "prerequisites": {[skill: string]: unknown};
    "outcomes": string[];
}
