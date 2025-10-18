import axiosInstance from '../axios'
import { ENDPOINTS } from '../endpoints'

export const callLogService = {
  getAll: async (params = {}) => {
    const response = await axiosInstance.get(ENDPOINTS.CALL_LOGS, { params })
    return response.data
  },
  
  getById: async (id) => {
    const response = await axiosInstance.get(ENDPOINTS.CALL_LOG_BY_ID(id))
    return response.data
  },
  
  getTranscript: async (id) => {
    const response = await axiosInstance.get(ENDPOINTS.CALL_TRANSCRIPT(id))
    return response.data
  },
}
