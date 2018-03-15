import React, { Component } from 'react';



     
    class Cmplist extends Component {
        constructor() {
            super();
            this.state = { 
              data: [],
             };
        }
        
        componentDidMount() {
            fetch('http://slide58.pythonanywhere.com/api/campaigns/')
            .then(response => response.json())
            .then(data => this.setState({ data: data }));
               
        }
        
        render() {        
            return(
                <div>
                    <div><b>Мои Кампании</b>:</div>
                    { this.state.data.map(item=> { return <div>{item.name} <a href = {'http://slide58.pythonanywhere.com/yandex/keywords/'+item.directId+'/'}>Обновить ключевики с директа №{item.directId}</a></div>}) }          
                </div>  
            );
        }
    }


export default Cmplist;