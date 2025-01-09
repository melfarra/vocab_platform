import React from "react";

const WordCard = ({ word, details }) => {
  return (
    <div
      style={{
        marginTop: "20px",
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "10px",
        backgroundColor: "#f9f9f9",
      }}
    >
      <h2>{word}</h2>
      <pre>{details}</pre>
    </div>
  );
};

export default WordCard;
