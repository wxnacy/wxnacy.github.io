import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import asyncComponent from './AsyncComponent';

const RunHTML = asyncComponent(() => import('./RunHTML'));

ReactDOM.render(
  <BrowserRouter>
    <Switch>
        <Route path="/runhtml/:id" component={RunHTML}/>
        <Route path="/wapi/:id" component={RunHTML}/>
    </Switch>
  </BrowserRouter>, document.getElementById('root'));
registerServiceWorker();
