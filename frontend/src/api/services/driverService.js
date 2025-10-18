import axiosInstance from '../axios'
import { ENDPOINTS } from '../endpoints'

export const driverService = {
  getAll: async (params = {}) => {
    const response = await axiosInstance.get(ENDPOINTS.DRIVERS, { params })
    return response.data
  },
  
  getById: async (id) => {
    const response = await axiosInstance.get(ENDPOINTS.DRIVER_BY_ID(id))
    return response.data
  },
  
  create: async (data) => {
    const response = await axiosInstance.post(ENDPOINTS.DRIVERS, data)
    return response.data
  },
  
  update: async (id, data) => {
    const response = await axiosInstance.put(ENDPOINTS.DRIVER_BY_ID(id), data)
    return response.data
  },
  
  delete: async (id) => {
    const response = await axiosInstance.delete(ENDPOINTS.DRIVER_BY_ID(id))
    return response.data
  },
}
