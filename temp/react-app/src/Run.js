import React, { PureComponent } from 'react';
import brace from 'brace';
import AceEditor from 'react-ace';
import { fetchPost, fetchGet } from './utils.js'
import Input from './component/Input'
import Button from './component/Button'
import { Tabs } from 'antd';

import 'brace/mode/css';
import 'brace/mode/html';
import 'brace/mode/javascript';
import 'brace/theme/monokai';

const TabPane = Tabs.TabPane;
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
export default class Run extends PureComponent {

    constructor(props) {
        super(props);
        this.state = {
            htmlText:'',
            jsText: '',
            cssText: '',
            name: "",
            description: ""
        }
        this.id = this.props.match.params.id || "";
    }

    initData() {
        if( this.id ){
            this.fetchData(this.id)
        } else {
            this.setState({
                htmlText: defaultHtml,
                jsText: defaultJS,
                cssText: defaultCss
            })
        }
    }

    componentDidMount() {
        this.initData()
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
            name: this.state.name,
            description: this.state.description,
            code: code
        }

        fetchPost(`${HTTP_HEAD}/api/v1/code`, data).then(data => {
            console.log(data);
            let id = data.data.id
            window.location.href = `/run/${id}`
        })

    }

    fetchData(id) {
        fetchGet(`${HTTP_HEAD}/api/v1/code/${id}`).then(data => {
            console.log(data);
            data = data.data
            let code = data.code
            this.setState({
                htmlText: decodeURIComponent(code.html),
                jsText: decodeURIComponent(code.js),
                cssText: decodeURIComponent(code.css),
                name: data.name,
                description: data.description
            })
            console.log(this.state)
            this.run()
        })
    }

    onLoad(editor, a) {
        this.initData()
    }


    onChange(newValue, mode) {
        if( mode === "html" ){
            this.setState({htmlText: newValue});
        } else if( mode === "javascript" ){
            this.setState({jsText: newValue});
        } else if( mode === "css" ){
            this.setState({cssText: newValue});
        }
        console.log(newValue, mode);

    }

    onSelectInput(value) {
        console.log("input ", value);
    }


    initEditor(mode, value) {

        return (
            <AceEditor
                style={{width: "100%"}}
                mode={mode}
                theme="monokai"
                name={mode}
                onLoad={(newValue) => this.onLoad(newValue)}
                onChange={(newValue) => this.onChange(newValue, mode)}
                fontSize={14}
                showPrintMargin={true}
                showGutter={true}
                highlightActiveLine={true}
                editorProps={{$blockScrolling: true}}
                value={value}
                setOptions={{
                enableBasicAutocompletion: false,
                enableLiveAutocompletion: false,
                enableSnippets: false,
                showLineNumbers: true,
                tabSize: 2,
                }}/>
        )
    }

    onNameChange(value) {
        this.setState({name: value})
    }
    onDescChange(value) {
        this.setState({description: value})
    }


    render() {
        const {htmlText, cssText, jsText} = this.state
        return (
            <div>
                <div style={{ float: "left", width: "15%" }}>
                    title
                    <Input placeholder="名称" value={ this.state.name } onChange={ this.onNameChange.bind(this) }/>
                    description
                    <Input placeholder="描述" type="textarea" value={this.state.description} onChange={ this.onDescChange.bind(this) }/>
                </div>
                <div style={{ float: "left", width: "40%" }}>
                    <Tabs defaultActiveKey="1" >
                            <TabPane tab="Tab 1" key="1">
                            { this.initEditor("html", this.state.htmlText) }
                            </TabPane>
                            <TabPane tab="Tab 2" key="2">
                            { this.initEditor("javascript", this.state.jsText) }
                            </TabPane>
                            <TabPane tab="Tab 3" key="3">
                            { this.initEditor("css", this.state.cssText) }
                            </TabPane>
                    </Tabs>


                </div>
                <div style={{ float: "left", width: "40%" }}>
                    <Button onClick={ this.run.bind(this) } >运行</Button>
                    <Button onClick={ this.save.bind(this) } >保存</Button>
                    <div >
                        <iframe id="preview" frameBorder="no" border="0"
                            style={{width: "100%", height: "700px"}} ></iframe>
                    </div>
                </div>

            </div>
        )
    }
}
