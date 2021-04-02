import {UserProfile} from "../model/UserProfile";

export default class UserProfileService {
    static async getProfile() {
        return await fetch("/api/user-profile").then(res => res.json());
    }

    static async updateProfile(profile: UserProfile) {
        const result = await fetch("/api/user-profile", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                data: {
                    id: "user-profile",
                    type: "update",
                    attributes: {
                        profile
                    }
                }
            })
        })
        console.log("Profile updated", result.status);
    }
}
