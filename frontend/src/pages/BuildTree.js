import React, { Component, useEffect, useState } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTree from "../components/Mytree";
import data from "../FinalFamilyData.json";

export default function BuildTree(props) {
  /*const [familyData, setFamilyData] = React.useState([]);
    const temp = [{"gender":"female","id":0,"name":"Lalita","pids":[3]},{"fid":3,"gender":"male","id":1,"mid":0,"name":"Akshay","pids":[]},{"fid":3,"gender":"male","id":2,"mid":0,"name":"Ashwath Niranja","pids":[]},{"gender":"male","id":3,"name":"Anantharaman","pids":[0]}]
    const [files, setFiles] = useState(null);
    const [load, setLoad] = useState(false);

    const handleChange = e => {
        //e.preventDefault();
        const fileReader = new FileReader();
        fileReader.readAsText(e.target.files[0], "UTF-8");
        fileReader.onload = e => {
        console.log("e.target.result", e.target.result);
        //let a = JSON.parse(JSON.stringify(e.target.result));
        setFiles(e.target.result);
        setLoad(true);
        console.log("---");
        console.log(files);
        console.log(Array.isArray(files));
        };
  };

  const btnclick = e => {
    e.preventDefault();
    console.log(files.length);
    console.log(typeof files);
  };

    return ( 
      <>
      <div className="actionBtns">
          <input type="file" className='mt-5 py-2 px-4 rounded-md bg-green-500 text-gray-50 hover:bg-green-700' onClick={handleChange} />
        </div>

        <button onClick={btnclick}> check files</button>

        
        {load && <div className=' w-3/4 border border-1 my-4 mx-auto'>
            {files}
        <FamilyTree
          nodes={files}
        />
        </div>}
        
      </> 
      
    );*/

  const [jsonData, setData] = useState(data);
  // Fetch Function
  // useEffect(() => {
  //   fetch("./all.json")
  //     .then(function (res) {
  //       return res.json();
  //     })
  //     .then(function (data) {
  //       // store Data in State Data Variable
  //       setData(data);
  //       console.log(jsonData);
  //     })
  //     .catch(function (err) {
  //       console.log(err, " error");
  //     });
  // }, []);
  // console.log(data.slice(0, 25));
  return (
    <>
      <Header />
      <div className=' w-1/2 border border-1 my-4 mx-auto'>
        <FamilyTree nodes={jsonData.slice(0, 10)} />
      </div>

      <Footer />
    </>
  );
}
