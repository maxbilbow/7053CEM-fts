import "bootstrap/dist/css/bootstrap.min.css"
import React from "react";
import {Container} from 'react-bootstrap';
import {BrowserRouter, Link, Route} from "react-router-dom";
import "./App.css";
import UserService from "./service/UserService";
import NavBar from "./view/Navigation/NavBar";
import licensing from "./view/Licensing";
import CourseListView from "./view/course-list/CourseListView";
import UserProfileView from "./view/user-profile/UserProfileView";
import LoginView from "./view/auth/LoginView";

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

                <div className="content text-center">
                    <Container>
                        <Route exact path="/">
                            Hi
                        </Route>
                        <Route path="/licensing" component={licensing}/>
                        <Route path="/course-list" component={CourseListView}/>
                        <Route path="/user-profile" component={UserProfileView}/>
                        <Route path="/login" component={LoginView}/>
                    </Container>
                </div>

                <div className="footer">
                    MADE WITH LOVE BY COVENTRY UNIVERSITY STUDENTS
                    <br/>
                    Copyright © 2020 |
                    <Link className="footer-link" to="/licensing">Licensing</Link>
                </div>
            </BrowserRouter>

        </div>
    );
}
