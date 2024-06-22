import PageNotFound from "./components/PageNotFound";
import BuildingPage from "./pages/BuildingPage";
import Homepage from "./pages/Homepage";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignUpPage from "./pages/SignUpPage";
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<BuildingPage />}></Route>
        <Route path="/home" element={<Homepage />}></Route>
        <Route path="/signup" element={<SignUpPage />}></Route>

        <Route path="*" element={<PageNotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
