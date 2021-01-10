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

@router.put("/{id}")
async def update_student_data(id: str, request: UpdateStudentModel = Body(...)):
    request = {k: v for k,v in request.dict().items() if v is not None}
    updated_student = await update_student(id, request)
    if updated_student:
        return ResponseModel(
            f"Student with ID: {id} name is updated successfully",
            "Success"
        )
    return ErrorResponseModel("An error occured", 404, "Something went wrong")

@router.delete("/{id}", response_description="Student data is deleted")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            f"Student with ID: {id} is deleted successfully",
            "Success"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"Student with ID: {id} does not exist"
    )