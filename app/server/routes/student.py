from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_student,
    retrieve_student,
    retrieve_students,
    update_student,
    delete_student
)
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentShema,
    UpdateStudentModel
)

router = APIRouter()

@router.post("/", response_description="Student data added into db")
async def add_student_data(student: StudentShema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully")


@router.get("/", response_description="Students retrived")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Studens data retrieved successfully")
    return ResponseModel(students, "Empty List Returned")\

@router.get("/{id}", response_description="Student data retrieved")
async def get_student(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Studend data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "There is no student with that id")

