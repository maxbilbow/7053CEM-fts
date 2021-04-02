import LoggerFactory from "./LoggerFactory";

interface AuthStatus {
    authenticated: boolean;
}

let authenticated = false;

const logger = LoggerFactory.getLogger("UserService");

export default class UserService {
    static toggle() {
        return authenticated = !authenticated;
    }
    /**
     * Can be used to quickly check login status (after checkAuthStatus() has been called once)
     */
    static get IS_LOGGED_IN() {
        return authenticated;
    }

    /**
     * Use this to determine the authentication status of the user.
     *  It should be used to refine UX but not as a gateway for restricted areas
     */
    static async checkAuthStatus(): Promise<boolean> {
        try {
            const response = await fetch("/auth/status");
            if (response.status === 200) {
                const status: AuthStatus = await response.json();
                authenticated = status.authenticated;
            }
            logger.info(`Authenticated: ${authenticated}`);
        } catch (e) {
            console.error("Unable to determine authentication state", e);
        }
        return authenticated;
    }
}
