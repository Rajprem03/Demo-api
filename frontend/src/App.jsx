import { Box } from "@mui/material";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/layout/Sidebar";
import TopBar from "./components/layout/TopBar";

import Dashboard from "./components/dashboard/Dashboard";
import Projects from "./pages/Projects";
import APIChanges from "./pages/APIChanges";
import ImpactAnalysis from "./pages/ImpactAnalysis";
import AIRepairs from "./pages/AIRepairs";
import Validation from "./pages/Validation";

function App() {
  return (
    <BrowserRouter>
      <Box
        sx={{
          display: "flex",
          minHeight: "100vh",
          backgroundColor: "#0B0F14",
        }}
      >
        <Sidebar />

        <Box
          component="main"
          sx={{
            flexGrow: 1,
            minWidth: 0,
          }}
        >
          <TopBar />

          <Box sx={{ p: 4 }}>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/projects" element={<Projects />} />
              <Route path="/api-changes" element={<APIChanges />} />
              <Route path="/impact-analysis" element={<ImpactAnalysis />} />
              <Route path="/ai-repairs" element={<AIRepairs />} />
              <Route path="/validation" element={<Validation />} />
            </Routes>
          </Box>
        </Box>
      </Box>
    </BrowserRouter>
  );
}

export default App;