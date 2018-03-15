import React, { Component } from 'react';



     
    class Kwdlist extends Component {
        constructor() {
            super();
            this.state = { 
              data: [],
             };
        }
        
        componentDidMount() {
            fetch('http://slide58.pythonanywhere.com/api/keywords/')
            .then(response => response.json())
            .then(data => this.setState({ data: data }));
               
        }
        
        render() {        
            return(
                <div>
                    <div><b>Ключевики</b>:</div>
                    { this.state.data.map(item=> { return <div>{item.keyword}</div>}) }          
                </div>  
            );
        }
    }


export default Kwdlist;