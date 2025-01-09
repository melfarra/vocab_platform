import React from "react";

const subjects = ["random", "math", "science", "history", "literature"];

const SubjectButtons = ({ onSubjectClick }) => {
  return (
    <div style={{ margin: "20px 0" }}>
      {subjects.map((subject) => (
        <button
          key={subject}
          onClick={() => onSubjectClick(subject)}
          style={{
            margin: "5px",
            padding: "10px 20px",
            backgroundColor: "#007bff",
            color: "#fff",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          {subject === "random" ? "Generate Random Word" : subject}
        </button>
      ))}
    </div>
  );
};

export default SubjectButtons;
