export const ENDPOINTS = {
  // Health
  HEALTH: '/health',
  
  // Drivers
  DRIVERS: '/api/drivers',
  DRIVER_BY_ID: (id) => `/api/drivers/${id}`,
  
  // Trucks
  TRUCKS: '/api/trucks',
  TRUCK_BY_ID: (id) => `/api/trucks/${id}`,
  
  // Loads
  LOADS: '/api/loads',
  LOAD_BY_ID: (id) => `/api/loads/${id}`,
  LOAD_STATUS: (id) => `/api/loads/${id}/status`,
  
  // Call Logs
  CALL_LOGS: '/api/call-logs',
  CALL_LOG_BY_ID: (id) => `/api/call-logs/${id}`,
  CALL_TRANSCRIPT: (id) => `/api/call-logs/${id}/transcript`,
  
  // Status Updates
  STATUS_UPDATES: '/api/status-updates',
  STATUS_LATEST: '/api/status-updates/latest',
  STATUS_LOADED: '/api/status-updates/loaded',
  STATUS_NOT_LOADED: '/api/status-updates/not-loaded',
  
  // VAPI
  VAPI_INITIATE: '/api/vapi/initiate-call',
  VAPI_BULK: '/api/vapi/bulk-call',
  
  // Analytics
  ANALYTICS_DASHBOARD: '/api/analytics/dashboard',
  ANALYTICS_DELAYS: '/api/analytics/delays',
  ANALYTICS_DRIVER_PERFORMANCE: (id) => `/api/analytics/driver-performance/${id}`,
  ANALYTICS_TRENDS: '/api/analytics/delay-trends',
  ANALYTICS_LOCATIONS: '/api/analytics/top-delay-locations',
}
