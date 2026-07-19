import React from "react";
import NutrientPage from "../components/NutrientPage";

const Fats = () => {
  return (
    <NutrientPage
      title="Fats"
      description="Healthy fats are vital for hormone production, nutrient absorption, brain function, and providing cellular energy."
      categoryKey="fat"
      unit="g"
    />
  );
};

export default Fats;