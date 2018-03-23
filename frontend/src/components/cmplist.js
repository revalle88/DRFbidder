import React, { Component } from 'react';
import Kwdlist from './kwdlist';



     
    class Cmplist extends Component {
        constructor() {
            super();
            this.state = { 
              data: [],
              cmpId: null,
              kwdList: [],
             };
        }
        
        componentDidMount() {
            this.fetchData();
        }

        fetchData = () => {
            fetch('http://slide58.pythonanywhere.com/api/campaigns/')
            .then(response => response.json())
            .then(data => this.setState({ data: data }));
               

        }

        fetchKwds = (cmpId) => {
            console.log("catch the hoop");
            var urladdress = 'http://slide58.pythonanywhere.com/api/'+cmpId+'/keywords';
            fetch(urladdress)
            .then(response => response.json())
            .then(data => this.setState({ kwdList: data }));
            this.setState({cmpId: cmpId})
               

        }

        setCmpId = (cmpId) => {
        this.setState({ cmpId: cmpId });
        }
        
        render() {        
            return(
                <div>
                    <div><b>Мои Кампании</b>:</div>
                    
                    { this.state.data.map(item=> { return <div>{item.name} <button onClick={() => {this.fetchKwds(item.directId)}}>показать ключи</button><a href = {'http://slide58.pythonanywhere.com/yandex/keywords/'+item.directId+'/'}>Обновить ключевики с директа №{item.directId}</a></div>}) }          
                    <Kwdlist kwdList = {this.state.kwdList} cmpId = {this.state.cmpId}/>
                </div>  
            );
        }
    }


export default Cmplist;