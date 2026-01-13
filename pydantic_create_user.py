from pydantic import BaseModel, EmailStr, ConfigDict, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """Модель данных пользователя"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """Модель для запроса на создание пользователя"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """Модель для ответа с данными созданного пользователя"""
    user: UserSchema
