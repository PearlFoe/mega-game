from pydantic import BaseSettings

class Settings(BaseSettings):
	secret_key: str
	real_ip: str
	
	db_name: str
	db_user_name: str
	db_password: str

settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8'
)