import ListGroup from "../components/ListGroup";
import Alert from "../components/Alert"; 
import Button from "../components/Button";
import { useState } from "react";

function App() {
  let items = ["New York","San Francisco","Tokyo","London","Paris"];
  const [alertVisible, setAlertVisibility] = useState(false);
  
  // Event handler
  const handleSelectItem = (item: string) => {
    console.log(item)
  }

  return (
    <div>
      {alertVisible == true ? <Alert onClose={() => setAlertVisibility(false)}>
        <strong>WARNING</strong> This is a crazy alert
        </Alert> : null}
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
      <ListGroup items={items} heading="Cities" onSelectItem={handleSelectItem}/>
    </div>  
  )
}

export default App; 