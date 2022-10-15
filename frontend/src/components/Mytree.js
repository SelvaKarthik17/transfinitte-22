import React, { Component } from 'react';
import FamilyTree from '@balkangraph/familytree.js';

export default class Chart extends Component {

    constructor(props) {
        super(props);
        this.divRef = React.createRef();
    }

    shouldComponentUpdate() {
        return false;
    }

    componentDidMount() {
        this.family = new FamilyTree (this.divRef.current , {
            nodes: this.props.nodes,
            editForm: {
                buttons:  {
                    edit: null,
                    share: null,
                    pdf: null,
        
                }
            },       
            nodeBinding: {
                field_0: 'name'
            },
            elements: [
                { type: 'textbox', label: 'Name', binding: 'Name'},
            ]
        });
    }

    render() {
        return (
            <div id="tree" ref={this.divRef}></div>
        );
    }
}
