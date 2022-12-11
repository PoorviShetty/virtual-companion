import Journal from "./components/Journal";
import Options from "./components/Options";
import Questionnaire from "./components/Questionnaire";

async function getResponse(text) {
  const url = `http://localhost:5000/${text}`;
  const response = await fetch(url).then((res) => res.json());
  return response;
}

const API = {
  GetChatbotResponse: async (message) => {
    return new Promise(function (resolve, reject) {
      setTimeout(async function () {
        let response = await getResponse(message);
        if (message === "hi") resolve("Welcome to chatbot!");
        else if (message === "journal") resolve(<Journal />);
        else if (message === "options")
          resolve(<Options choices={["Option 1", "Option 2"]} />);
        else if (message === "quiz")
          resolve(
            <Questionnaire
              questions={{
                "Question 1": ["A", "B"],
                "Question 2": ["1", "2", "3"],
              }}
            />
          );
        else resolve(response.message);
      }, 2000);
    });
  },
};

export default API;
