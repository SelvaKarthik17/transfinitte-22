import React, { Component } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
//import { LockClosedIcon } from '@heroicons/react/solid'
import axios from "axios";
export default function GetFamily() {
  const [states, setStates] = React.useState(["Tamil Nadu"]);
  const [name, setName] = React.useState("");
  const [fatherName, setFatherName] = React.useState("");
  const [state, setState] = React.useState("");
  const [age, setAge] = React.useState("");
  const [vid, setVid] = React.useState("");
  const [gender, setGender] = React.useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // replace states with state codes if needed
    //tn is S22
    /* let reqBody = {
            name: name,
            relation_name: fatherName,
            state: state,
            age: age,
            voter_id: vid,
            gender: gender,
        } */

    var bodyFormData = new FormData();
    bodyFormData.append("name", name);
    bodyFormData.append("relation_name", fatherName);
    bodyFormData.append("state", state);
    bodyFormData.append("age", age);
    bodyFormData.append("voter_id", vid);
    bodyFormData.append("gender", gender);

    //console.log(reqBody);
    axios
      .post("https://transfinitte-api.selvakarthik.me/", bodyFormData)
      .then((response) => {
        console.log(response.data);
      })
      .catch((err) => {
        console.log(err);
      });

    alert("Finding election records for you...");
  };

  return (
    <div>
      <form
        className='flex flex-col items-center justify-center m-2'
        onSubmit={handleSubmit}
      >
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for='name'>Enter your name:</label>
          <input
            required
            name='name'
            type='text'
            placeholder='Enter name'
            className='ml-4 p-2 border border-3 rounded-md'
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for='fatherName'>Enter your Father's name:</label>
          <input
            required
            name='fatherName'
            type='text'
            placeholder="Enter father's name"
            className='ml-4 p-2 border  border-3 rounded-md'
            onChange={(e) => setFatherName(e.target.value)}
          />
        </div>
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for=''>Enter your state:</label>
          <select
            className='p-2 ml-4 border border-1 w-2/5'
            onChange={(e) => setState(e.target.value)}
          >
            <option disabled selected value>
              Select state
            </option>
            {states.map((state) => {
              return <option value={state}>{state}</option>;
            })}
          </select>
        </div>{" "}
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for='age'>Enter your age:</label>
          <input
            required
            type='number'
            min={18}
            className='p-2 border ml-4  border-3 rounded-md'
            onChange={(e) => setAge(e.target.value)}
          />
        </div>
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for=''>Enter your voter ID:</label>
          <input
            name='voterId'
            type='text'
            placeholder='Enter voter ID'
            className='p-2 ml-4 border  border-3 rounded-md'
            onSelect={(e) => setVid(e.target.value)}
          />
        </div>
        <div className='w-2/5 m-2 flex justify-between items-center'>
          <label for='gender'>Enter your gender:</label>
          <select
            className='ml-4 p-2 border border-1 w-1/5'
            onChange={(e) => setGender(e.target.value)}
          >
            <option disabled selected value>
              Select gender
            </option>
            <option value='M'>male</option>
            <option value='F'>female</option>
          </select>
        </div>
        <div>
          <input
            type='submit'
            value='Submfeit'
            className='py-3 px-4 rounded-md bg-blue-500 text-gray-50 hover:bg-blue-700'
          />
          <input
            type='button'
            value=' Get all family Trees'
            className='py-3 px-4 rounded-md bg-blue-500 text-gray-50 hover:bg-blue-700'
          />
        </div>
      </form>
    </div>
  );
}
