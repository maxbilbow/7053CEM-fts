import React from "react";
import {Course} from "../../model/Course";
import {Button, Form} from "react-bootstrap";

export default function CourseItemRow(props: { course: Course }) {
    const {id, title, outcomes, prerequisites, startTime} = props.course;
    return (
        <tr>
            <td>{title}</td>
            <td>{outcomes?.join(", ")}</td>
            <td>{prerequisites?.map(o => JSON.stringify(o)).join(", ")}</td>
            <td>{new Date(startTime).toLocaleDateString()}</td>

            <td>
                <Button variant="primary" type="button" href={`/course-info/${id}`}>
                    View
                </Button>
            </td>
        </tr>
    );
}