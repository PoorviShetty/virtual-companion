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
        if (message === "hi")
          resolve("Welcome to chatbot! Type 'hello' to get started!");
        else if (message === "hello")
          resolve(
            <Options
              choices={["Get help", "Just chat", "Write a journal entry"]}
            />
          );
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
        else {
          if (response.tone === "negative") {
            resolve([
              "I detect sadness, let me help you!\nAnswer this tiny quiz to let me understand better",
              <hr />,
              <Questionnaire
                questions={{
                  "Question 1": ["A", "B"],
                  "Question 2": ["1", "2", "3"],
                }}
              />,
            ]);
          } else {
            var res = [];

            response.message.forEach(function (entry) {
              res.push(entry);
              res.push(<hr />);
            });

            res.pop();

            resolve(res);
          }
        }
      }, 2000);
    });
  },
};

export default API;
