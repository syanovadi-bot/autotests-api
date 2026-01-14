from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


# Добавили описание структуры курса
class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema  # Вложенная структура файла
    estimated_time: str
    created_by_user: UserSchema  # Вложенная структура пользователя


class GetCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    user_id: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


# Добавили описание структуры ответа на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
