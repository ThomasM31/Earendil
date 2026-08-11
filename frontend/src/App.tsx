//import ListGroup from "../components/ListGroup";
// External
import { useEffect, useState } from "react";
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';
import {api} from "../api/api";

// Internal
import Dashboard from "../components/Dashboard/Dashboard";
import Preferences from "../components/Preferences/Preferences";
import Home from "../components/Home/Home";

import Alert from "../components/Alert"; 
import Button from "../components/Button";


function App() {
  // let items = ["New York","San Francisco","Tokyo","London","Paris"];
  // <ListGroup items={items} heading="Cities" onSelectItem={handleSelectItem}/>
  const [alertVisible, setAlertVisibility] = useState(false);

  const [status, setStatus] = useState("");

  useEffect(() => {
    api.get("/health")
    //.then((data) => setMessage(data.status))
    .then((response) => {
      console.log(response.data);
      setStatus(response.data.status);
    })
    .catch(error => console.log(error));
  }, []);
  
  // Event handler
  //const handleSelectItem = (item: string) => {console.log(item)}

  return (
    <div className="wrapper">
      <h1>Earendil</h1>
      <p>Backend status: {status}</p>
      <BrowserRouter>
        <nav>
          <Link to={"/"}>Home</Link>{" "}
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/preferences" element={<Preferences />} />  
          <Route path="*" element={<p>Path not resolved</p>} />
        </Routes>  
      </BrowserRouter>
      {/*<div>
        <Button color="primary" onClick={() => console.log("Clicked primary button")}>
          My Primary Button
        </Button>
        <Button color="secondary" onClick={() => console.log("Clicked secondary button")}>
          My Secondary Button
        </Button>
        <Button color="warning" onClick={() => console.log("Clicked warning button")}>
          Warning Button
        </Button>
        <Button color="danger" onClick={() => setAlertVisibility(true)}>
          My Danger Button
        </Button>
      </div>
        {alertVisible == true ? <Alert onClose={() => setAlertVisibility(false)}>
        <strong>WARNING</strong> This is a crazy alert
        </Alert> : null} */}
    </div>
  );
}

export default App; 