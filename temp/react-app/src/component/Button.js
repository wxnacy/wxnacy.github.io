import React, { PureComponent } from 'react';


export default class Button extends PureComponent {

    // constructor(props) {
        // super(props);
        // this.state = {
            // type: "text"
        // }
    // }

    onClick(e) {
        const { onClick } = this.props;
        if( onClick ){
            onClick(e);
        }
    }

    render() {
        const {type, ...otherProps} = this.props
        return (
            <button type={type} {...otherProps} onClick={ this.onClick.bind(this)} />
        )
    }
}
