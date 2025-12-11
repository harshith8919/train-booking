import React, {useEffect, useState} from 'react';

export default function TrainList(){
  const [trains, setTrains] = useState([]);
  const [seats, setSeats] = useState({});

  useEffect(()=>{
    fetch("http://127.0.0.1:8000/api/trains/")
      .then(r=>r.json())
      .then(setTrains)
      .catch(err=>console.error(err));
  },[]);

  const handleBook = async (trainId) => {
    const s = parseInt(seats[trainId] || "1", 10);
    if (!s || s <= 0) return alert("Enter positive seat count");
    try {
      const resp = await fetch(`http://127.0.0.1:8000/api/trains/${trainId}/book/`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({seats: s})
      });
      const data = await resp.json();
      if (!resp.ok) {
        alert(data.error || "Booking failed");
      } else {
        alert(`${data.message}. Total with GST: ₹${data.total_with_gst}`);
        const r = await fetch("http://127.0.0.1:8000/api/trains/");
        setTrains(await r.json());
      }
    } catch(e){
      console.error(e);
      alert("Network error");
    }
  };

  return (
    <div>
      <h2>Trains</h2>
      <ul style={{listStyle:'none', padding:0}}>
        {trains.map(tr=>(
          <li key={tr.id} style={{marginBottom:12, border:'1px solid #ddd', padding:12, borderRadius:6}}>
            <div style={{fontSize:18, fontWeight:600}}>{tr.name}</div>
            <div>Fare: ₹{tr.fare} — Available: {tr.available_seats}</div>
            <div style={{marginTop:8}}>
              <input type="number" min="1" value={seats[tr.id]||""}
                     onChange={e=>setSeats({...seats, [tr.id]: e.target.value})}
                     placeholder="seats" style={{width:80, marginRight:8}} />
              <button onClick={()=>handleBook(tr.id)}>Book</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
