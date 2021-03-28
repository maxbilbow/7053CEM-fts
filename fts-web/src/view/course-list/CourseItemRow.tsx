import React from "react";
import {Course} from "../../model/Course";

export default function CourseItemRow(props: { course: Course }) {
    const {title, outcomes, prerequisites} = props.course;
    return (
        <tr>
            <td>{title}</td><td>{outcomes.join(", ")}</td><td>{Object.keys(prerequisites).join(", ")}</td>
        </tr>
    );
}