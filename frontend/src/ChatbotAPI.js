import Journal from "./components/Journal";
import Options from "./components/Options";
import Questionnaire from "./components/Questionnaire";

async function getResponse(text) {
  const url = `http://localhost:5000/${text}`;
  const response = await fetch(url).then((res) => res.json());
  return response;
}

async function getSummary() {
  const url = `http://localhost:5000/summarise`;
  const response = await fetch(url).then((res) => res.json());
  return response;
}

const API = {
  GetChatbotResponse: async (message) => {
    return new Promise(function (resolve, reject) {
      setTimeout(async function () {
        let response = "";
        if (message === "summary") {
          response = await getSummary();
        } else {
          response = await getResponse(message);
        }

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
                  "What is your age?": [
                    "18-24",
                    "25-34",
                    "35-44",
                    "45-54",
                    "55-64",
                    "65-74",
                    "75-84",
                    "85+",
                  ],
                  "Given my current physical condition, I am satisfied with what I can do.":
                    [
                      "Never",
                      "Sometimes",
                      "More than half the days",
                      "All the time",
                    ],
                  "I have confidence in my ability to sustain important relationships.":
                    [
                      "Never",
                      "Sometimes",
                      "More than half the days",
                      "All the time",
                    ],
                  "I feel hopeful about my future.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "I am often interested and excited about things in my life.":
                    [
                      "Never",
                      "Sometimes",
                      "More than half the days",
                      "All the time",
                    ],
                  "I am able to have fun.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "I am generally satisfied with my psychological health.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "I am able to forgive myself for my failures.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "My life is progressing according to my expectations.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "I am able to handle conflict with others.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
                  "I have peace of mind.": [
                    "Never",
                    "Sometimes",
                    "More than half the days",
                    "All the time",
                  ],
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
