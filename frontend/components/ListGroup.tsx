//import { Fragment } from "react";

function ListGroup() {
    const items = ["NY", "SF","Tokyo","London","Paris"];

    /**IF statement */
    const getMessage = () => {items.length == 0 ? <p>No item found</p>: null}
    return <>
            <h1>List</h1>
            
            {getMessage}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li className="list-group-item" 
                        key={item} 
                        onClick={() => console.log(item, index)} 
                    >
                        {item}</li>
                    ))};
            </ul>
        </>
}

export default ListGroup;