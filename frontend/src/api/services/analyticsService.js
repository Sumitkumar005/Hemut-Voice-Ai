import axiosInstance from '../axios'
import { ENDPOINTS } from '../endpoints'

export const analyticsService = {
  getDashboard: async () => {
    const response = await axiosInstance.get(ENDPOINTS.ANALYTICS_DASHBOARD)
    return response.data
  },
  
  getDelays: async (days = 30) => {
    const response = await axiosInstance.get(ENDPOINTS.ANALYTICS_DELAYS, {
      params: { days }
    })
    return response.data
  },
  
  getDriverPerformance: async (id, days = 30) => {
    const response = await axiosInstance.get(ENDPOINTS.ANALYTICS_DRIVER_PERFORMANCE(id), {
      params: { days }
    })
    return response.data
  },
  
  getDelayTrends: async (days = 30) => {
    const response = await axiosInstance.get(ENDPOINTS.ANALYTICS_TRENDS, {
      params: { days }
    })
    return response.data
  },
  
  getTopLocations: async (limit = 10) => {
    const response = await axiosInstance.get(ENDPOINTS.ANALYTICS_LOCATIONS, {
      params: { limit }
    })
    return response.data
  },
}
