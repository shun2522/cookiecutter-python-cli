import * as React from 'react';
import * as ReactDOM from 'react-dom';

interface HelloState {
    value: string;
    button?: boolean;
}

export class Hello extends React.Component<{}, HelloState> {

    constructor(props: any) {
        super(props);
        this.state = {
            value: '',
            button: true
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event: any) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event: any) {
        console.log(this.state.value);
        this.setState({value: ''});
    }

    render() {

        const field = (
            <div className="form-group">
                <label className="control-label">Form</label>
                <input className="form-control" value={this.state.value} onChange={this.handleChange}/>
            </div>
        );

        let disabled = '';
        let onClick = this.handleSubmit;
        if(!this.state.button) {
            disabled = 'disabled';
            onClick = null
        }
        const button = (
            <button className={"btn btn-default " + disabled} onClick={onClick}>Go</button>
        );

        return (
            <div>
                {field}
                {button}
            </div>
        );
    }
}

ReactDOM.render(
    <Hello/>,
    document.getElementById('js')
);
