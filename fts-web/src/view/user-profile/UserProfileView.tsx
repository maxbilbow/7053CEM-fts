import React from "react";
import LoggerFactory from "../../service/LoggerFactory";
import {UserProfile} from "../../model/UserProfile";
import UserProfileService from "../../service/UserProfileService";
import {Form} from "react-bootstrap";
import SkillsService from "../../service/SkillsService";
import {pullAt, noop} from "lodash"
import "@pathofdev/react-tag-input/build/index.css";
import ReactTagInput from "@pathofdev/react-tag-input";
import {Skill} from "../../model/Skill";
import { WithContext as ReactTags } from "react-tag-input";

const logger = LoggerFactory.getLogger("UserProfile");


export default class UserProfileView extends React.Component<{}, UserProfile> {

    state = {
        name: "",
        email: "",
        competencies: [],
        interests: []
    };
    skills: { text: string, id:string }[] = []
    profile!: UserProfile;
    competencies: { text: string, id:string }[] = [];
    interests: { text: string, id:string }[] = [];

    constructor(props = {}) {
        super(props);
        this.load().catch(logger.error);
    }

    async load() {
        this.skills = (await SkillsService.getSkills()).map(({id, displayName}) => ({id, text: displayName}));
        const profile = await UserProfileService.getProfile();
        this.profile = profile;
        this.setState({...profile});
    }

    update = async () => {
        const profile = this.profile;
        const {competencies, interests, name, email} = this.state;
        profile.competencies = competencies;
        profile.interests = interests;
        profile.name = name;
        profile.email = email;
        await UserProfileService.updateProfile(profile).catch(logger.error);
        return this.load().catch(logger.error);
    }

    render() {
        if (!this.profile) {
            return (<p>...</p>)
        }
        const {competencies, interests, name, email} = this.state;

        return (
            <Form>
                <div><label>Name:</label> <input value={name} onChange={evt => this.setState({name: evt.target.value})}/></div>
                <div><label>Email:</label> <input value={email} onChange={evt => this.setState({email: evt.target.value})}/></div>
                <div><label>Experience:</label>
                    <ReactTagInput tags={competencies}
                                   editable={true}
                                   removeOnBackspace={true}
                                   onChange={newTags => this.setState({competencies: newTags})}
                    />
                </div>
                <div><label>Interests:</label>
                    {/*<ReactTagInput tags={interests}*/}
                    {/*               removeOnBackspace={true}*/}
                    {/*               onChange={newTags => this.setState({interests: newTags})}*/}
                    {/*/>*/}

                    <ReactTags
                        tags={interests}
                        suggestions={this.skills}
                        handleDelete={noop}
                        handleAddition={noop}
                        handleDrag={noop}
                        handleTagClick={noop}
                    />
                </div>
                <button onClick={this.update}>Save</button>
            </Form>
        );
    }

}
