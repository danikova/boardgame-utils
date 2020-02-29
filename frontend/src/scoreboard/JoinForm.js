import React from 'react';
import { useFormik } from 'formik';
import { TextField, Button, makeStyles } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    mb: {
        'margin-bottom': '2rem',
    },
}));

export function JoinForm(props) {
    const classes = useStyles();
    const fromik = useFormik({
        initialValues: { groupId: '', name: '' },
        validate: values => {
            const errors = {};
            if (!values.groupId) {
                errors.groupId = 'Required';
            } else if (!RegExp('\\d{6}').test(values.groupId)) {
                errors.groupId = 'Group ID should have exactle 6 digits';
            }
            if (!values.name) {
                errors.name = 'Required';
            } else if (values.name.length < 3) {
                errors.name = 'Name should have at least 3 characters';
            }
            return errors;
        },
        onSubmit: values => {
            fetch(
                `http://localhost:8080/scoreboard/check-name/?groupId=${values.groupId};name=${values.name}`,
                {
                    mode: 'cors'
                },
            ).then(res => {
                console.log(res.status);
            });
            // props.setFormData(values);
        },
    });

    return (
        <form noValidate autoComplete='off' onSubmit={fromik.handleSubmit}>
            <div>
                <TextField
                    className={classes.mb}
                    id='groupId'
                    label='Group ID'
                    variant='outlined'
                    onChange={fromik.handleChange}
                    value={fromik.values.groupId}
                    helperText={fromik.errors.groupId}
                    error={!fromik.errors.groupId ? false : true}
                />
            </div>
            <div>
                <TextField
                    className={classes.mb}
                    id='name'
                    label='Visible Name'
                    variant='outlined'
                    onChange={fromik.handleChange}
                    value={fromik.values.name}
                    helperText={fromik.errors.name}
                    error={!fromik.errors.name ? false : true}
                />
            </div>
            <div>
                <Button variant='contained' color='primary' type='submit'>
                    Join Group
                </Button>
            </div>
        </form>
    );
}
