import React from "react";
//import GetFamily from "../pages/GetFamily";
import Tree from "../pages/Tree";
import axios from "axios";
const Body = () => {
  const [states, setStates] = React.useState(["Tamil Nadu"]);
  const [name, setName] = React.useState("");
  const [fatherName, setFatherName] = React.useState("");
  const [state, setState] = React.useState("");
  const [age, setAge] = React.useState("");
  const [vid, setVid] = React.useState("");
  const [gender, setGender] = React.useState("");

  const [famData, setFamData] = React.useState([]);

  const handleAllSubmit = (e) => {
    var bodyFormData = new FormData();
    bodyFormData.append("name", name);
    bodyFormData.append("relation_name", fatherName);
    bodyFormData.append("state", state);
    bodyFormData.append("age", age);
    bodyFormData.append("voter_id", vid);
    bodyFormData.append("gender", gender);

    //console.log(reqBody);
    axios
      .post(
        "https://transfinitte-api.selvakarthik.me/getAllPartFamilies",
        bodyFormData
      )
      .then((response) => {
        console.log(response.data);
        setFamData(response.data);
      })
      .catch((err) => {
        console.log(err);
      });

    alert("Finding election records for you...");
  };

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
        setFamData(response.data);
      })
      .catch((err) => {
        console.log(err);
      });

    alert("Finding election records for you...");
  };

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
    console.log(famData);
    downloadFile({
      data: JSON.stringify(famData),
      fileName: "answer.json",
      fileType: "text/json",
    });
  };

  return (
    <div className='w-full'>
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
              className='ml-4 p-2 border border-1 w-2/5'
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
              value='Submit'
              className='py-3 px-4 rounded-md m-2 bg-blue-500 text-gray-50 hover:bg-blue-700'
            />
            <input
              type='button'
              value=' Get all family Trees'
              className='py-3 px-4 rounded-md m-2 bg-blue-500 text-gray-50 hover:bg-blue-700'
              onClick={handleAllSubmit}
            />
          </div>
        </form>
      </div>
      <div className='actionBtns'>
        <button
          type='button'
          className='mt-5 py-2 px-4 rounded-md bg-green-500 text-gray-50 hover:bg-green-700'
          onClick={exportToJson}
        >
          Export to JSON
        </button>
      </div>
      {famData && famData.length > 500 ? (
        <>
          <Tree familyData={famData.slice(0, 20)} />
        </>
      ) : (
        <>
          <Tree familyData={famData} />
        </>
      )}
      {/* <Tree familyData={famData} /> */}
    </div>
  );
};

export default Body;
