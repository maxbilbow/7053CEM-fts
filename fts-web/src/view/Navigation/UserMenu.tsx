import {faUserCircle} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import React from "react";
import {Nav, NavDropdown} from "react-bootstrap";
import UserService from "../../service/UserService";
import {NavLink} from "react-router-dom";

interface State {
    result: Boolean;
}

export default class UserMenu extends React.Component<{}, State> {
    constructor(props: any) {
        super(props);
        this.state = {result: false};
        this.checkAuth();
    }

    private async checkAuth() {
        const result = await UserService.checkAuthStatus();
        this.setState({result});
    }

    render() {
        let menu: JSX.Element;
        if (this.state.result) {
            const title = (<FontAwesomeIcon icon={faUserCircle}/>);
            menu = (
                <NavDropdown id="user-menu" title={title} alignRight={true}>
                    <NavDropdown.Item as={NavLink} to="user-profile">Profile</NavDropdown.Item>
                    <NavDropdown.Item href="/logout">Log Out</NavDropdown.Item>
                </NavDropdown>
            )

        } else {
            menu = (
                <Nav.Link href="/login">Log In</Nav.Link>
            )
        }
        return (<Nav>{menu}</Nav>)
    }
}
