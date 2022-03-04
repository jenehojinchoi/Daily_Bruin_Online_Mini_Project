import React from 'react';
import styled from 'styled-components';
import { SignForm } from '../components';

const Styled = {
    SignInPage : styled.div`
        display: flex;
        flex-direction: row;
        justify-content: center; 
        width: 100vw;
        height: 100vh;
        background-color: ${({ theme }) => theme.color.bg_yellow};
    `,

    InputContainer: styled.div`
        width: 60%;
        height: 90vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    `,

    Title: styled.span`
        font-size: 4rem;
        margin-bottom: 1rem;
        line-height: 5rem;
        font: ${({ theme }) => theme.font.display};
    `,
};


function SignIn() {
    return (
        <Styled.SignInPage>
            <Styled.InputContainer>
                <Styled.Title>DB Online Mini Project</Styled.Title>
                <SignForm />
            </Styled.InputContainer>
        </Styled.SignInPage>
    );
};

export default SignIn;