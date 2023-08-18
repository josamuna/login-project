import React, {useState,useEffect} from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const url_get = "http://127.0.0.1:8000/api/loginsystem";
  
  // Fetch data from Django api using his url 
  const fetchDataFromApi = async(url_get)=>{
    try{
      const response = await fetch(url_get);
      const valueResponse = await response.json();
      console.log("Response is ", valueResponse);
      const data = valueResponse;
      setData(data);
      console.log("=============>>>", data[0].fullname);
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
        <div>
        {data.map(item=>{
            <div key={item.id}>              
              <h1>{item.fullname}</h1>
              <p>{item.username}</p>
              <p>{item.email}</p>
              <p>{item.password}</p>
            </div>
          })}
        </div>
        
      </header>
    </div>
  );
}

export default App;
