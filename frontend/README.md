# Hemut Load Status - Frontend

React + Vite frontend application for the Hemut Load Status tracking system.

## Features

- 📊 Real-time dashboard with live updates
- 👥 Driver management interface
- 🚛 Load tracking and management
- 📞 Call history viewer with transcripts
- 📈 Analytics and reporting
- 🎨 Modern, responsive UI with Tailwind CSS

## Tech Stack

- **Framework:** React 18
- **Build Tool:** Vite
- **Routing:** React Router v6
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **State Management:** React Query
- **Icons:** Lucide React
- **Charts:** Recharts
- **Notifications:** React Hot Toast

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn
- Backend API running on http://localhost:8000

### Installation

```bash
# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Edit .env with your API URL
nano .env

# Start development server
npm run dev
```

Open http://localhost:5173

### Build for Production

```bash
npm run build
npm run preview
```

## Project Structure

```
src/
├── api/              # API configuration and services
├── components/       # Reusable components
│   ├── layout/       # Layout components
│   ├── common/       # Common UI components
│   ├── dashboard/    # Dashboard-specific components
│   ├── drivers/      # Driver components
│   ├── loads/        # Load components
│   ├── calls/        # Call log components
│   └── analytics/    # Analytics components
├── pages/            # Page components
├── hooks/            # Custom React hooks
├── context/          # React Context providers
├── utils/            # Utility functions
└── styles/           # Global styles

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Environment Variables

```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_NAME=Hemut Load Status
```

## Deployment

### Vercel

```bash
npm install -g vercel
vercel
```

### Netlify

```bash
npm run build
# Drag and drop 'dist' folder to Netlify
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

Proprietary - Hemut (YC W25)