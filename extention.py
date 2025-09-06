from flask_sqlalchemy import SQLAlchemy
import time
# from sqlalchemy import create_engine, text

# مسیر دیتابیس
# SQLALCHEMY_DATABASE_URI = "sqlite:///D:/py/market/instance/database.db"

# # ساخت engine
# engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT sqlite_version();"))
#         version = result.fetchone()
#         print("✅ اتصال موفق. نسخه SQLite:", version[0])
# except Exception as e:
#     print("❌ خطا در اتصال:", e)

db=SQLAlchemy()


def get_current_time():
    return round(time.time())