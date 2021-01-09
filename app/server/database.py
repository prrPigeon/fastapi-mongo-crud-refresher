import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = 'mongodb://localhost:27017'
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")

#helpers
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "gpa": student["gpa"]
    }

# Retrieve all students present in the db
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

# Add a new student into db
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

# Retrive a student with mathching id
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)

# Update a student with matching id
async def update_student(id: str, data: dict):
    """Return False if empty body is send"""
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        update_student = await student_collection.update_one(
            {"_id":ObjectId(id)}, {"$set": data}
        )
        if update_student:
            return True
        return False

# Delete a student from db
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True