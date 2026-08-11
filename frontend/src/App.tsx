//import ListGroup from "../components/ListGroup";
import Alert from "../components/Alert"; 
import Button from "../components/Button";
import { useEffect, useState } from "react";

function App() {
  // let items = ["New York","San Francisco","Tokyo","London","Paris"];
  // <ListGroup items={items} heading="Cities" onSelectItem={handleSelectItem}/>
  const [alertVisible, setAlertVisibility] = useState(false);

  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/health")
    .then((response) => response.json())
    .then((data) => setMessage(data.status));
  }, []);
  
  // Event handler
  //const handleSelectItem = (item: string) => {console.log(item)}

  return (
    <div>
      <h1>Earendil</h1>
      <p>Backend status: {message}</p>
      <div>
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
        </Alert> : null}
    </div>  
  );
}

export default App; 