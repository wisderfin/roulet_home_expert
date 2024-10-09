from fastapi import HTTPException


user_already_exists = HTTPException(status_code=409, detail = "user already exists")

user_not_found = HTTPException(status_code=404, detail="User not found")
