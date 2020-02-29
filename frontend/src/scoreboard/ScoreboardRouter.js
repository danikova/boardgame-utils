import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { JoinForm } from './JoinForm';
import { Scoreboard } from './Scoreboard';
import { NewForm } from './NewForm';

export function ScoreboardRouter() {
    const { board_action } = useParams();
    if (board_action === 'join') return <JoinScoreboard></JoinScoreboard>;
    else return <NewScoreboard></NewScoreboard>;
}

function JoinScoreboard() {
    const [formData, setFormData] = useState(null);

    return formData ? (
        <Scoreboard formData={formData}></Scoreboard>
    ) : (
        <JoinForm setFormData={setFormData}></JoinForm>
    );
}

function NewScoreboard() {
    const [formData, setFormData] = useState(null);

    return formData ? (
        <Scoreboard formData={formData}></Scoreboard>
    ) : (
        <NewForm setFormData={setFormData}></NewForm>
    );
}
