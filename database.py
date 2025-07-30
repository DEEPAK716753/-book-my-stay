import mysql.connector

try:
    db = mysql.connector.connect(
        host = 'localhost' , 
        user = 'root',
        password = '',
        database = 'pg'
    )
    print("DataBase Connected")

except Exception as e:
    print("Not Connected" , e)
    
    
cursor = db.cursor()

def adminLogin(data):
    try:
        cursor.execute('select * from admin where name=%s and password=%s',data )
        return cursor.fetchone()
    except Exception as e:
        print("Error is",e)
        return False
    
def register(data):
    try:
        cursor.execute('INSERT into user(name,email,password,contact) Values (%s,%s,%s,%s)',data)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

def login(data):
    try:
        cursor.execute('select * from user where email=%s and password=%s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is",e)
        return False
    

def getAllUsers():
    try:
        cursor.execute('Select * from user')
        return cursor.fetchall()
    except:
        print("Error is ",e)
        return False


def addPgDetails(data):
    try:
        cursor.execute('insert into pg_details(pg_name,pg_address,pg_rent,pg_amenities,pg_type,pg_owner_id,pg_image) values(%s,%s,%s,%s,%s,%s,%s)', data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
def allPG():
    try:
        cursor.execute('select * from pg_details')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
    
    
def updatePgDetails(data):
    try:
        cursor.execute('update pg_details set pg_name=%s,pg_address=%s,pg_rent=%s,pg_amenities=%s,pg_type=%s,pg_owner_id=%s,pg_image=%s where id=%s', data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False 
        
        
def getSinglePg(data):
    try:
        cursor.execute('select * from pg_details where id=%s', data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is",e)
        return False
#show enquiry
    
def allEn():
    try:
        cursor.execute('select * from pg_enquiry')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
    
        
def deletePg(data):
    try:
        cursor.execute('delete from pg_details where id=%s', data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
def get_pgs_by_location(data):
    try:
        cursor.execute('select * from pg_details where pg_address=%s', (data,))
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
    
    
def get_pgs_by_filters(location=None, min_price=None, max_price=None):
    try:
        query = "SELECT * FROM pg_details WHERE 1=1"

        # location filter
        if location:
            query += " AND pg_address = %s"
            params = (location,)
        else:
            params = ()

        # minimum price filter 
        if min_price:
            query += " AND pg_rent >= %s"
            params += (min_price,)

        # maximum price filter
        if max_price:
            query += " AND pg_rent <= %s"
            params += (max_price,)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False




def add_enquiry(data):
    try:
        cursor.execute('Insert into pg_enquiry (pg_id, username, email,message) values(%s,%s,%s,%s)',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
def all_enquiry():
    try:
        cursor.execute('select * from pg_enquiry')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False