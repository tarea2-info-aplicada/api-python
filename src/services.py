from database import Connection

class CattleServices: 
    
    def getData():
        print("enter")
        cattleList = []
        cursor = Connection()
        cursor.execute("exec [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]")
        rows = cursor.fetchall()
        for row in rows:
            cattleList.append(row) 
        return cattleList   
            
