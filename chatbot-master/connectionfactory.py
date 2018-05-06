import pymysql.cursors  
 
# Function return a connection.
def getConnection():
     
    # You can change the connection arguments.
    # connection = pymysql.connect(
#         host='localhost',
#         user='Springstudent',
#         password='Springstudent',
#         db='Web_customer_service',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor)
    connection = pymysql.connect(
         host='localhost',
         user='root',
         password='svr',
         db='chatbot',
         charset='utf8mb4',
         cursorclass=pymysql.cursors.DictCursor
         )
    print ("DB connection successfully created.")
    return connection
