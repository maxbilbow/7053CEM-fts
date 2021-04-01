import React from "react";
import {Course} from "../../model/Course";
import LoggerFactory from "../../service/LoggerFactory";
import {Button} from "react-bootstrap";

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

    register = () => alert("not implemented")

    render() {
        if (!this.state.course) {
            return (<>Not Yet</>)
        }
        const {title, outcomes, prerequisites, startTime, synopsis} = this.state.course;
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
                <div>
                    <Button variant="primary" type="submit" onClick={this.register} disabled={CourseInfo.isDisabled(date)}>
                        Register
                    </Button>
                </div>
            </div>
        );
    }

    private static isDisabled(date: Date) {
        // To calculate the time difference of two dates
        const difference_In_Time = date.getTime() - new Date().getTime();
        const difference_In_Days = difference_In_Time / (1000 * 3600 * 24);
        return difference_In_Days < 1
    }
}