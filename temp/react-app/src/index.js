import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import asyncComponent from './AsyncComponent';

const Run = asyncComponent(() => import('./Run'));
const Test = asyncComponent(() => import('./Test'));

ReactDOM.render(
  <BrowserRouter>
    <Switch>
        <Route path="/test" component={Test}/>
        <Route exact strict path="/run" component={Run}/>
        <Route exact strict path="/run/:id" component={Run}/>
    </Switch>
  </BrowserRouter>, document.getElementById('root'));
registerServiceWorker();
