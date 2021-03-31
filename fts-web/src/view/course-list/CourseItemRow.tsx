import React from "react";
import {Course} from "../../model/Course";

export default function CourseItemRow(props: { course: Course }) {
    const {id, title, outcomes, prerequisites, startTime} = props.course;
    return (
        <tr>
            <td>{title}</td><td>{outcomes?.join(", ")}</td><td>{prerequisites?.map(o => JSON.stringify(o)).join(", ")}</td>
            <td>{new Date(startTime).toLocaleDateString()}</td>
            <td><a href={`/course-info/${id}`}>View Info</a></td>
        </tr>
    );
}