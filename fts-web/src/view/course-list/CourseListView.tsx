import React from "react";
import CourseItemRow from "./CourseItemRow";
import {Table} from "react-bootstrap";
import LoggerFactory from "../../service/LoggerFactory";
import {Course} from "../../model/Course";

const logger = LoggerFactory.getLogger("CourseListView");
export default class CourseListView extends React.Component<{  }, { courseList: Course[] }>{

    state = {
        courseList: []
    };

    constructor(props: { }) {
        super(props);
        this.update().catch(logger.error);
    }

    async update() {
        const response = await fetch("/api/course-list");
        this.setState({
            courseList: await response.json()
        });
    }

    render() {
        const courses = this.state.courseList.map(each => (<CourseItemRow course={each}/>));
        return (
            <Table>
                <tbody>
                {courses}
                </tbody>
            </Table>
        );
    }
}