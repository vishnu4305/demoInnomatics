from sqlalchemy import text
from database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM products"))
        print("✅ Connected to MySQL! Products in table:", result.scalar())
except Exception as e:
    print("❌ Connection failed:")
    print(e)