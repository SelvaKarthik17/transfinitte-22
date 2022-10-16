import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Tree from "./pages/Tree";
import BuildTree from "./pages/BuildTree";
import GetFamily from "./pages/GetFamily";

function App() {
  return (
    <div className='App'>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route path='/getfamily' element={<GetFamily/>} />
        <Route path='/tree' element={<BuildTree />} />
      </Routes>
    </div>
  );
}

export default App;
