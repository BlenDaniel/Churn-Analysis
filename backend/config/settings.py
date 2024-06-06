# backend/config/settings.py

# backend/config/settings.py

from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    db_username: str = os.getenv("DB_USERNAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")
    logging_level: str = os.getenv("LOGGING_LEVEL")
    arbitrary_types_allowed = True


    @property
    def database_url(self) -> str:
        print(f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        return f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
