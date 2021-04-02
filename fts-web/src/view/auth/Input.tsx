import React, {Component} from 'react'
import LoggerFactory from "../../service/LoggerFactory";

export interface InputProps {
    name: string;
    value?: string,
    className?: string;
    placeholder?: string;
    type?: string;
    handleError?: Function;
}

interface State {
    value: string;
    className: string;
    error: boolean;
}

const logger = LoggerFactory.getLogger("Input");
export default class Input extends Component<InputProps, State> {
    readonly props!: InputProps;
    handleError?: Function;

    constructor(props: InputProps) {
        super(props)
        this.state = {
            value: props.value ? props.value : '',
            className: props.className ? props.className : '',
            error: false
        }
    }

    inputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        this.setState({value: event.target.value})
    };

    render() {
        const {handleError, ...opts} = this.props
        this.handleError = handleError
        return (
            <input {...opts} value={this.state.value}
                   onChange={this.inputChange} className={this.state.className}/>
        )
    }
}

