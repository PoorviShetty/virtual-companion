import React, {useState} from 'react'

function Journal() {
    const [entry, setEntry] = useState("")
    const saveEntry = (event) => {
        event.preventDefault();
        console.log(entry)
    }
    return (
        <form method="post" onSubmit={saveEntry}>
            <textarea className="form-control" value={entry} onChange={(e) => setEntry(e.target.value)}/>
            <br />
            <button className="btn btn-light" type="submit">
            Add entry
            </button>
        </form>
    )
}

export default Journal