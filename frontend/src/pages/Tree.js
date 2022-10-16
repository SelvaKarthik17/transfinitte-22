import React, { Component, useEffect } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTreeClass from "../components/Mytree";
import usersData from "./example.json";

export default function Tree(props) {
  const { familyData } = props;
  const [propsData, setFamilyData] = React.useState([]);
  const temp = [
    { gender: "female", id: 0, name: "Lalita", pids: [3] },
    { fid: 3, gender: "male", id: 1, mid: 0, name: "Akshay", pids: [] },
    {
      fid: 3,
      gender: "male",
      id: 2,
      mid: 0,
      name: "Ashwath Niranja",
      pids: [],
    },
    { gender: "male", id: 3, name: "Anantharaman", pids: [0] },
  ];

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

  const exportToJson = (e) => {
    e.preventDefault();
    console.log(familyData);
    downloadFile({
      data: JSON.stringify(familyData),
      fileName: "answer.json",
      fileType: "text/json",
    });
  };

  useEffect(() => {
    console.log("hi");
    setFamilyData(props.familyData);
    console.log(familyData);
  }, []);

  return (
    <>
      <div className=' w-3/4 border border-1 my-4 mx-auto'>
        {props.familyData ? (
          <>
            <FamilyTreeClass nodes={props.familyData} />
          </>
        ) : (
          ""
        )}
      </div>
    </>
  );
}
