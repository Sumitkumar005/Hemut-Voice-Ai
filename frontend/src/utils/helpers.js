export const cn = (...classes) => {
  return classes.filter(Boolean).join(' ')
}

export const getStatusColor = (status) => {
  const colors = {
    ACTIVE: 'success',
    INACTIVE: 'gray',
    ON_LEAVE: 'warning',
    AVAILABLE: 'success',
    IN_TRANSIT: 'primary',
    MAINTENANCE: 'warning',
    LOADED: 'success',
    NOT_LOADED: 'danger',
    DELAYED: 'danger',
    COMPLETED: 'success',
    FAILED: 'danger',
  }
  return colors[status] || 'gray'
}

export const getBadgeClass = (color) => {
  const classes = {
    success: 'badge-success',
    danger: 'badge-danger',
    warning: 'badge-warning',
    primary: 'badge-primary',
    gray: 'badge-gray',
  }
  return classes[color] || 'badge-gray'
}

export const debounce = (func, wait) => {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

export const downloadCSV = (data, filename) => {
  const csv = convertToCSV(data)
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
  const link = document.createElement('a')
  if (link.download !== undefined) {
    const url = URL.createObjectURL(blob)
    link.setAttribute('href', url)
    link.setAttribute('download', filename)
    link.style.visibility = 'hidden'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }
}

const convertToCSV = (data) => {
  if (!data || data.length === 0) return ''
  
  const headers = Object.keys(data[0])
  const rows = data.map(row => 
    headers.map(header => JSON.stringify(row[header] || '')).join(',')
  )
  
  return [headers.join(','), ...rows].join('\n')
}