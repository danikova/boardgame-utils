import React from 'react';
import { Button, makeStyles } from "@material-ui/core";


const useStyles = makeStyles(theme => ({
  button: {
    'margin-right': '2rem',
    'margin-bottom': '2rem',
  }
}));


export function Selector(props) {
  const classes = useStyles();

  return (
    <div>
      <div>
        <Button className={classes.button} variant="contained" color="primary" href="/scoreboard/new">Create New Scoreboard</Button>
        <Button className={classes.button} variant="contained" color="primary" href="/scoreboard/join">Join Scoreboard</Button>
      </div>
      <div>
        <Button variant="contained" disabled color="primary" href="/">More coming soon</Button>
      </div>
    </div>
  );
}