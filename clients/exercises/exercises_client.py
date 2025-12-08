import uuid
from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class GetExercisesByCourse(TypedDict):
    """Описание структуры запроса на получение заданий определенного курса"""
    courseId: uuid.UUID


class CreateExercise(TypedDict):
    """Описание структуры запроса на создание задания"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercise(TypedDict):
    """Описание структуры запроса на обновление задания"""
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesByCourse) -> Response:
        """
        Метод получения списка заданий для определенного курса.
        :param query: Словарь с course_id
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: uuid.UUID) -> Response:
        """
        Метод получения информации о задании по exercise_id
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExercise) -> Response:
        """
        Метод создания задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: uuid.UUID, request: UpdateExercise) -> Response:
        """
        Метод обновления задания
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: uuid.UUID) -> Response:
        """
        Метод удаления задания
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')
