import React, { PureComponent } from 'react';


export default class Input extends PureComponent {

    constructor(props) {
        super(props);
        this.state = {
            type: "text"
        }
    }

    onChange(e) {
        const { onChange } = this.props;
        if( onChange ){
            onChange(e.target.value)
        }
    }

    render() {
        const {type, ...otherProps} = this.props
        return (
            <input type={type} {...otherProps} onChange={ this.onChange.bind(this)} />
        )
    }
}
