// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;



// import React from 'react';
// import Counter from './component/props';

// function App() {
//   return (
//     <div>
//     <center><Counter/></center>
//     </div>
//   );
// }

// export default App;
import React from 'react';
import Counter from './component/counter';
import Login from './component/login';


function welcome(){
  alert("welcome to training");
}


function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

function App() {
  return (
    <center><div>
      <Greeting name="pooja" />
      {/* <Greeting name="bantu" />
      <Greeting name="pintu" /> */}
      <button onClick={welcome}>click me!</button>
      <Counter/>
      <Login/>
    </div>
    </center>
  );
}

export default App;


