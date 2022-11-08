import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextField from '@mui/material/TextField';

import './App.css';

export default function App() {
  const [typeOfEngagement, setTypeOfEngagement] = React.useState('');
  const [maidenName, setMaidenName] = React.useState('');

  const handleTypeOfEngagement = (event) => {
    setTypeOfEngagement(event.target.value);
  };

  const handleMaidenName = (event) => {
    setMaidenName(event.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Create a DJ Joe Contract.
        </p>
        <Box sx={{ minWidth: 300 }}>
          <FormControl fullWidth>
            <InputLabel id="type-of-engagement">Type Of Engagement</InputLabel>
            <Select
              labelId="type-of-engagement-select-label"
              id="type-of-engagement-select"
              value={typeOfEngagement}
              label="typeOfEngagement"
              onChange={handleTypeOfEngagement}
            >
              <MenuItem value="Wedding Ceremony">Wedding Ceremony</MenuItem>
              <MenuItem value="Wedding Ceremony and Reception">Wedding Ceremony and Reception</MenuItem>
              <MenuItem value="Wedding Reception">Wedding Reception</MenuItem>
              <MenuItem value="School Dance">School Dance</MenuItem>
            </Select>
          </FormControl>
        </Box>
        <Box
          component="form"
          sx={{
            minWidth: 300,
            '& > :not(style)': { m: 1, width: '25ch' },
          }}
          noValidate
          autoComplete="off"
        >
          <FormControl fullWidth>
            <InputLabel id="maiden-name">Maiden Name</InputLabel>
            <TextField id="maiden-name-input" variant="outlined" value={maidenName} onChange={handleMaidenName}/>
          </FormControl>
        </Box>
      </header>
    </div>
  );
}
