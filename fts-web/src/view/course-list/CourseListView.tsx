import React from "react";
import {Col, Container, Row, Table} from "react-bootstrap";
import LoggerFactory from "../../service/LoggerFactory";
import {Course} from "../../model/Course";
import CourseListTable from "./CourseListTable";
import * as _ from "lodash";
import CourseListFilter, {CourseListFilterState} from "./CourseListFilter";
import {serialize} from "v8";

const logger = LoggerFactory.getLogger("CourseListView");

enum OrderBy {
    Date = "Date",
    Relevance = "Relevance"
}

class CourseListViewState extends CourseListFilterState {
    courseList: Course[] = [];
}

export default class CourseListView extends React.Component<{}, CourseListViewState> {

    state = new CourseListViewState();

    constructor(props: {}) {
        super(props);
        this.update().catch(logger.error);
    }

    async update() {
        const response = await fetch("/api/course-list");
        this.setState({
            courseList: await response.json()
        });
    }

    static containsAny(tags: string[], searchTags: string[]): boolean {
        tags = tags.map(_.snakeCase).map(_.lowerCase);
        searchTags = searchTags.map(_.snakeCase).map(_.lowerCase);

        return _.difference(tags, searchTags).length < tags.length;
    }
    private filterCourseList() {
        const {searchText, courseList, orderBy, prerequisites, outcomes} = this.state;
        let filteredList = courseList;
        if (prerequisites.length) {
            filteredList = filteredList.filter(course => !CourseListView.containsAny(course.prerequisites, prerequisites))
        }
        if (outcomes.length) {
            filteredList = filteredList.filter(course => CourseListView.containsAny(course.outcomes, outcomes))
        }
        if (searchText) {
            filteredList = courseList.filter(({title}) => title.includes(searchText))
        }
        const order = orderBy === OrderBy.Relevance ? ["relevance", "startTime"] : ["startTime", "relevance"];
        return _.orderBy(filteredList, order);
    }
    render() {

        const orderedList = this.filterCourseList()
        return (
            <Container>
                <Row>
                    <Col>
                        <Table>
                            <thead>
                            <th>Filter Results</th>
                            </thead>
                            <tbody>
                            <tr>
                                <td>
                                    <CourseListFilter onChange={filter => this.setState(filter as CourseListViewState)}/>
                                </td>
                            </tr>
                            </tbody>
                        </Table>

                    </Col>
                    <Col xs={9}>
                        <CourseListTable courseList={orderedList}/>
                    </Col>
                </Row>
            </Container>
        );
    }
}