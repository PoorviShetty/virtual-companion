import "./App.css";
import React from "react";
import Chatbot from "./Chatbot";

function App() {
  return (
    <div className="App container-fluid bg-dark">
      <div className="row d-flex justify-content-center">
        <div className="col-md-5 py-5">
          <Chatbot />
        </div>
      </div>
    </div>
  );
}

export default App;
