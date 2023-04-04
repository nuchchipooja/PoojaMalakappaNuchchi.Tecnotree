import React, { useState} from "react";

function Counter() {

    const [time, setTime] = useState('')
  
    const handleTimeChange = (event) => {
        setTime(event.target.value);
      };



function startCounter(){
    let getTime = document.getElementById("input").value;
let x = setInterval(function() {


  let currentTime = getTime--;

  let minutes = Math.floor(currentTime / 60);
  let seconds = currentTime % 60;

  
  if (seconds < 10) {
    seconds = "0" + seconds;
  }

  document.getElementById("countdown").innerHTML = minutes + ":" + seconds;
  if (currentTime <= 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "Time's up!";
    alert("Done");
  }
}, 1000);
}

  return (
    <center>
    <div className="counter">
      <h1> Enter the Time</h1>
      <p id="countdown"></p>
      <label>
        Set Time:
   </label>
   <input type="text" id='input' value={time} onChange={handleTimeChange} /><br></br>
   <button id='start' onClick={startCounter}>Start</button>
    </div>
    </center>
  );
}

export default Counter;



