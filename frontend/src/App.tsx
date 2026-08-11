//import ListGroup from "../components/ListGroup";
// External
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';

// Internal
import Dashboard from "../pages/Dashboard/Dashboard";
import Preferences from "../pages/Preferences/Preferences";
import Home from "../pages/Home/Home";
import Login from "../pages/Login/Login";
import "./App.css";

function App() {
  // Event handler
  //const handleSelectItem = (item: string) => {console.log(item)}

  return (
    <div className="wrapper">
      <h1>Earendil</h1>
      <BrowserRouter>
        <nav>
          <Link to={"/"}>Home</Link>{" "}
          <Link to={"/login"}>Login</Link>{" "}
          <Link to={"/dashboard"}>Dashboard</Link>{" "}
          <Link to={"/preferences"}>Preferences</Link>{" "}
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
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