import React from "react";
import {Course} from "../../model/Course";
import {useParams} from "react-router-dom";
import LoggerFactory from "../../service/LoggerFactory";
import * as stream from "stream";

const logger = LoggerFactory.getLogger("CourseInfoView")
export default class CourseInfo extends React.Component<{ id: string }, { course?: Course }> {
    state: { course?: Course } = {}

    constructor(readonly props: { id: string }) {
        super(props);
    }

    private async _load() {
        const response = await fetch(`/api/course-info/${this.props.id}`);
        if (response.ok) {
            this.setState({course: await response.json()});
        }
    }

    componentDidMount() {
        this._load().catch(logger.error)
    }

    render() {
        if (!this.state.course) {
            return (<>Not Yet</>)
        }
        const {id, title, outcomes, prerequisites, startTime, synopsis} = this.state.course;
        const date = new Date(startTime)
        return (
            <div>
                <div>Title: {title}</div>
                <div>Outcomes: {outcomes?.join(", ")}</div>
                <div>Prerequisites: {prerequisites?.map(o => JSON.stringify(o)).join(", ")}</div>
                <div>Date: {date.toLocaleDateString()}, Time: {date.toLocaleTimeString()}</div>

                <div>
                    <h4>Synopsis</h4>
                    <div>
                        {synopsis}
                    </div>
                </div>
                <div><a href={`/course-info/${id}`}>Register</a></div>
            </div>
        );
    }
}