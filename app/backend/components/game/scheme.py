from pydantic import BaseModel, field_validator, ValidationError

class DepositScheme(BaseModel):
    deposit: int

    @field_validator("deposit")
    def validate_deposit(cls, v):
        if v < 50:
            raise ValueError("Deposit must be at least 50")
        if v > 10000:
            raise ValueError("Deposit must not exceed 10000")
        if v % 50 != 0:
            raise ValueError("Deposit must be a multiple of 50")
        return v
