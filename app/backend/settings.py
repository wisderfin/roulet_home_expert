from pydantic_settings import BaseSettings, SettingsConfigDict


# схема переменного окружения
class Settings(BaseSettings):
    # redis
    REDIS_PASSWORD: str
    BOT_TOKEN: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
