import React from "react";
import {Course} from "../../model/Course";
import LoggerFactory from "../../service/LoggerFactory";
import {Button, Col, Container, Form, Row} from "react-bootstrap";

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
            <Container>
                <Row>
                    <Col className={"courseInfo__label"}>
                        Title
                    </Col>
                    <Col xs={9}>
                        {title}
                    </Col>
                </Row>
                <Row>
                    <Col className={"courseInfo__label"}>
                        {"Outcomes"}
                    </Col>
                    <Col xs={9}>
                        {outcomes?.join(", ")}
                    </Col>
                </Row>
                <Row>
                    <Col className={"courseInfo__label"}>
                        Interests
                    </Col>
                    <Col xs={9}>
                        {prerequisites?.join(", ")}
                    </Col>
                </Row>
                <Row>
                    <Col className={"courseInfo__label"}>
                        Start Time
                    </Col>
                    <Col xs={9}>
                        {date.toLocaleDateString()} at {date.toLocaleTimeString()}
                    </Col>
                </Row>
                <Row>
                    <Col className={"courseInfo__label"}>
                        Synopsis
                    </Col>
                    <Col xs={9}>
                        {synopsis}
                    </Col>
                </Row>
                <Row>
                   <hr/>
                </Row>
                <Row>
                    <Col className={"courseInfo__label"}>
                    </Col>
                    <Col xs={9}>
                        <Button variant="primary" type="submit" onClick={this.register}
                                disabled={CourseInfo.isDisabled(date)}>
                            Register
                        </Button>
                    </Col>
                </Row>
            </Container>
        );
    }

    private static isDisabled(date: Date) {
        // To calculate the time difference of two dates
        const difference_In_Time = date.getTime() - new Date().getTime();
        const difference_In_Days = difference_In_Time / (1000 * 3600 * 24);
        return difference_In_Days < 1
    }
}