import React from 'react';
import ReactDOM from 'react-dom';

//COMPONENTS
import Header from './components/header';
import Cmplist from './components/cmplist';
import Kwdlist from './components/kwdlist';
import Yandex from './components/yandexctrls';

import 'bootstrap/dist/css/bootstrap.min.css';


const App = () =>{
	return (
	<div class = 'container'>
		<div>
			<Header/>
		</div><br/>
		<div>
			<Cmplist/>
		</div>
		<br/>
		<div>
			<Yandex/>
		</div><br/>
		
		
	</div>
	)
}

ReactDOM.render(<App/>,document.querySelector('#root'));