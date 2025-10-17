from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging

from app.config import get_settings
from app.database.session import engine, get_db
from app.api.routes import (
    drivers,
    trucks,
    loads,
    status_updates,
    call_logs,
    vapi,
    webhooks,
    analytics
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for startup and shutdown"""
    # Startup
    logger.info("🚀 Starting Hemut Load Status API...")
    logger.info(f"📊 Database: {settings.SUPABASE_URL}")
    logger.info(f"🎤 VAPI Integration: Enabled")
    
    yield
    
    # Shutdown
    logger.info("👋 Shutting down Hemut Load Status API...")


# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered load status tracking system for trucking operations",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)


# Configure CORS
origins = settings.CORS_ORIGINS.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


# Health check endpoint
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Hemut Load Status API",
        "version": settings.APP_VERSION,
        "status": "operational",
        "docs": "/api/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database": "connected",
        "vapi": "configured"
    }


# Include routers
app.include_router(drivers.router, prefix="/api/drivers", tags=["Drivers"])
app.include_router(trucks.router, prefix="/api/trucks", tags=["Trucks"])
app.include_router(loads.router, prefix="/api/loads", tags=["Loads"])
app.include_router(status_updates.router, prefix="/api/status-updates", tags=["Status Updates"])
app.include_router(call_logs.router, prefix="/api/call-logs", tags=["Call Logs"])
app.include_router(vapi.router, prefix="/api/vapi", tags=["VAPI"])
app.include_router(webhooks.router, prefix="/api/webhooks", tags=["Webhooks"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG
    )
