import axiosInstance from '../axios'
import { ENDPOINTS } from '../endpoints'

export const vapiService = {
  initiateCall: async (data) => {
    const response = await axiosInstance.post(ENDPOINTS.VAPI_INITIATE, data)
    return response.data
  },
  
  bulkCall: async (driverIds) => {
    const response = await axiosInstance.post(ENDPOINTS.VAPI_BULK, { driver_ids: driverIds })
    return response.data
  },
}
