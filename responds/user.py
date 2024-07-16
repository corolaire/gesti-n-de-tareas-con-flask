from pydantic import BaseModel,Field
class user (BaseModel):
    id_user:str=Field(min_length=1,nullable=False)
    user_name:str=Field(min_length=1,max_length=15,null=False)
    user_lastname:str=Field(min_length=1,max_length=20,null=False)
    phonenumber:int=Field(min_length=8,max_length=15,null=False)
    age:int=Field(gt=18,lt=99)
    
