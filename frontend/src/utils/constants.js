export const DRIVER_STATUS = {
  ACTIVE: 'ACTIVE',
  INACTIVE: 'INACTIVE',
  ON_LEAVE: 'ON_LEAVE',
}

export const TRUCK_STATUS = {
  AVAILABLE: 'AVAILABLE',
  IN_TRANSIT: 'IN_TRANSIT',
  MAINTENANCE: 'MAINTENANCE',
  OUT_OF_SERVICE: 'OUT_OF_SERVICE',
}

export const LOAD_STATUS = {
  ASSIGNED: 'ASSIGNED',
  LOADING: 'LOADING',
  LOADED: 'LOADED',
  IN_TRANSIT: 'IN_TRANSIT',
  DELIVERED: 'DELIVERED',
  CANCELLED: 'CANCELLED',
}

export const CALL_STATUS = {
  INITIATED: 'INITIATED',
  RINGING: 'RINGING',
  ANSWERED: 'ANSWERED',
  COMPLETED: 'COMPLETED',
  FAILED: 'FAILED',
  BUSY: 'BUSY',
  NO_ANSWER: 'NO_ANSWER',
}

export const DELAY_REASONS = {
  WAREHOUSE_DELAY: 'Warehouse Delay',
  MECHANICAL_ISSUE: 'Mechanical Issue',
  WEATHER: 'Weather',
  PAPERWORK: 'Paperwork',
  TRAFFIC: 'Traffic',
  LOADING_EQUIPMENT: 'Loading Equipment',
  DRIVER_UNAVAILABLE: 'Driver Unavailable',
  OTHER: 'Other',
}

export const STATUS_COLORS = {
  ACTIVE: 'success',
  INACTIVE: 'gray',
  ON_LEAVE: 'warning',
  AVAILABLE: 'success',
  IN_TRANSIT: 'primary',
  MAINTENANCE: 'warning',
  LOADED: 'success',
  NOT_LOADED: 'danger',
  COMPLETED: 'success',
  FAILED: 'danger',
}
