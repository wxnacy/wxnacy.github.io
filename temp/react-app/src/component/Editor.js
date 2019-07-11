import React from 'react';
import brace from 'brace';
import AceEditor from 'react-ace';

import 'brace/mode/css';
import 'brace/mode/html';
import 'brace/mode/javascript';
import 'brace/theme/monokai';


export default class Editor extends React.Component {

    constructor(props) {
        super(props);

    }

    // shouldComponentUpdate(nextProps, nextState) {
        // if (this.state. !== nextState.htmlText) {
            // return false
        // } else {
            // return true;
        // }
    // }

    render() {
        const mode = this.props.mode;
        return (
            <AceEditor
                style={{width: "100%"}}
                mode={mode}
                theme="monokai"
                name={mode}
                onLoad={(newValue) => this.props.onLoad(newValue)}
                onChange={(newValue) => this.props.onChange(newValue, mode)}
                fontSize={14}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                editorProps={{$blockScrolling: true}}
                value={this.props.value}
                setOptions={{
                enableBasicAutocompletion: false,
                enableLiveAutocompletion: false,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 2,
                }}/>
        )
    }
}
