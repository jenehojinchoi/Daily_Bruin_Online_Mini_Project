import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SignIn, InfoTable } from "./pages";
import GlobalStyle from './styles/GlobalStyle';


function App() {
  return (
    <>
      <GlobalStyle />
      <Router>
        <Routes>
          <Route exact path ="/signin" element={<SignIn />} />
          <Route exact path ="/" element={<InfoTable />} />
        </Routes>
      </Router>
    </>
  )
}

export default App;
