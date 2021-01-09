from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=6)
    gpa: float = Field(..., lte=10.0)

    class Config:
        schema_extra = {
            "example":{
                "fullname": "Vladimir Mijatovic",
                "email": "mijatovski@gmail.com",
                "course_of_study": "Computer Science",
                "year": 3,
                "gpa": '6.50'
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_example = {
            "example":{
                "fullname": "Vladimir Mijatovic",
                "email": "mijatovski@gmail.com",
                "course_of_study": "Computer Science and Mathematics",
                "year": 4,
                "gpa": '8.00'
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }

def ErrorResponseModel(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message
    }