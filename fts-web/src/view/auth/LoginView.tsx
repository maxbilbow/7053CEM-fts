import React from "react";
import Form from "./Form";

export default function LoginView() {
    const inputs = [{
        name: "username",
        placeholder: "username",
        type: "text"
    },{
        name: "password",
        placeholder: "password",
        type: "password"
    },{
        type: "submit",
        value: "Submit",
        className: "btn"
    }]

    const props = {
        name: 'loginForm',
        method: 'POST',
        action: '/perform_login',
        inputs: inputs
    }

    const params = new URLSearchParams(window.location.search);
    return (<Form {...props} error={params.get('error')} />)
}