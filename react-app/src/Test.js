import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AceEditor from 'react-ace';

import 'brace/mode/css';
import 'brace/mode/html';
import 'brace/mode/javascript';
import 'brace/theme/monokai';

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

    render() {
        return (
        <MuiThemeProvider>
            <div style={{"height": "100% !important"}}>
                <div style={{"float": "left", "width": "50%" }}>
            <Tabs sytle={{"height": "100%"}}
                            value={this.state.value}
                            onChange={this.handleChange}
                        >
                            <Tab label="Tab A" value="a">
                                <div>
            <AceEditor style={{width: "100%"}} ref="htmlEditor" mode="html"
                theme="monokai" name="html" fontSize={14} showPrintMargin={true}
                showGutter={true} highlightActiveLine={true}
                editorProps={{$blockScrolling: true}}
                value={`<div>Hello world</div>`}
                setOptions={{ enableBasicAutocompletion: false,
                enableLiveAutocompletion: false, enableSnippets: false,
                showLineNumbers: true, tabSize: 2, }}/>
                                </div>
                            </Tab>
                            <Tab label="Tab B" value="b">
                                <div>
                                    <h2 style={styles.headline}>Controllable Tab B</h2>
                                    <p>
                                        This is another example of a controllable tab. Remember, if you
                                        use controllable Tabs, you need to give all of your tabs values or else
                                        you wont be able to select them.
                                    </p>
                                </div>
                            </Tab>
                        </Tabs>
                </div>
                <div style={{"float": "right", "width": "50%"}}>
                </div>
            </div>
                        </MuiThemeProvider>
        )
    }
}
