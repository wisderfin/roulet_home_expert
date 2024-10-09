from pydantic_settings import BaseSettings, SettingsConfigDict


# схема переменного окружения
class Settings(BaseSettings):
    # postgres
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    # redis
    REDIS_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
