import React, { useState } from 'react';
import styled from 'styled-components';

const Styled = {
    InputGrid: styled.div`
        display: grid;
        grid-gap: 0.5rem;
        grid-template-rows: repeat(3, 1fr);
    `,
    
    Input: styled.input`
        width: 25rem;
        height: 4rem;
        border: solid 0.1rem;
        padding: 1rem;
        border-radius: 0.5rem;
    `,

    Button: styled.button`
        width: 25rem;
        height: 1rem;
        padding: 1.5rem;
        text-align: center;
        border-radius: 0.5rem;
        font: ${({ theme }) => theme.font.button};
            
    `,
};

function SignForm() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleChange = e => {
        console.log(e.target.value)
        if (e.target.name === 'email') {
            setEmail(e.target.value);
        } else if (e.target.name === 'password') {
            setPassword(e.target.value);
        } else {}
    }

    return (
        <>
            <Styled.InputGrid>
                <Styled.Input 
                    placeholder="email"
                    type="text"
                    name="email"
                    onChange={handleChange} 
                />
                <Styled.Input 
                    placeholder="password"
                    type="text"
                    name="password"
                    onChange={handleChange} 
                />
                <Styled.Button>Submit</Styled.Button>
            </Styled.InputGrid>
        </>
    )
}

export default SignForm;