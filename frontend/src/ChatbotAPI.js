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
        else resolve(response.message);
      }, 2000);
    });
  },
};

export default API;
