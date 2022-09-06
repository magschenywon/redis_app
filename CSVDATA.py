import redis
import mysql.connector
import datetime

def connect():
    conn=redis.Redis(host= "127.0.0.1", port = 6379)
    print(redis.Redis.ping(conn))
    return conn



def setString(mkey,mval):
    redis1=connect()
    redis1=set(key=mkey,value =mval)
    return setString
    #print(redis1)

def getString(mkey):
    redis1=connect()
    return redis1.get(mkey) 

def getDataFromMySQL():
    conn=mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='CSVDATA')
    #conn = mysql.connector.connect("127.0.0.1","root@localhost","","CSVDATA")
 
    
    cur1=conn.cursor()
    cur1.execute("SELECT * FROM US_COUNTRIES")
    print("result:")
    mkey = None
    mval = None
    
    for row in cur1.fetchall():
        mkey="covid19" + ":"+"date/"+"county/"+"state/"+"flips/"+"cases/"+"deaths"
        mval =row[0]+"/"+row[1]+"/"+row[2]+"/"+row[3]+"/"+row[4]+"/"+row[5]
        print(mkey +':'+mval)
       

    print("end")

    
getDataFromMySQL()
