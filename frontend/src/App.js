import React, { Component } from 'react';



     
    class App extends Component {
        constructor() {
            super();
            this.state = { 
              data: [],
             };
        }
        
        componentDidMount() {
          /*fetch('http://localhost:8000/api/campaigns/')
          .then((response)=>response.json())
          .then((findresponse)=>
          {
            console.log(findresponse)
          })*/
          //.then(data=>console.log(data));
            fetch('http://localhost:8000/api/campaigns/') 
            .then(response => response.json())
            .then(data => this.setState({ data: data }));
               
        }
        
        render() {        
            return(
                <div>
                    <div>Itemsss:</div>
                    { this.state.data.map(item=> { return <div>{item.name}</div>}) }          
                </div>  
            );
        }
    }


export default App;