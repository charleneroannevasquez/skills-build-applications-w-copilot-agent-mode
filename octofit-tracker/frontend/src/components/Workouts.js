import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [data, setData] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Workouts API endpoint:', endpoint);
        console.log('Fetched data:', json);
        setData(json.results || json);
      });
  }, [endpoint]);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {Array.isArray(data) && data.map((item, idx) => (
          <li key={item.id || idx}>{item.name || JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
