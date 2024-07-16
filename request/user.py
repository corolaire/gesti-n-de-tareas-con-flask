from pydantic import BaseModel,UUID4
class user(BaseModel):
    id_user=UUID4
    user_name=str
    user_lastname=str
    phonenumber=int
    age=int
