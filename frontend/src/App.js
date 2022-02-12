import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignIn from "./pages/SignIn.jsx";
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route index element={<SignIn />} />
      </Routes>
    </Router>
  )
}

export default App;
