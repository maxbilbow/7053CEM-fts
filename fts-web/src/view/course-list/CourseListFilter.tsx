import React from "react";
import CourseItemRow from "./CourseItemRow";
import {Col, Container, Form, FormGroup, Row, Table} from "react-bootstrap";
import LoggerFactory from "../../service/LoggerFactory";
import {Course} from "../../model/Course";
import CourseListTable from "./CourseListTable";
import * as _ from "lodash";
import ReactTagInput from "@pathofdev/react-tag-input";
import {UserProfile} from "../../model/UserProfile";
import UserService from "../../service/UserService";
import UserProfileService from "../../service/UserProfileService";

const logger = LoggerFactory.getLogger("CourseListFilter");

enum OrderBy {
    Date = "Date",
    Relevance = "Relevance"
}

export class CourseListFilterState {
    searchText = ""
    orderBy = OrderBy.Relevance;
    outcomes: string[] = [];
}

interface Props {
    courseList: Course[];
    onChange(filter: Partial<CourseListFilterState>): void;
}



export default class CourseListFilter extends React.Component<Props, CourseListFilterState> {

    state = new CourseListFilterState();

    constructor(props: Props) {
        super(props);
    }

    updateState(state: Partial<CourseListFilterState>) {
        this.setState(state as CourseListFilterState)
        this.props.onChange(state);
    }

    componentDidMount() {
        const {courseList} = this.props;
        this.updateState({
            outcomes: _.uniq(_.flatMap(courseList, "outcomes"))
        })
    }

    render() {
        const {searchText, outcomes} = this.state;
        return (
            <Form>
                <Form.Row>
                    <Form.Control type="text" placeholder="Search" value={searchText}
                                  onChange={evt => this.updateState({searchText: evt.target.value})}/>
                </Form.Row>
                <fieldset name={"orderby"} defaultValue={OrderBy.Relevance}>
                    <Form.Group as={Row} controlId={"orderby"} value={OrderBy.Relevance}>
                        <Col sm={10}>
                            <Form.Check onChange={() => this.updateState({orderBy: OrderBy.Relevance})}
                                        type="radio"
                                        id={`OrderBy-${OrderBy.Relevance}`}
                                        value={OrderBy.Relevance}
                                        label={"order by relevance"}
                                        name="orderby"
                                        defaultChecked
                            />
                            <Form.Check onChange={() => this.updateState({orderBy: OrderBy.Date})}
                                        type="radio"
                                        id={`OrderBy-${OrderBy.Date}`}
                                        value={OrderBy.Date}
                                        label={"order by date"}
                                        name="orderby"
                            />
                        </Col>
                    </Form.Group>
                </fieldset>
                <Form.Row>
                    <Form.Label>Include Topics:
                        <ReactTagInput tags={outcomes}
                                       editable={false}
                                       removeOnBackspace={true}
                                       onChange={newTags => this.updateState({outcomes: newTags})}>
                        </ReactTagInput>
                    </Form.Label>
                </Form.Row>
            </Form>

        );
    }
}