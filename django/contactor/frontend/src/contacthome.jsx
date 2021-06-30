import React, { Component } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.css";
// import Nav from "./nav";
// import { BrowserRouter } from "react-router-dom";
export default class ContactList extends Component {
  constructor() {
    super();
    this.state = {
      contactlist: [],
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/contact/")
      .then((res) => this.setState({ contactlist: res.data }))
      .catch((err) => console.log(err));
  };

  render() {
    const baseURL = "http://localhost:8000/api";
    const headers = {
      "Content-type": "application/json",
    };

    return (
      <div>
        <div className="container bg-dark ">
          <br />
          <br />
          <h1 className="text-white mb-5 text-center">Contact List</h1>
          <div className="row ">
            <br />
            <br />
            {this.state.contactlist.map((item) => (
              <div  className="col-3 text-center">
                <div
                 className="card mt-3 text-center m-3"
                  style={{ width: "22rem" }}
                >
                  <img
                    src={item.picture}
                    style={{ width: "22rem", height: "22rem" }}
                    className="card-img-top"
                    alt="no pic"
                  ></img>
                  const id = {item.id}
                  console.log(id)
                  <div className="card-body  ">
                    <h2 className="card-title text-capitalize">
                      {item.first_name} - {item.last_name}
                    </h2>
                    <h5 className="card-text">Number: {item.number} </h5>
                    <button className="btn p-3 m-3 btn-primary">Edit</button>
                    <button
                      onClick={(id) => {
                        axios
                          .get(`/delete/${id}`)
                          .then((res) => console.log("done"))
                          .catch((err) => console.log(err));
                      }}
                      className="btn p-3 btn-danger"
                    >
                      Delete
                    </button>
                    <br />
                    <br />
                    <br />
                  </div>
                </div>
              </div>
            ))}
            <br />
          </div>
        </div>
      </div>
    );
  }
}
