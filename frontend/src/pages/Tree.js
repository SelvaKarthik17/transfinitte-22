import React, { Component } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import FamilyTree from "../components/Mytree";

export default class Tree extends Component {
  render() {
    return (
      <div className=' w-1/2 border border-1 my-4 mx-auto'>
        <FamilyTree
          nodes={[
            { id: 0, name: "Divyanathan", pids: [1, 2], gender: "male" },
            { id: 1, name: "Meenarosari", pids: [0], gender: "female" },
            { id: 2, name: "Caroline", pids: [0], gender: "female" },
          ]}
        />
      </div>
    );
  }
}
