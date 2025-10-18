import { Package } from 'lucide-react'

export default function EmptyState({
  icon: Icon = Package,
  title = 'No data available',
  description = 'Get started by adding your first item',
  action,
}) {
  return (
    <div className="text-center py-12">
      <Icon className="mx-auto h-12 w-12 text-gray-400" />
      <h3 className="mt-2 text-sm font-semibold text-gray-900">{title}</h3>
      <p className="mt-1 text-sm text-gray-500">{description}</p>
      {action && <div className="mt-6">{action}</div>}
    </div>
  )
}