import React, { Component } from "react";

import ContactList from "./contacthome";
import Editcontact from "./editcontact";
import Deletecontact from "./deletecontact";
import Signup from "./signup";
import Createcontact from "./createcontact";
import "bootstrap/dist/css/bootstrap.css";

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
export default class Nav extends Component {
  render() {
    return (
      <Router>
        <div>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/create">Add</Link>
            </li>
            <li>
              <Link to="/signup">Sign up</Link>
            </li>
          </ul>

          <hr />

          {/*
          A <Switch> looks through all its children <Route>
          elements and renders the first one whose path
          matches the current URL. Use a <Switch> any time
          you have multiple routes, but you want only one
          of them to render at a time
        */}
          <Switch>
            <Route exact path="/">
              <ContactList />
            </Route>
            <Route exact path="/api/delete">
              <Deletecontact />
            </Route>
            <Route exact path="/edit">
              <Editcontact />
            </Route>
            <Route exact path="/signup">
              <Signup />
            </Route>
            <Route exact path="/create">
              <Createcontact />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}
