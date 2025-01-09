import React, { useState } from "react";
import api from "../utils/api";
import SubjectButtons from "../components/SubjectButtons";
import WordCard from "../components/WordCard";

const HomePage = () => {
  const [wordData, setWordData] = useState(null); // State for the generated word
  const [loading, setLoading] = useState(false); // State for loading status

  const handleSubjectClick = async (subject) => {
    setLoading(true); // Show loading spinner
    try {
      const response = await api.get(`/random?subject=${subject}`);
      setWordData(response.data); // Update word data
    } catch (error) {
      console.error("Error fetching word:", error);
    } finally {
      setLoading(false); // Hide loading spinner
    }
  };

  return (
    <div>
      <h1>Vocabulary Builder</h1>
      <SubjectButtons onSubjectClick={handleSubjectClick} />
      {loading && <p>Loading...</p>}
      {wordData && <WordCard word={wordData.word} details={wordData.details} />}
    </div>
  );
};

export default HomePage;
