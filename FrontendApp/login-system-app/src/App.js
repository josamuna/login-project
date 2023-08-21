import React, { useState, useEffect } from 'react';
import  Axios from 'axios';
import './App.css';
import {Table} from 'reactstrap';
import {NotificationContainer, NotificationManager} from 'react-notifications'

function App() {
  const [userData, setUserData] = useState([]);
  const url_get = "http://127.0.0.1:8000/api/loginsystem/";
  
  // Fetch data from Django api using an expected url 
  const fetchDataFromApi = async(url_get)=>{
    try{
      const response = await Axios.get(url_get);
      console.log('Response is :', response.data);
      setUserData(response.data);
    }catch(error){
      console.log(`Something went wrong:${ error }`);
      NotificationManager.warning('Failed to load data!', 'Loading Data', 6000);
    }    
  }

  useEffect(() =>{
    fetchDataFromApi(url_get)
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <Table>
            <thead>
              <tr>
                <th>User ID</th>
                <th>Fullname</th>
                <th>Email</th>
                <th>Password</th>
              </tr>
            </thead>
            {userData.map((item)=>{
              return(
                <tbody key={item.id}>
                    <tr key={item.id}>
                      <td>{item.id}</td>
                      <td>{item.fullname}</td>
                      <td>{item.email}</td>
                      <td>{item.password}</td>
                    </tr>
                </tbody>
              )
            })}
          </Table>
        </div> 
        <NotificationContainer />       
      </header>
    </div>
  );
}

export default App;