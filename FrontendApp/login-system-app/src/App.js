import React, {useState,useEffect} from 'react';
import './App.css';

function App() {
  const [data, setData] = useState({});
  const url_get = "http://127.0.0.1:8000/api/";
  
  // Fetch data from Django api using his url 
  const fetchDataFromApi = async(url_get)=>{
    try{
      const response = await fetch(url_get);
      const valueResponse = await response.json();
      console.log("Response is ", valueResponse);
      return valueResponse;
    }catch(error){
      console.log(`Something went wrong:${error}`);
    }    
  }

  useEffect(() =>{
    fetchDataFromApi(url_get)
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <p>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
