import React from 'react';
import Input from './component/Input'
import Button from './component/Button'
import './component/Tab.css'


const styles = {
    headline: {
        fontSize: 24,
        paddingTop: 16,
        marginBottom: 12,
        fontWeight: 400,
    },
};

export default class Test extends React.Component {

    constructor(props) {
            super(props);
            this.state = {
                value: 'a',
            };
        }

        handleChange = (value) => {
            this.setState({
                value: value,
            });
        };
    onChangeInput(value) {
        this.setState({ value: value })
    }

    render() {
        return (
            <div></div>
        )
    }
}
