import { useQuery } from '@tanstack/react-query'
import { Phone, MapPin } from 'lucide-react'
import { driverService } from '../../api/services/driverService'
import { vapiService } from '../../api/services/vapiService'
import Badge from '../common/Badge'
import Button from '../common/Button'
import Loading from '../common/Loading'
import { getStatusColor } from '../../utils/helpers'
import { formatPhone, getRelativeTime } from '../../utils/formatters'
import toast from 'react-hot-toast'

export default function LiveStatusBoard() {
  const { data: drivers, isLoading } = useQuery({
    queryKey: ['drivers', 'active'],
    queryFn: () => driverService.getAll({ status: 'ACTIVE' }),
    refetchInterval: 30000, // Refetch every 30 seconds
  })

  const handleCallDriver = async (driver) => {
    try {
      await vapiService.initiateCall({
        driver_id: driver.driver_id,
        phone_number: driver.phone_number,
        driver_name: driver.driver_name,
      })
      toast.success(`Calling ${driver.driver_name}...`)
    } catch (error) {
      toast.error('Failed to initiate call')
    }
  }

  if (isLoading) return <Loading />

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Live Driver Status
      </h3>
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Driver
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Phone
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Last Update
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Actions
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {drivers?.map((driver) => (
              <tr key={driver.driver_id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="font-medium text-gray-900">
                    {driver.driver_name}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {formatPhone(driver.phone_number)}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <Badge color={getStatusColor(driver.status)}>
                    {driver.status}
                  </Badge>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {driver.updated_at ? getRelativeTime(driver.updated_at) : 'Never'}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={() => handleCallDriver(driver)}
                  >
                    <Phone className="w-4 h-4 mr-1" />
                    Call
                  </Button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}