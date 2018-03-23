import React, { Component } from 'react';



     
    class Kwdlist extends Component {
        constructor() {
            super();
            this.state = { 
              data: [],
             };
        }
        
        componentDidMount() {
            //this.fetchData();
               
        }

        fetchData = () => {
        	var urladdress = 'http://slide58.pythonanywhere.com/api/keywords/';
            fetch(urladdress)
            .then(response => response.json())
            .then(data => this.setState({ data: data }));
               

        }
        
        render() {        
            return(
                <div>
                    <div><b>Ключевики для компании №: </b> { this.props.cmpId}:</div>
                    { this.props.kwdList.map(item=> { return <div>{item.keyword}</div>}) }          
                </div>  
            );
        }
    }


export default Kwdlist;