import React, {useState} from 'react'
import axios from 'axios'

function Journal() {
    const [entry, setEntry] = useState("")
    const [mood, setMood] = useState("Neutral")
    const saveEntry = (event) => {
        event.preventDefault();
        document.getElementById("journal-box").disabled = true; 
        document.getElementById("journal-box").style.background = "#00AAA5";
        document.getElementById("journal-box").style.border = "none";
        document.getElementById("journal-box").style.outline = "none";
        document.getElementById("journal-box").style.color = "white";
        document.getElementById("journal-button").style.display = "none"; 
        window.localStorage.setItem("journal", "true");
        setEntry(entry);
        axios.post('http://localhost:5000/journal', {entry, mood}, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response){
            //console.log(response);
        })
        .catch(function(error){
            //console.log(error);
        });
        window.dispatchEvent(new Event("storage"));
        return;
    }
    return (
        <form method="post" onSubmit={saveEntry}>
            <textarea className="form-control" value={entry} onChange={(e) => setEntry(e.target.value)} id="journal-box"/>
            <br />
            <select className="form-control" id="mood" onChange={(e) => setMood(e.target.value)} value={mood}>
                <option value="Neutral">Neutral</option>
                <option value="Positive">Positive</option>
                <option value="Negative">Negative</option>
            </select>
            <br />
            <button className="btn btn-light" type="submit" id="journal-button">
            Add entry
            </button>
        </form>
    )
}

export default Journal