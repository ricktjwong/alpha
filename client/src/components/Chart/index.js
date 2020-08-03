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
    const filtered = data.filter(
      (d) => d.x >= zoomedXDomain[0] && d.x <= zoomedXDomain[1],
    );
    if (filtered.length > maxPoints) {
      const k = Math.ceil(filtered.length / maxPoints);
      return filtered.filter((d, i) => i % k === 0);
    }
    return filtered;
  };

  const getZoomFactor = () => {
    const factor = 10 / (zoomedXDomain[1] - zoomedXDomain[0]);
    return _.round(factor, factor < 3 ? 1 : 0);
  };

  const renderedData = getData();
  if (zoomedXDomain.length == 0) {
    return null;
  } else {
    return (
      <div>
        <VictoryChart
          domain={props.entireDomain}
          containerComponent={
            <VictoryZoomContainer
              zoomDimension="x"
              onZoomDomainChange={onDomainChange}
              minimumZoom={{ x: 1 / 10000 }}
            />
          }>
          <VictoryLine data={renderedData} style={style.chart} />
        </VictoryChart>
        <div>
          {getZoomFactor()}x zoom; rendering {renderedData.length} of{' '}
          {props.data.length}
        </div>
      </div>
    );
  }
};

const style = {
  chart: {
    data: { stroke: 'tomato' },
  },
};

export default Chart;
