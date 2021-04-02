import React from "react";
import LoggerFactory from "../../service/LoggerFactory";
import {UserProfile} from "../../model/UserProfile";
import UserProfileService from "../../service/UserProfileService";
import {Alert, Button, Fade, Form} from "react-bootstrap";
import SkillsService from "../../service/SkillsService";
import {pullAt, noop, keyBy} from "lodash"
import "@pathofdev/react-tag-input/build/index.css";
import ReactTagInput from "@pathofdev/react-tag-input";
import {Skill} from "../../model/Skill";

const logger = LoggerFactory.getLogger("UserProfile");

enum UpdateResult {
    None = "", Success = "success", Error = "danger"
}

export default class UserProfileView extends React.Component<{}, UserProfile> {

    state!: UserProfile;
    skills: Skill[] = [];
    updateResult = UpdateResult.None;

    constructor(props = {}) {
        super(props);
        this.load().catch(logger.error);
    }

    async load() {
        this.skills = await SkillsService.getSkills();
        const profile = await UserProfileService.getProfile();
        this.setState({...profile});
    }

    update = async () => {
        const profile = this.state;
        try {
            await UserProfileService.updateProfile(profile);
            await this.load();
            this.updateResult = UpdateResult.Success;
        } catch (e) {
            logger.error(e)
            this.updateResult = UpdateResult.Error;
            this.setState({})
        }
    }

    render() {
        if (!this.state) {
            return (<p>...</p>)
        }
        const {competencies, interests, name, email} = this.state;

        return (
            <Form>
                <Form.Group controlId="name">
                    <Form.Label>Name</Form.Label>
                    <Form.Control type="text" placeholder="Full Name" value={name}
                                  onChange={evt => this.setState({name: evt.target.value})}/>
                </Form.Group>
                <Form.Group controlId="email">
                    <Form.Label>Name</Form.Label>
                    <Form.Control type="email" placeholder="name@example.com" value={email}
                                  onChange={evt => this.setState({email: evt.target.value})}/>
                </Form.Group>
                <Form.Group controlId="competencies">
                    <Form.Label>Experience</Form.Label>
                    <ReactTagInput tags={competencies}
                                   editable={true}
                                   removeOnBackspace={true}
                                   onChange={newTags => this.setState({competencies: newTags})}
                    />
                </Form.Group>
                <Form.Group controlId="interests">
                    <Form.Label>Interests</Form.Label>
                    <ReactTagInput tags={interests}
                                   removeOnBackspace={true}
                                   onChange={newTags => this.setState({interests: newTags})}
                    />
                </Form.Group>

                <Form.Group controlId="alert">
                    <Button variant="primary" type="button" onClick={this.update}>
                        Save
                    </Button>
                {this.alert()}
                </Form.Group>
            </Form>
        );
    }

    alert() {
        if (this.updateResult === UpdateResult.None) {
            return <></>
        } else {
            const message = UpdateResult.Success ? "Profile Updated" : "Failed to update profile"
            return (
                <Alert variant={this.updateResult}>
                    {message}
                </Alert>
            )
        }
    }

}
