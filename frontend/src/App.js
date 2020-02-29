import React from "react"
import { Selector } from './util-selector/Selector';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Container, Grid, makeStyles } from "@material-ui/core";
import { ScoreboardRouter } from "./scoreboard/ScoreboardRouter";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    padding: '4rem 0',
  }
}));


function getRouter(props) {
  return (
    <Router>
      <Route exact path="/">
        <Selector></Selector>
      </Route>
      <Route path="/scoreboard/:board_action">
        <ScoreboardRouter></ScoreboardRouter>
      </Route>
    </Router>
  );
}

export function App(props) {
  const classes = useStyles();

  return (
    <Container maxWidth="md">
      <Grid container className={classes.root} spacing={2}>
        <Grid item xs={12}>
          <Grid container justify="center" >
            {getRouter()}
          </Grid>
        </Grid>
      </Grid>
    </Container>
  );
}