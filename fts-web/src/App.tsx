import "bootstrap/dist/css/bootstrap.min.css"
import React from "react";
import {Container} from 'react-bootstrap';
import {BrowserRouter, Link, Route, Redirect} from "react-router-dom";
import "./App.css";
import UserService from "./service/UserService";
import NavBar from "./view/Navigation/NavBar";
import licensing from "./view/Licensing";
import CourseListView from "./view/course-list/CourseListView";
import UserProfileView from "./view/user-profile/UserProfileView";
import LoginView from "./view/auth/LoginView";
import CourseInfoView from "./view/course-info/CourseInfoView";

UserService.checkAuthStatus()
    .then((r) => console.log("Logged in:", r))
    .catch(console.error);

export default function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <header className="App-header">
                   <NavBar/>
                </header>

                <div className="content">
                    <Container>
                        <Route exact path="/">
                            <Redirect to="/course-list"/>
                        </Route>
                        <Route path="/licensing" component={licensing}/>
                        <Route path="/course-list" component={CourseListView}/>
                        <Route path="/course-info/:id" component={CourseInfoView}/>
                        <Route path="/user-profile" component={UserProfileView}/>
                        <Route path="/login" component={LoginView}/>
                    </Container>
                </div>

                <div className="footer">
                    Copyright © 2021 |
                    <Link className="footer-link" to="/licensing">Licensing</Link>
                </div>
            </BrowserRouter>
        </div>
    );
}
