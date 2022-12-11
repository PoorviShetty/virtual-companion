import React from 'react'
import axios from 'axios'

function Options(choices) {
    function registerChoice(option){
        window.localStorage.setItem("option", option);
        document.getElementById(option).style.background = "#CCCCCC";

        axios.post('http://localhost:5000/option', option, {
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
        <div>
            {choices.choices.map((choice, idx) => (
                <div 
                    className="choice border my-2 p-2 rounded bg-light text-black shadow options-choice" 
                    key={idx} 
                    onClick={() => {registerChoice(choice);}}
                    id={choice}
                >
                    {choice}
                </div>    
            ))}
        </div>
    )
}

export default Options