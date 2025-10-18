import axiosInstance from '../axios'
import { ENDPOINTS } from '../endpoints'

export const loadService = {
  getAll: async (params = {}) => {
    const response = await axiosInstance.get(ENDPOINTS.LOADS, { params })
    return response.data
  },
  
  getById: async (id) => {
    const response = await axiosInstance.get(ENDPOINTS.LOAD_BY_ID(id))
    return response.data
  },
  
  create: async (data) => {
    const response = await axiosInstance.post(ENDPOINTS.LOADS, data)
    return response.data
  },
  
  update: async (id, data) => {
    const response = await axiosInstance.put(ENDPOINTS.LOAD_BY_ID(id), data)
    return response.data
  },
  
  updateStatus: async (id, status) => {
    const response = await axiosInstance.put(ENDPOINTS.LOAD_STATUS(id), null, {
      params: { new_status: status }
    })
    return response.data
  },
}