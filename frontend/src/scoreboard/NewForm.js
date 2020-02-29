import React from 'react';
import { useFormik } from 'formik';
import { TextField, Button, makeStyles } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    mb: {
        'margin-bottom': '2rem',
    },
}));

export function NewForm(props) {
    const classes = useStyles();
    const fromik = useFormik({
        initialValues: { groupId: '', name: '' },
        validate: values => {
            const errors = {};
            if (!values.name) {
                errors.name = 'Required';
            } else if (values.name.length < 3) {
                errors.name = 'Name should have at least 3 characters';
            }
            return errors;
        },
        onSubmit: values => {
            const random_group_id = Math.floor(Math.random() * Math.floor(1000000));
            values.groupId = random_group_id;
            props.setFormData(values);
        },
    });

    return (
        <form noValidate autoComplete='off' onSubmit={fromik.handleSubmit}>
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
                    Create New Group
                </Button>
            </div>
        </form>
    );
}
