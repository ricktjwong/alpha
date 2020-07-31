import React from 'react';

const Weights = (props) => {
  const updateWeights = (k) => (e) => {
    let newWeights = Object.assign({}, props.weights);
    newWeights[k] = e.target.value;
    props.setWeights(newWeights);
  };
  const renderWeights = () => {
    const inputComponent = [];
    Object.keys(props.weights).forEach((k, idx) => {
      inputComponent.push(
        <div>
          {k}:
          <input
            type={'text'}
            key={idx}
            value={props.weights[k]}
            onChange={updateWeights(k)}
          />
          <br />
        </div>,
      );
    });
    return inputComponent;
  };
  return renderWeights();
};

export default Weights;
