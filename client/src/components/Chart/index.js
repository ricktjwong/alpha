import React, { useState } from 'react';
import _ from 'lodash';
import { VictoryChart, VictoryLine, VictoryZoomContainer } from 'victory';

const Chart = (props) => {
  const [zoomedXDomain, setZoomedXDomain] = useState(props.entireDomain.x);

  const onDomainChange = (domain) => {
    setZoomedXDomain(domain.x);
  };

  const getData = () => {
    const { data, maxPoints } = props;
    // Get data within the bounds of the new x axis domain
    const filtered = data.filter(
      (d) => d.x >= zoomedXDomain[0] && d.x <= zoomedXDomain[1],
    );
    // If filtered data within bounds is greater than maxPoints,
    // reduce the number of points allowed by a multiple equal
    // to filtered length / maxPoints
    if (filtered.length > maxPoints) {
      const k = Math.ceil(filtered.length / maxPoints);
      return filtered.filter((d, i) => i % k === 0);
    }
    return filtered;
  };

  const renderedData = getData();
  if (zoomedXDomain.length == 0) {
    return null;
  } else {
    return (
      <VictoryChart
        domain={props.entireDomain}
        containerComponent={
          <VictoryZoomContainer
            zoomDimension="x"
            onZoomDomainChange={onDomainChange}
          />
        }>
        <VictoryLine data={renderedData} style={style.chart} />
      </VictoryChart>
    );
  }
};

const style = {
  chart: {
    data: { stroke: 'tomato' },
  },
};

export default Chart;
