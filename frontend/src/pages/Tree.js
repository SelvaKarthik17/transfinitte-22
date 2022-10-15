import React, { Component, useEffect } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTree from "../components/Mytree";

export default function Tree(props){

    const [familyData, setFamilyData] = React.useState([]);
    const temp = [{"id": 0, "name": "Nagaratnam", "pids": [], "gender": "female"}, {"id": 1, "name": "Sreedharan", "pids": [2], "gender": "male"}, {"id": 2, "name": "Maheshwari", "pids": [1], "gender": "female"}, {"id": 3, "name": "Sulaiman", "pids": [], "gender": "male", "fid": 4}, {"id": 4, "name": "Syed Alivi", "pids": [], "gender": "male"}, {"id": 5, "name": "Srinivasaragavan", "pids": [6], "gender": "male", "fid": 1, "mid": 2}, {"id": 6, "name": "Revathi", "pids": [5], "gender": "female"}, {"id": 7, "name": "Nandini", "pids": [], "gender": "female", "fid": 9}, {"id": 8, "name": "Arunkarthik", "pids": [], "gender": "male"}, {"id": 9, "name": "Ganesan", "pids": [], "gender": "male"}, {"id": 10, "name": "Saranyaphanu", "pids": [], "gender": "female"}, {"id": 11, "name": "Saravanan", "pids": [], "gender": "male", "fid": 12, "mid": 13}, {"id": 12, "name": "Pattappasamy", "pids": [13], "gender": "male"}, {"id": 13, "name": "Sumathi", "pids": [12], "gender": "female"}, {"id": 14, "name": "Bhupathiraj", "pids": [], "gender": "male", "fid": 12, "mid": 13}, {"id": 15, "name": "Kalachelvi", "pids": [], "gender": "female"}, {"id": 16, "name": "Gomati", "pids": [19], "gender": "female"}, {"id": 17, "name": "Soundaryabala", "pids": [], "gender": "female", "fid": 19, "mid": 16}, {"id": 18, "name": "Balasubramaniam", "pids": [], "gender": "male", "fid": 19, "mid": 16}, {"id": 19, "name": "Ramamurthy", "pids": [16], "gender": "male"}, {"id": 20, "name": "Kausalya", "pids": [], "gender": "female"}, {"id": 21, "name": "Sandhya", "pids": [], "gender": "female"}, {"id": 22, "name": "Ramya", "pids": [25], "gender": "female"}, {"id": 23, "name": "Arumugam", "pids": [], "gender": "male"}, {"id": 24, "name": "Muthukumar", "pids": [], "gender": "male"}, {"id": 25, "name": "Chandramouleswaran", "pids": [22], "gender": "male"}, {"id": 26, "name": "Satyakokila", "pids": [], "gender": "female"}, {"id": 27, "name": "Gandhi", "pids": [], "gender": "female"}, {"id": 28, "name": "Shanti", "pids": [], "gender": "female"}, {"id": 29, "name": "Saipreeta", "pids": [], "gender": "female"}]
    useEffect(() => {
        setFamilyData(props.familyData);
        console.log(familyData);
    }, [props.familyData]);

    return (  
      <div className=' w-3/4 border border-1 my-4 mx-auto'>
        <FamilyTree
          nodes={temp}
        />
      </div>
    );
}
