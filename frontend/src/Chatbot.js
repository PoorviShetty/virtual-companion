import React, { useState, useEffect } from "react";

import BotMessage from "./components/BotMessage";
import UserMessage from "./components/UserMessage";
import Messages from "./components/Messages";
import Input from "./components/Input";

import API from "./ChatbotAPI";

import "./styles.css";
import Header from "./components/Header";

function Chatbot() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    async function loadWelcomeMessage() {
      setMessages([
        <BotMessage
          key="0"
          fetchMessage={async () => await API.GetChatbotResponse("hi")}
        />,
      ]);
    }
    loadWelcomeMessage();
  }, []);

  const send = async (text) => {
    localStorage.clear();
    const newMessages = messages.concat(
      <UserMessage key={messages.length + 1} text={text} />,
      <BotMessage
        key={messages.length + 2}
        fetchMessage={async () => await API.GetChatbotResponse(text)}
      />
    );
    setMessages(newMessages);
  };

  window.addEventListener("storage", () => {
    function removeLocal() {
      return new Promise(function (resolve) {
        localStorage.clear();
      });
    }

    if (
      localStorage.hasOwnProperty("action") &&
      !(
        localStorage.hasOwnProperty("questionnaire") ||
        localStorage.hasOwnProperty("journal")
      )
    ) {
      function addNew() {
        return new Promise(function (resolve) {
          const newMessages = messages.concat(
            <BotMessage
              key={messages.length + 1}
              fetchMessage={async () =>
                await API.GetChatbotResponse(localStorage["action"])
              }
            />
          );
          setMessages(newMessages);
        });
      }
      addNew().then(removeLocal);
    } else {
      // use promises or something idk, why is questionnaire TRUE OMG
      let message = "";
      if (localStorage.hasOwnProperty("option")) {
        message =
          "'" + localStorage["option"] + "' option chosen successfully!";
      }

      if (localStorage.hasOwnProperty("journal")) {
        message = "Thank you for journalling!";
      }

      if (localStorage.hasOwnProperty("questionnaire")) {
        message = "Thank you for answering!";
      }

      const newMessages = messages.concat(
        <BotMessage key={messages.length + 1} fetchMessage={() => message} />
      );
      setMessages(newMessages);
      //localStorage.clear();
    }
  });

  return (
    <div className="chatbot">
      <Header />
      <Messages messages={messages} />
      <Input onSend={send} />
    </div>
  );
}

export default Chatbot;
