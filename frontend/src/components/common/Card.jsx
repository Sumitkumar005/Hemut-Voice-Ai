import { cn } from '../../utils/helpers'

export default function Card({ children, className = '', ...props }) {
  return (
    <div
      className={cn('bg-white rounded-lg shadow-sm border border-gray-200 p-6', className)}
      {...props}
    >
      {children}
    </div>
  )
}