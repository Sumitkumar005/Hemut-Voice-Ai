import { Routes, Route } from 'react-router-dom'
import Layout from './components/layout/Layout'
import Dashboard from './pages/Dashboard'
import DriversPage from './pages/DriversPage'
import LoadsPage from './pages/LoadsPage'
import CallsPage from './pages/CallsPage'
import AnalyticsPage from './pages/AnalyticsPage'
import NotFound from './pages/NotFound'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="drivers" element={<DriversPage />} />
        <Route path="loads" element={<LoadsPage />} />
        <Route path="calls" element={<CallsPage />} />
        <Route path="analytics" element={<AnalyticsPage />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}

export default App
