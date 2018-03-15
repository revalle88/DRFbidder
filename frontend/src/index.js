import React from 'react';
import ReactDOM from 'react-dom';

//COMPONENTS
import Header from './components/header';
import Cmplist from './components/cmplist';
import Kwdlist from './components/kwdlist';
import Yandex from './components/yandexctrls';


const App = () =>{
	return (
	<div>
		<div>
			<Header/>
		</div><br/>
		<div>
			<Cmplist/>
		</div>
		<div>
			<Yandex/>
		</div><br/>
		<div>
			<Kwdlist/>
		</div>
		
	</div>
	)
}

ReactDOM.render(<App/>,document.querySelector('#root'));