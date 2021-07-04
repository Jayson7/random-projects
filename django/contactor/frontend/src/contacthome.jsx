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

    setInterval(() => {
      this.refreshList();
    }, 100000);
  }
  refreshList = () => {
    axios
      .get("/api/contact/")
      .then((res) => this.setState({ contactlist: res.data }))

      .catch((err) => console.log(err));
  };

  render() {
    return (
      <div>
        <div className="container justify-content-center bg-dark ">
          <br />
          <br />
          <h1 className="text-white mb-5 text-center">Contact List</h1>
          <div className="row ">
            <br />
            <br />
            {this.state.contactlist.map((item) => (
              <div className="col justify-content-center  text-center">
                <div
                  className="card mt-3 text-center m-3"
                  style={{ width: "18rem" }}
                >
                  <img
                    src={item.picture}
                    style={{
                      width: "18rem",
                      height: "13rem",
                      objectFit: "contain",
                      textAlign: "center",
                    }}
                    className="card-img-top"
                    alt="no pic"
                  ></img>
                  <div className="card-body  ">
                    <h2 className="card-title text-capitalize">
                      {item.first_name} - {item.last_name} -{item.pk}
                    </h2>
                    <h5 className="card-text">Number: {item.number} </h5>
                    <button
                      className="btn p-3 m-3 btn-primary"
                      onClick={() => {
                        axios
                          .get(`api/contact/${item.id}`)
                          .then((res) => console.log(res.data))
                          .catch((err) => console.log(err));
                      }}
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => {
                        axios
                          .get(`/delete/${item.id}`)
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
