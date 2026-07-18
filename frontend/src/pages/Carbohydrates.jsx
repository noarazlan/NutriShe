import React from "react";
import NutrientPage from "../components/NutrientPage";

const Carbohydrates = () => {
  return (
    <NutrientPage
      title="Carbohydrates"
      description="Carbohydrates are your body's primary energy source, fueling your daily activities, workouts, and brain function."
      categoryKey="carbohydrates"
      unit="g"
    />
  );
};

export default Carbohydrates;
