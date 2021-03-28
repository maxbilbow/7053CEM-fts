import React from "react";
import "./NavBar.css";
import UserMenu from "./UserMenu";
import {Nav, Navbar} from "react-bootstrap";
import {NavLink} from "react-router-dom";

export default function NavBar() {
    return (
        <Navbar collapseOnSelect expand="sm" bg="dark" variant="dark">
            <Navbar.Brand as={NavLink} to="/">Home</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link as={NavLink} to="/course-list">Courses</Nav.Link>
                </Nav>
                <UserMenu/>
            </Navbar.Collapse>
        </Navbar>
    );
}
