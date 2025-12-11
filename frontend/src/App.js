import React from 'react';
import TrainList from './components/TrainList';

function App(){
  return (
    <div style={{padding:20, fontFamily:'Arial, sans-serif'}}>
      <h1>Train Booking</h1>
      <TrainList />
    </div>
  );
}

export default App;
