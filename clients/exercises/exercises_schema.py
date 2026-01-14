from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Exercise(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExerciseResponseSchema(BaseModel):
    """Описание структуры ответа получения задания"""
    exercise: Exercise


class GetExercisesResponseSchema(BaseModel):
    """Описание структуры ответа получения заданий"""
    exercises: list[Exercise]


class GetExercisesQuerySchema(BaseModel):
    """Описание структуры запроса на получение заданий определенного курса"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    course_id: str


class CreateExerciseRequestSchema(BaseModel):
    """Описание структуры запроса на создание задания"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class UpdateExerciseRequestSchema(BaseModel):
    """Описание структуры запроса на обновление задания"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None
