import React from "react";

export default function UserMessage({ text }) {
  return (
    <div className="message-container">
      <div className="user-message shadow">{text}</div>
    </div>
  );
}
