import React, {FormEvent} from "react";
import Input from "./Input";

declare const window: Window;
export interface LoginFormProps {
    name: string;
    action: string;
    method: string;
    inputs: any[];
    error: string|null;
}
interface State {
    errorCount: number;
    failure?: string;
    errorMessages: { [field: string]: string }
}

export default class Form extends React.Component<LoginFormProps, State> {
    form!: HTMLFormElement;

    constructor(props: LoginFormProps) {
        super(props)
        if(props.error) {
            this.state = {
                failure: 'wrong username or password!',
                errorCount: 0,
                errorMessages: {}
            }
        } else {
            this.state = { errorCount: 0, errorMessages: {} }
        }
    }

    handleError = (field: string, errmsg: string) => {
        if(!field) return

        if(errmsg) {
            this.setState((prevState) => ({
                failure: '',
                errorCount: prevState.errorCount + 1,
                errorMessages: {...prevState.errorMessages, [field]: errmsg}
            }))
        } else {
            this.setState((prevState) => ({
                failure: '',
                errorCount: prevState.errorCount===1? 0 : prevState.errorCount-1,
                errorMessages: {...prevState.errorMessages, [field]: ''}
            }))
        }
    }

    renderError = () => {
        if(this.state.errorCount || this.state.failure) {
            const errmsg = this.state.failure
                || Object.values(this.state.errorMessages).find(v=>v)
            return <div className="error">{errmsg}</div>
        }
    }

    handleSubmit = (event: FormEvent) => {
        event.preventDefault()
        if(!this.state.errorCount) {
            const data = new FormData(this.form)
            fetch(this.form.action, {
                method: this.form.method,
                body: new URLSearchParams(data as URLSearchParams)
            })
                .then(v => {
                    if(v.redirected) window.location.href = v.url
                })
                .catch(e => console.warn(e))
        }
    }

    render() {
        const inputs = this.props.inputs.map(
            ({name, placeholder, type, value, className}, index) => (
                <Input key={index} name={name} placeholder={placeholder} type={type} value={value}
                       className={type==='submit'? className : ''} handleError={this.handleError} />
            )
        )
        const errors = this.renderError()
        return (
            <form {...this.props} onSubmit={this.handleSubmit} ref={fm => {this.form=fm!}} >
                {inputs}
                {errors}
            </form>
        )
    }
}
