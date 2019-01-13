import mysql.connector

def uploadLogs(card, date):
    mydb = mysql.connector.connect (
            host = "localhost",
            user = "pi",
            passwd = "root",
            database = "mydb"
        )

    mycursor = mydb.cursor()

    sql = "INSERT INTO logs (card, date) VALUES (%s, %s)"
    val = (card, date)
    
    mycursor.execute(sql, val)
    
    mydb.commit()
    
def queryCards(card):
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "pi",
            passwd = "root",
            database = "mydb"
        )
        mycursor = mydb.cursor()
        
        
        sql = "SELECT enable FROM cards WHERE card = %s"
        val = (card, )
        
        mycursor.execute(sql, val)
        
        myresult = mycursor.fetchone()
        
        return myresult[0]