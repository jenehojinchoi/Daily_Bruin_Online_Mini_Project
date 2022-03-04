import React, { useState, useEffect } from 'react'
import styled from 'styled-components';
import { Container, Row, Col } from 'react-bootstrap'
import axios from 'axios';

const config = {
    headers: {
        'Content-type': "application-json"
    },
    baseURL: 'http://127.0.0.1:5000',
}

const Styled = {
    InfoLayout : styled.div`
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 100vw;
        height: 100vh;
        font: ${({ theme }) => theme.font.display};
        background-color: ${({ theme }) => theme.color.bg_yellow};
    `,

    Title: styled.div`
        margin: 2rem;
    `,

    InfoGrid: styled.div`
        width: 200rem;
        height: auto;
        font: ${({ theme }) => theme.font.table};
    `,

    Input: styled.input`
        width: 13rem;
        background-color: ${({ theme }) => theme.color.bg_skyblue};
        border-radius: 1rem;
    `,

    Button: styled.button`
        border: solid 0.1rem;
        border-color: ${({ theme }) => theme.color.black};
        border-radius: 1rem;
    `,
}

const getSources = async() => {
    try {
        const res = await axios.get(`${config.baseURL}/api/source`);
        return res.data;
    } catch (e) {
        return e;
    }
};

const updateSource = async(newName) => {

    try {
        const res = await axios.get(`${config.baseURL}/api/source`, );
        return res.data;
    } catch (e) {
        return e;
    }
};


function InfoTable() {
    const [ sources, setSources ] = useState([]);
    const [ sourceName, setSourceName ] = useState("");

    const handleChange = (e) => {
        setSourceName(e.target.value);
    }

    useEffect(() => {
        getSources().then(data => {
            setSources(data);
        })
    }, []);

    return (
    <Styled.InfoLayout>
        <Styled.Title>Source</Styled.Title>
        <Styled.InfoGrid>
            <Container style={{ border: "solid 0.1rem", height: "20rem", borderRadius: "1.5rem" }}>
                <Row className="justify-content-md-center" style={{height: "3rem", margin: "2rem"}}>
                    <Col sm>Name</Col>
                    <Col sm>Organization</Col>
                    <Col sm>Email</Col>                   
                    <Col sm>Notes</Col>                   
                    <Col sm>Phone</Col>    
                    <Col sm></Col>       
                </Row>
                {sources && sources.map((source, idx) => (
                    <Row className="justify-content-md-center" style={{height: "3rem", margin: "2rem"}}>
                        <Col sm>
                            <Styled.Input type="text" name="name" value={source.name} onChange={handleChange}/>
                        </Col>
                        <Col sm>
                            <Styled.Input type="text" name="name" value={source.organization} />
                        </Col>
                        <Col sm>
                            <Styled.Input type="text" name="name" value={source.email}/>
                        </Col>                 
                        <Col sm>
                            <Styled.Input type="text" name="name" value={source.notes}/>
                        </Col>                   
                        <Col sm>
                            <Styled.Input type="text" name="name" value={source.phone}/>
                        </Col>
                        <Col sm><Styled.Button>update</Styled.Button></Col> 
                    </Row>          
                ))}
            </Container>
        </Styled.InfoGrid>
    </Styled.InfoLayout>
    )
}

export default InfoTable
