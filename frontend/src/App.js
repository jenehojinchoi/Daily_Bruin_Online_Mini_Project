import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SignIn } from "./pages";
import GlobalStyle from './styles/GlobalStyle';


function App() {
  return (
    <>
      <GlobalStyle />
      <Router>
        <Routes>
          <Route exact path ="/" element={<SignIn />} />
        </Routes>
      </Router>
    </>
  )
}

export default App;
