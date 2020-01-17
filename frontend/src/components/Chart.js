import React from "react";
import { Bar, Line, Pie } from "react-chartjs-2";

const Chart = props => {
  const { chartData } = props;
  return (
    <div>
      <Pie
        data={chartData}
        options={{
          title: {
            display: "Students",
            text: "Existing Skills",
            fontSize: 25
          }
        }}
      />
    </div>
  );
};

export default Chart;
