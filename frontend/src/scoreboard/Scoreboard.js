import React from 'react';
import { HotTable } from '@handsontable/react';
import {
    makeStyles,
    Paper,
    Card,
    CardContent,
    Typography,
} from '@material-ui/core';

const useStyles = makeStyles({
    root: {
        minWidth: 275,
    },
});

export default function SimpleCard({ groupId, name }) {
    const classes = useStyles();

    return (
        <Card className={classes.root}>
            <CardContent>
                <Typography variant='h5' component='h2' gutterBottom>
                    Group details:
                </Typography>
                <Typography color='textSecondary'>
                    id: {groupId.toString().replace(/\B(?=(\d{2})+(?!\d))/g, " ")}
                </Typography>
                <Typography color='textSecondary'>
                    name: {name}
                </Typography>
            </CardContent>
        </Card>
    );
}

export class Scoreboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [
                [10, 11, 12, 13],
                [20, 11, 14, 13],
                [30, 15, 12, 13],
            ],
            headers: ['Ford', 'Volvo', 'Toyota', 'Honda'],
        };
        this.settings = {
            rowHeaders: false,
            colHeaders: true,
            licenseKey: 'non-commercial-and-evaluation',
            columnSummary: [
                {
                    sourceColumn: 0,
                    destinationRow: 0,
                    destinationColumn: 0,
                    reversedRowCoords: true,
                    type: 'sum',
                    forceNumeric: true,
                },
            ],
            stretchH: 'all',
        };
    }

    render() {
        return (
            <div>
                <SimpleCard {...this.props.formData}></SimpleCard>
                <Paper elevation={0}>
                    <HotTable
                        settings={this.settings}
                        data={this.state.data}
                        colHeaders={this.state.headers}
                    />
                </Paper>
            </div>
        );
    }
}
