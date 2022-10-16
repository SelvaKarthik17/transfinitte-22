import React, { Component } from "react";
import FamilyTree from "@balkangraph/familytree.js";

export default class FamilyTreeClass extends Component {
  constructor(props) {
    super(props);
    this.divRef = React.createRef();
  }

  shouldComponentUpdate() {
    return true;
    // return false;
  }

  componentDidMount() {
    this.family = new FamilyTree(this.divRef.current, {
      nodes: this.props.nodes,
      editForm: {
        buttons: {
          edit: null,
          share: null,
          pdf: null,
        },
      },
      menu: {
        pdf: { text: "Export PDF" },
        png: { text: "Export PNG" },
        svg: { text: "Export SVG" },
        csv: { text: "Export CSV" },
        json: { text: "Export JSON" },
      },
      nodeMenu: {
        pdf: { text: "Export PDF" },
        png: { text: "Export PNG" },
        svg: { text: "Export SVG" },
      },
      nodeBinding: {
        field_0: "name",
      },
      elements: [{ type: "textbox", label: "Name", binding: "Name" }],
    });
  }

  componentDidUpdate() {
    this.family = new FamilyTree(this.divRef.current, {
      nodes: this.props.nodes,
      editForm: {
        buttons: {
          edit: null,
          share: null,
          pdf: null,
        },
      },
      menu: {
        pdf: { text: "Export PDF" },
        png: { text: "Export PNG" },
        svg: { text: "Export SVG" },
        csv: { text: "Export CSV" },
        json: { text: "Export JSON" },
      },
      nodeMenu: {
        pdf: { text: "Export PDF" },
        png: { text: "Export PNG" },
        svg: { text: "Export SVG" },
      },
      nodeBinding: {
        field_0: "name",
      },
      elements: [{ type: "textbox", label: "Name", binding: "Name" }],
    });
  }

  render() {
    return <div id='tree' key={this.props.nodes} ref={this.divRef}></div>;
  }
}
