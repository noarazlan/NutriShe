import React from "react";
import NutrientPage from "../components/NutrientPage";

const Protein = () => {
  return (
    <NutrientPage
      title="Protein"
      description="Protein is essential for building and repairing tissues, supporting immune function, and maintaining lean muscle mass."
      categoryKey="protein"
      unit="g"
    />
  );
};

export default Protein;