import { useEffect, useState } from "react";
import {api} from "../../api/api";

function Home() {
  const [status, setStatus] = useState("");

  useEffect(() => {
    api.get("/health")
    .then((response) => {
      console.log(response.data);
      setStatus(response.data.status);
    })
    .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <p>Backend status: {status}</p>
    </div>
  )
}

export default Home;