import React from "react";
import {Col, Container, Row, Table} from "react-bootstrap";
import LoggerFactory from "../../service/LoggerFactory";
import {Course} from "../../model/Course";
import CourseListTable from "./CourseListTable";
import * as _ from "lodash";
import CourseListFilter, {CourseListFilterState} from "./CourseListFilter";
import {serialize} from "v8";
import UserService from "../../service/UserService";
import UserProfileService from "../../service/UserProfileService";
import {pre} from "../../../../../../Users/MaxBilbow/anaconda3/Lib/site-packages/bokeh/server/static/js/types/core/dom";

const logger = LoggerFactory.getLogger("CourseListView");

enum OrderBy {
    Date = "Date",
    Relevance = "Relevance"
}

class CourseListViewState extends CourseListFilterState {
    courseList?: Course[];
}


interface UserInfo {
    competencies: string[];
    interests: string[];
}

export default class CourseListView extends React.Component<{}, CourseListViewState> {

    state = new CourseListViewState();
    userProfile?: UserInfo;

    constructor(props: {}) {
        super(props);
    }

    async componentDidMount() {
        try {
            await this.update();
            if (!UserService.IS_LOGGED_IN) return;
            const {interests, competencies} = await UserProfileService.getProfile();
            this.userProfile = {interests, competencies};
            this.setState({})
        } catch (e) {
            logger.error("Unable to retrieve user profile", e)
        }
    }

    async update() {
        const response = await fetch("/api/course-list");
        const courseList = await response.json();
        this.setState({
            courseList
        });
    }

    static containsAny(tags: string[], searchTags: string[]): boolean {
        tags = tags.map(_.lowerCase);
        searchTags = searchTags.map(_.lowerCase);

        for (const tag of searchTags) {
            if (tags.includes(tag)) return true;
        }
        return false;//_.difference(tags, searchTags).length < tags.length;
    }

    private filterCourseList(filteredList: Course[]) {
        const {searchText, orderBy, outcomes} = this.state;
        if (outcomes.length) {
            logger.info("Filtering", outcomes)
            filteredList = filteredList.filter(course => CourseListView.containsAny(course.outcomes, outcomes))
            logger.info("Filtering", filteredList.length)
        }
        if (searchText) {
            filteredList = filteredList.filter(({title}) => title.includes(searchText))
        }
        if (orderBy === OrderBy.Relevance) {
            filteredList = filteredList.filter(({startTime}) => startTime < Date.now());
        }
        const order = orderBy === OrderBy.Relevance ? ["relevance", "startTime"] : ["startTime", "relevance"];
        return _.orderBy(filteredList, order);
    }

    render() {
        if (!this.state.courseList) {
            return <>...</>
        }
        const orderedList = this.filterCourseList(this.state.courseList)
        return (
            <Container>
                <Row>
                    <Col>
                        <Table>
                            <thead>
                            <tr>
                                <th>Filter Results</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td>
                                    <CourseListFilter courseList={this.state.courseList}
                                                      onChange={filter => this.setState(filter as CourseListViewState)}/>
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