import React from 'react'
import axios from 'axios'


function Options(choices) {
    function registerChoice(option){
        window.localStorage.setItem("option", option);
        for (const i of choices.choices){
            if (i == option){
                document.getElementById(i).style.backgroundColor = "#CCCCCC";
            }else{
                document.getElementById(i).style.backgroundColor = "white";
            }
        }

        axios.post('http://localhost:5000/option', option, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response){
            if (response.data.action){
                window.localStorage.setItem("action", response.data.action);
                window.dispatchEvent(new Event("storage"));
            }
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
                    className="choice border my-2 p-2 rounded text-black shadow options-choice" 
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