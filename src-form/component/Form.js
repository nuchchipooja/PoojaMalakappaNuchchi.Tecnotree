import React, { useState } from 'react';

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const[CollegeName] =useState('');
  const [isAgreed, setIsAgreed] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Age:', age);
    console.log('Gender:', gender);
    console.log('CollegeName:',CollegeName);
    console.log('Agreed:', isAgreed);
  };

  return (
    <center>
    <form onSubmit={handleSubmit}>
        <h1>Student Registration Form</h1>
      <label>
        Name:
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label><br></br>
      <label>
        Email:
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </label><br></br>
      <label>
        Age:
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} />
      </label><br></br>
      <label className='gender'>
        Gender:
        <select value={gender} checked={isAgreed} onChange={(e) => setGender(e.target.value)}> 
        
           <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option> 
        </select>
      </label><br></br>
      <label>
        CollegeName:
        <input type="text" value={CollegeName} onChange={(e) => setName(e.target.value)} />
      </label><br></br>
      <label>
        <h3>Once the form is submited you cannot change</h3>
        <input type="checkbox" checked={isAgreed} onChange={(e) => setIsAgreed(e.target.checked)} />
        I agree to the terms and conditions
      </label><br></br>
      <button type="submit">Submit</button>
    </form>
    </center>
  );
}

export default App;