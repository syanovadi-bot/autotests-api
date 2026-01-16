from clients.private_http_builder import AuthenticationUserSchema

from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.courses.courses_client import get_courses_client, CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestSchema

from tools.fakers import fake

users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id,
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

create_exercise_request = CreateExerciseRequestSchema(
    courseId=create_course_response.course.id,
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
