import React, { useState } from 'react'
import axios from 'axios'

function Questionnaire(questions) {
    const [answer, setAnswer] = useState([]);

    const idRand = Math.random() * (10000-1) + 1

    function registerAnswer(data){
        for (const i of questions.questions[data[0]]){
            if (i === data[1]){
                document.getElementById(idRand + data[0] + i).style.backgroundColor = "#CCCCCC";
            }else{
                document.getElementById(idRand + data[0] + i).style.backgroundColor = "white";
            }
        }
        setAnswer(answer => [...answer, data])
        return;
    }

    const submitAnswer = (event) => {
        event.preventDefault();
        document.getElementById("submit-button").style.display = "none"; 
        
        answer.reverse()
        let q = []
        let data = []
        for (const i of answer){
            if (!(q.includes(i[0]))){
                q.push(i[0])   
                data.push(i)
            }
        }
        axios.post('http://localhost:5000/questionnaire', data, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response){
            window.localStorage.setItem("questionnaire", response.data.message);
        })
        .catch(function(error){
            //console.log(error);
        });
        window.dispatchEvent(new Event("storage"));
        return;
    }
    return (
        <form method = "post" onSubmit={submitAnswer}>
            {
                Object.entries(questions.questions)
                .map( ([question, value]) => (
                    <div key={question}>
                        <p>{question}</p>
                        <div>
                            {value.map((choice, idx) => (
                                <div 
                                    className="choice border my-2 p-2 rounded  text-black shadow options-choice" 
                                    key={choice} 
                                    onClick={() => {registerAnswer([question, choice]);}}
                                    id={idRand + question + choice}
                                >
                                    {choice}
                                </div>    
                            ))}
                        </div>
                        <hr/>
                    </div>
                ) )
            }
            <button type="submit" className='btn btn-light' id="submit-button">Submit Answers!</button>
        </form>
    )
}

export default Questionnaire