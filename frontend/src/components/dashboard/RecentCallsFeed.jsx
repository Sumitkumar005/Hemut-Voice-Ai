import { useQuery } from '@tanstack/react-query'
import { Phone, Clock } from 'lucide-react'
import { callLogService } from '../../api/services/callLogService'
import Badge from '../common/Badge'
import { getStatusColor } from '../../utils/helpers'
import { formatDateTime, formatDuration } from '../../utils/formatters'

export default function RecentCallsFeed() {
  const { data: calls } = useQuery({
    queryKey: ['calls', 'recent'],
    queryFn: () => callLogService.getAll({ limit: 10 }),
    refetchInterval: 30000,
  })

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Recent Calls
      </h3>
      <div className="space-y-4">
        {calls?.map((call) => (
          <div
            key={call.call_id}
            className="flex items-start space-x-3 p-3 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <div className={cn(
              'p-2 rounded-lg',
              call.call_status === 'COMPLETED' ? 'bg-success-100' : 'bg-gray-100'
            )}>
              <Phone className={cn(
                'w-5 h-5',
                call.call_status === 'COMPLETED' ? 'text-success-600' : 'text-gray-600'
              )} />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center justify-between">
                <p className="text-sm font-medium text-gray-900 truncate">
                  {call.phone_number}
                </p>
                <Badge color={getStatusColor(call.call_status)}>
                  {call.call_status}
                </Badge>
              </div>
              <p className="text-sm text-gray-500 mt-1">
                {formatDateTime(call.created_at)}
              </p>
              {call.call_duration_seconds && (
                <div className="flex items-center mt-1 text-xs text-gray-500">
                  <Clock className="w-3 h-3 mr-1" />
                  {formatDuration(call.call_duration_seconds)}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
