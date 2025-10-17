import asyncio
import asyncpg
from pathlib import Path
import sys
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings

settings = get_settings()


async def run_migrations():
    """Execute all SQL migration files"""
    
    # Extract connection parameters from DATABASE_URL
    # Format: postgresql+asyncpg://user:pass@host:port/database
    url = settings.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://")
    
    print("🔄 Connecting to database...")
    conn = await asyncpg.connect(url)
    
    try:
        # Get migration files
        migrations_dir = Path(__file__).parent.parent / "app" / "database" / "migrations"
        
        if not migrations_dir.exists():
            print("❌ Migrations directory not found")
            return
        
        migration_files = sorted(migrations_dir.glob("*.sql"))
        
        print(f"📂 Found {len(migration_files)} migration files")
        
        for migration_file in migration_files:
            print(f"   Running: {migration_file.name}")
            
            with open(migration_file, 'r') as f:
                sql = f.read()
            
            try:
                await conn.execute(sql)
                print(f"   ✅ {migration_file.name} completed")
            except Exception as e:
                print(f"   ❌ {migration_file.name} failed: {str(e)}")
        
        print("✅ All migrations completed!")
    
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(run_migrations())
