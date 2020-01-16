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
            text: "Current Semester",
            fontSize: 25
          }
          //   legend: {
          //     display: this.props.displayLegend,
          //     position: this.props.legendPosition
          //   }
        }}
      />
    </div>
  );
};

export default Chart;
