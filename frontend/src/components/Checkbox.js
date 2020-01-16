import React, { useState, useEffect } from "react";

const Checkbox = props => {
  const { skill, array, setArray, forEditArray } = props;
  const [value, setValue] = useState("");

  const handleChange = e => {
    const selectedName = e.target.name;
    const selectedValue = e.target.value;
    const selectedObject = { selectedName, selectedValue };
    setValue(e.target.value);

    if (array.filter(object => object.selectedName === selectedName)) {
      let filtered = array.filter(function(item) {
        return item.selectedName != selectedObject.selectedName;
      });
      setArray(filtered);
    }
    if (selectedObject.selectedValue != "0") {
      setArray(prevArray => [...prevArray, selectedObject]);
    }
  };

  const getValue = () => {
    if (forEditArray.filter(object => object.selectedName === skill)) {
      forEditArray.filter(object => {
        let parsedSkillObject = object;
        if (skill == parsedSkillObject.selectedName) {
          setValue(parsedSkillObject.selectedValue);
          return;
        }
      });
    } else {
      setValue(0);
    }
  };

  useEffect(() => {
    getValue();
  }, [forEditArray]);

  return (
    <label>
      <input
        type="number"
        min="0"
        max="5"
        name={skill}
        value={value}
        className="input-number"
        onChange={e => handleChange(e)}
      />
      {skill}
    </label>
  );
};

export default Checkbox;
