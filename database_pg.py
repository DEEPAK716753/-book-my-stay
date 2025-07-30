import mysql.connector

try:
    db = mysql.connector.connect(
        host = 'localhost' , 
        user = 'root',
        password = '',
        database = 'pg-entries'
    )
    print("DataBase Connected")

except Exception as e:
    print("Not Connected" , e)
    
    
cursor = db.cursor()

def register(data):
    try:
        cursor.execute('INSERT into user(name,email,password) Values (%s,%s,%s)',data)
        
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getAllUsers():
    try:
        cursor.execute('Select * from user')
        return cursor.fetchall()
    except:
        print("Error is ",e)
        return False
    

getAllUsers()
