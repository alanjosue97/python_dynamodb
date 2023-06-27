from uuid import uuid4
import boto3
from boto3.dynamodb.conditions import Key


def get_db_table():
    
    dynamodb_resource = boto3.resource("dynamodb")

    return dynamodb_resource.Table("academia_python")



def insert_account(user_email: str ,user_name: str) -> dict:
    ddb_table=get_db_table()

    response=ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"#PORFILE#",
            "name": user_name

        }
    )

def invite_account(user_email:str, invited_user_email:str, invited_user_name:str):
    ddb_table=get_db_table()
    
    response=ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"USER#{invited_user_email}",
            "name": invited_user_name

        }
    )
    return response


def insert_inventory(user_email: str ,user_name: str, inventory_price: int):
    ddb_table=get_db_table()

    response=ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"#INVENTORY#{str(uuid4())}",
            "name": user_name,
            "price": inventory_price

        }
    )

    return response
 
def get_invetory(user_email:str):
    ddb_table=get_db_table()

    response = ddb_table.query(
        KeyConditionExpression=Key("PK").eq(user_email)
        & Key("SK").begins_with("#PORFILE#")
   )
    return response["Items"]

def get_profile(user_email:str):
    ddb_table=get_db_table()

    response = ddb_table.query(
        KeyConditionExpression=Key("PK").eq(user_email)
        & Key("SK").begins_with("#PROFILE#")
   )
    return response ["Items"]


def delet_inventory(user_email:str, inventory_id:str):
    ddb_table=get_db_table()

    response = ddb_table.delete_item(
        Key={
            "PK": user_email,
            "SK": f"#INVENTORY#{inventory_id}",
        }
    )

    return response

def update_inventory(user_email:str, inventory_id:str, new_inventory:str, new_price:str):
    ddb_table=get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"#INVENTORY#{inventory_id}",
            "name": new_inventory,
            "price": new_price,
        }
    )

    return response

def update_profile(user_email:str, new_name:str, new_lastname:str, new_ocupation:str,):
    ddb_table=get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": f"#PROFILE#2",
            "name": new_name,
            "lastname": new_lastname,
            "ocupation": new_ocupation,
        }
    )

    return response
""" for item in get_invetory(user_email="alpe@gmail.com"):
    print(item) """

""" print(delet_inventory(
    user_email="alpe@gmail.com",
    inventory_id="edbcadaa-1b6d-4489-a251-864f2e0acb53"
))
 """

#print(get_profile(user_email="alan@gmail.com"))
""" for item in get_profile(user_email="alan@gmail.com"):
    print(item)  
 """
""" print(insert_account(
    user_email="alpe@gmail.com",
    user_name="Aprueba"
))
 """
""" print (insert_inventory(
    user_email="alpe@gmail.com",
    user_name="mouse logitech",
    inventory_price=100,
)) """

""" print (invite_account(
    user_email="alpe@gmail.com",
    invited_user_email="alan@gmail.com",
    invited_user_name="Josue Perez",
))  """

#print(ddb_table.scan())
""" print(update_inventory(
     user_email="alpe@gmail.com",
     inventory_id="e9fe0ed7-0315-4237-914d-329a958c412d",
     new_inventory= "Keyboard Keychrome" ,
     new_price= 1224
 )) """
 
print(update_profile(
     user_email="alan@gmail.com",
     new_name= "MIGUEL" ,
     new_lastname= "PEREZ",
     new_ocupation= "PROGRAMING "
 ))