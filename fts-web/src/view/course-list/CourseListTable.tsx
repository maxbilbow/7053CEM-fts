import React from "react";
import CourseItemRow from "./CourseItemRow";
import {Table} from "react-bootstrap";
import LoggerFactory from "../../service/LoggerFactory";
import {Course} from "../../model/Course";

const logger = LoggerFactory.getLogger("CourseListView");
export default class CourseListTable extends React.Component<{ courseList: Course[] }, {}> {
    constructor(readonly props: { courseList: Course[] }) {
        super(props);
    }

    render() {
        const courses = this.props.courseList.map(each => (<CourseItemRow course={each} key={each.id}/>));
        return (
            <Table>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>Prerequisites</th>
                    <th>Learning Outcomes</th>
                    <th>Date</th>
                </tr>
                </thead>
                <tbody>
                {courses}
                </tbody>
            </Table>
        );
    }
}