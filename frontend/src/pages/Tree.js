import React, { Component, useEffect } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTree from "../components/Mytree";
import usersData from "./example.json";

export default function Tree(props){

    const [familyData, setFamilyData] = React.useState([]);
    const temp = [{"gender":"female","id":0,"name":"Lalita","pids":[3]},{"fid":3,"gender":"male","id":1,"mid":0,"name":"Akshay","pids":[]},{"fid":3,"gender":"male","id":2,"mid":0,"name":"Ashwath Niranja","pids":[]},{"gender":"male","id":3,"name":"Anantharaman","pids":[0]}]
    
    const downloadFile = ({ data, fileName, fileType }) => {
      const blob = new Blob([data], { type: fileType });
    
      const a = document.createElement("a");
      a.download = fileName;
      a.href = window.URL.createObjectURL(blob);
      const clickEvt = new MouseEvent("click", {
        view: window,
        bubbles: true,
        cancelable: true,
      });
      a.dispatchEvent(clickEvt);
      a.remove();
    };

    const exportToJson = e => {
      e.preventDefault();
      downloadFile({
        data: JSON.stringify(familyData),
        fileName: "answer.json",
        fileType: "text/json",
      });
    };
    

    useEffect(() => {
        setFamilyData(props.familyData);
        console.log(familyData);
    }, [props.familyData]);

    return ( 
      <>
      <div className="actionBtns">
          <button type="button" className='mt-5 py-2 px-4 rounded-md bg-green-500 text-gray-50 hover:bg-green-700' onClick={exportToJson}>
            Export to JSON
          </button>
        </div>
        <div className=' w-3/4 border border-1 my-4 mx-auto'>
        <FamilyTree
          nodes={familyData}
        />
      </div>
      </> 
      
    );
}
