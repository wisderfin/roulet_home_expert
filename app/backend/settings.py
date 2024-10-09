from pydantic_settings import BaseSettings, SettingsConfigDict


# схема переменного окружения
class Settings(BaseSettings):
    # redis
    REDIS_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
