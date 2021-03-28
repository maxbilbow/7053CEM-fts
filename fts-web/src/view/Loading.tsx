import React from "react";
import {Spinner} from "react-bootstrap";
import "./Loading.css"

export default class Loading extends React.Component {
  isLoading: Boolean = true;

  delete() {
    this.isLoading = false;
  }

  render() {
    if (this.isLoading) {
      return (
        <div className="Loading">
          <Spinner animation="border" role="status">
            <span className="sr-only">Loading...</span>
          </Spinner>
          <p id="loading-state">Finding places...</p>
        </div>
      );
    }
    return null;
  }
}
