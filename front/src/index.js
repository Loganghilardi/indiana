import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/shared/Header/Header';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ListMovies from './components/ListMovies';

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <Header></Header>

        <Switch>
          <Route path="/" component={ListMovies} exact />
        </Switch>
      </div>
    </BrowserRouter>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
