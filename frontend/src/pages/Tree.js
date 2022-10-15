import React, { Component } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTree from "../components/Mytree";

export default class Tree extends Component {
  render() {
    return (
      <div className=' w-3/4 border border-1 my-4 mx-auto'>
        <FamilyTree
          nodes={[{'id': 0, 'name': ' Raghunath Singh ', 'pids': [1], 'gender': 'male'}, {'id': 1, 'name': ' Nannubai ', 'pids': [0], 'gender': 'female'}, {'id': 2, 'name': ' Yuvraj ', 'pids': [], 'gender': 'male', 'fid': 0}]}
        />
      </div>
    );
  }
}
