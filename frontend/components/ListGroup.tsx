//import { Fragment } from "react";
//import type { MouseEvent } from "react";

import { useState } from "react";

function ListGroup() {
    let items = ["NY", "SF","Tokyo","London","Paris"];
    
    // Hook
    const [selectedIndex, setSelectedIndex] = useState(-1);

    // Event handler
    //const handleClick = (event: MouseEvent) => console.log(event);

    /**IF statement */
    const getMessage = () => {items.length == 0 ? <p>No items found</p>: null};

    return <>
            <h1>List</h1>
            {getMessage}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li 
                     className={
                        selectedIndex == index 
                        ? "list-group-item active"
                        : "list-group-item"} 
                     key={item} 
                     onClick={() => {setSelectedIndex(index);}} 
                    >
                        {item}
                    </li>
                ))};
            </ul>
        </>
}

export default ListGroup;