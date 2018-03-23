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
                    <table class = 'table'>
                    <tr>
                    	<th>Кампания | </th><th>ID фразы | </th><th>Ключ | </th><th>Ставка</th>
                    </tr>
                    { this.props.kwdList.map(item=> { return <tr><td>{item.campaign}  </td><td>{item.directId}  </td><td>{item.keyword}  </td><td>{item.bid}</td></tr>}) }    
                    </table>      
                </div>  
            );
        }
    }


export default Kwdlist;