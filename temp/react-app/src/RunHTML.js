import React from 'react';
import { Button, Layout, Tabs  } from 'element-react';
import brace from 'brace';
import AceEditor from 'react-ace';
import { fetchPost, fetchGet } from './utils.js'
import asyncComponent from './AsyncComponent';

import 'brace/mode/css';
import 'brace/mode/html';
import 'brace/mode/javascript';
import 'brace/theme/monokai';

const defaultHtml = `<!DOCTYPE html>
<html lang="en">
 <head>
    <meta charset="UTF-8">
    <title></title>
 </head>
 <body>
    <p>Hello World</p>
 </body>
</html>
`
const defaultJS = `console.log("log")`
const defaultCss = `p {color: red}`
const defaultIframe = `<style>${defaultCss}</style>${defaultHtml}<script>${defaultJS}</script>`
// const HTTP_HEAD = 'http://localhost:8002'
const HTTP_HEAD = 'https://wxnacy.com'
export default class RunHTML extends React.Component {

    constructor(props) {
        super(props);
        // this.state = {
            // htmlText:defaultHtml,
            // jsText: defaultJS,
            // cssText: defaultCss
        // }
        this.state = {
            htmlText:'',
            jsText: '',
            cssText: ''
        }
    }

    componentDidMount() {
        let id = this.props.match.params.id
        this.fetchData(id)
    }

    run() {
        var preview = document.getElementById('preview')
        let htmlText = this.state.htmlText;
        let jsText = this.state.jsText;
        let cssText = this.state.cssText;

        let content = `<style>${cssText}</style>${htmlText}<script>${jsText}</script>`
        preview.srcdoc = content
    }

    save() {

        let code = {
            html: encodeURIComponent(this.state.htmlText),
            js: encodeURIComponent(this.state.jsText),
            css: encodeURIComponent(this.state.cssText)
        }
        let data = {
            name: "",
            code: code
        }

        fetchPost(`${HTTP_HEAD}/api/v1/code`, data).then(data => {
            console.log(data);
            let id = data.data.id
            window.location.href = `/runhtml/${id}`
        })

    }

    fetchData(id) {
        fetchGet(`${HTTP_HEAD}/api/v1/code/${id}`).then(data => {
            console.log(data);
            let code = data.data.code
            this.setState({
                htmlText: decodeURIComponent(code.html),
                jsText: decodeURIComponent(code.js),
                cssText: decodeURIComponent(code.css),
            })
            console.log(this.state)
            this.run()
        })
    }

    onLoad(editor, a) {
        let id = this.props.match.params.id
        this.fetchData(id)
    }

    shouldComponentUpdate(nextProps, nextState) {
        // https://github.com/securingsincity/react-ace/issues/181
        if (this.state.htmlText !== nextState.htmlText) {
            return false
        } else {
            return true;
        }
    }

    onChangeHtml(newValue) {
        this.setState({htmlText: newValue});
        console.log(this.state);
        console.log(newValue);
    }

    onChangeJS(newValue) {
        console.log(newValue);
        this.setState({jsText: newValue});
    }
    onChangeCss(newValue) {
        console.log(newValue);
        this.setState({cssText: newValue});
    }

    render() {
        const {htmlText, cssText, jsText} = this.state
        return (
            <Layout.Row gutter="20">
            <Layout.Col span="12">
            <Tabs type="card" value="1">
                <Tabs.Pane label="html" name="1">
            <AceEditor
                style={{width: "100%"}}
                ref="htmlEditor"
                mode="html"
                theme="monokai"
                name="html"
                onLoad={(newValue) => this.onLoad(newValue)}
                onChange={(newValue) => this.onChangeHtml(newValue)}
                fontSize={14}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                editorProps={{$blockScrolling: true}}
                value={htmlText}
                setOptions={{
                enableBasicAutocompletion: false,
                enableLiveAutocompletion: false,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 2,
                }}/>
                </Tabs.Pane>
                <Tabs.Pane label="js" name="2">

            <AceEditor
                style={{width: "100%"}}
                mode="javascript"
                theme="monokai"
                name="js"
                onChange={(newValue) => this.onChangeJS(newValue)}
                fontSize={14}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                value={this.state.jsText}
                setOptions={{
                enableBasicAutocompletion: false,
                enableLiveAutocompletion: false,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 2,
                }}/>
                </Tabs.Pane>
                <Tabs.Pane label="css" name="3">
            <AceEditor
                style={{width: "100%"}}
                mode="css"
                theme="monokai"
                name="css"
                onChange={(newValue) => this.onChangeCss(newValue)}
                fontSize={14}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                value={this.state.cssText}
                setOptions={{
                enableBasicAutocompletion: false,
                enableLiveAutocompletion: false,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 2,
                }}/>
                </Tabs.Pane>
            </Tabs>
            </Layout.Col>
            <Layout.Col span="12">
            <Button onClick={ this.run.bind(this) } type="success">运行</Button>
            <Button onClick={ this.save.bind(this) } type="primary"><i className="el-icon-upload "></i></Button>
            <div>
                <iframe id="preview" frameBorder="no" border="0"
                    style={{width: "100%", height: "700px"}} ></iframe>
            </div>
            <div id="log">

            </div>
            </Layout.Col>
            </Layout.Row>
        )
    }
}
