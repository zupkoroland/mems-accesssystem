#SQL használathoz szükséges könyvtár.
import mysql.connector

# Bejelentkezések elmentése az adatbázisban.
def uploadLogs(card, date):
    # Kapcsolat létrehozása a MYSQL-el.
    mydb = mysql.connector.connect (
            host = "localhost",
            user = "pi",
            passwd = "root",
            database = "mydb"
        )
    
    # Cursor létrehozása.
    mycursor = mydb.cursor()

    # SQL query
    sql = "INSERT INTO logs (card, date) VALUES (%s, %s)"
    val = (card, date)
    
    # Query előkészítése.
    mycursor.execute(sql, val)
    
    # Adatbázis lekérdezés végrehajtása.
    mydb.commit()
    
# Az adott kártya hozzáférésének ellenőrzése.
def queryCards(card):# Query előkésztése.
        # Kapcsolat létrehozása a MYSQL-el.
        mydb = mysql.connector.connect (
            
            host = "localhost",
            user = "pi",
            passwd = "root",
            database = "mydb"
        )
        
        # Cursor létrehozása.
        mycursor = mydb.cursor()
        
        # Az SQL Query
        sql = "SELECT enable FROM cards WHERE card = %s"
        val = (card, )
        
        # Query előkésztése, végrehajtása.
        mycursor.execute(sql, val)
        
        # Eredmény lekérése.
        myresult = mycursor.fetchone()
        
        # Eredménye visszaadása.
        return myresult[0]
