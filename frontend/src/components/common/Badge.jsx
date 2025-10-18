import { cn, getBadgeClass } from '../../utils/helpers'

export default function Badge({ children, color = 'gray', className = '' }) {
  return (
    <span className={cn('badge', getBadgeClass(color), className)}>
      {children}
    </span>
  )
}