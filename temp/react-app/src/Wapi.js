import { DatePicker, version, Input, Select } from 'antd';
import React from 'react';
import moment from 'moment';

const Option = Select.Option;
import 'antd/dist/antd.css';

const HTTP_HEAD = 'https://wxnacy.com'
export default class Wapi extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            method: "GET"
        }
    }
    

    render() {

        const selectBefore = (
            <Select defaultValue="Http://" style={{ width: 90 }}>
                <Option value="Http://">Http://</Option>
                <Option value="Https://">Https://</Option>
            </Select>
        );
        const selectAfter = (
            <Select defaultValue=".com" style={{ width: 80 }}>
                <Option value=".com">.com</Option>
                <Option value=".jp">.jp</Option>
                <Option value=".cn">.cn</Option>
                <Option value=".org">.org</Option>
            </Select>
        );


        return (
             <div style={{ margin: 24 }}>
                    <p style={{ marginBottom: 24 }}>
                        Current antd version: {version} <br/>
                        You can change antd version on the left panel (Dependencies section).
                    </p>
                    <Input addonBefore={selectBefore} addonAfter={selectAfter} defaultValue="mysite" />
                    <DatePicker defaultValue={moment()} />   
                </div>
            )
    }
}
