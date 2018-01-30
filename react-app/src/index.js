import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Route} from 'react-router-dom'
import RunHTML from './RunHTML.js'

ReactDOM.render(
  <BrowserRouter>
    <div>
        <Route path="/runhtml/:id" component={RunHTML}/>
    </div>
  </BrowserRouter>, document.getElementById('root'));
registerServiceWorker();
