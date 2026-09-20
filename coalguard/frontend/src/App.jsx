import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import CorporateDashboard from './pages/CorporateDashboard';
import MineDashboard from './pages/MineDashboard';
import Inspect from './pages/Inspect';
import GISMap from './pages/Map';
import TelemetryDashboard from './pages/TelemetryDashboard';
import Tickets from './pages/Tickets';
import Compliance from './pages/Compliance';
import SafetyIntelligence from './pages/SafetyIntelligence';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/corporate" element={<CorporateDashboard />} />
        <Route path="/mine/:mineId" element={<MineDashboard />} />
        <Route path="/inspect" element={<Inspect />} />
        <Route path="/map" element={<GISMap />} />
        <Route path="/telemetry" element={<TelemetryDashboard />} />
        <Route path="/tickets" element={<Tickets />} />
        <Route path="/compliance" element={<Compliance />} />
        <Route path="/safety-intelligence" element={<SafetyIntelligence />} />
      </Routes>
    </Router>
  );
}

export default App;
