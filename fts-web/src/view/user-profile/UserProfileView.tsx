import React from "react";
import LoggerFactory from "../../service/LoggerFactory";
import {UserProfile} from "../../model/UserProfile";
import UserProfileService from "../../service/UserProfileService";
import {log} from "util";

const logger = LoggerFactory.getLogger("UserProfile");
export default class UserProfileView extends React.Component<{}, UserProfile> {

    constructor(props = {}) {
        super(props);
        this.load().catch(logger.error);
    }

    async load() {
        this.setState(await UserProfileService.getProfile())
    }

    update = async () => {
        this.state.skills["A"]++;
        await UserProfileService.updateProfile(this.state).catch(logger.error);
        return this.load().catch(logger.error);
    }

    render() {
        if (!this.state) {
            return (<p>...</p>)
        }
        const {name, skills} = this.state;
        return (
            <>
                <p>Name: {name}</p>
                <p>Skills: {JSON.stringify(skills)}</p>
                <button onClick={this.update}>Update</button>
            </>
        );
    }
}