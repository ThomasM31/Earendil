//import { Fragment } from "react";
//import type { MouseEvent } from "react";
import { useState } from "react";

interface Props {
    items: string[];
    heading: string;
    onSelectItem: (item: string) => void;
}

function ListGroup({items, heading, onSelectItem}: Props) {
    // Hook
    const [selectedIndex, setSelectedIndex] = useState(-1);

    /**IF statement */
    const getMessage = () => {items.length == 0 ? <p>No items found</p>: null};

    return <>
            <h1>{heading}</h1>
            {getMessage}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li 
                     className={
                        selectedIndex == index 
                        ? "list-group-item active"
                        : "list-group-item"} 
                     key={item} 
                     onClick={() => {
                        setSelectedIndex(index);
                        onSelectItem(item);
                    }} 
                    >
                        {item}
                    </li>
                ))};
            </ul>
        </>
}

export default ListGroup;