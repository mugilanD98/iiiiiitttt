import pandas as pd
import schedule
import time
import mysql.connector
import pymysql
from sqlalchemy import create_engine

def scrc():
    co2='good'
    solar='good'
    wind='bad'
    location='good'
    
    mydb = mysql.connector.connect(host="mysql-41080-0.cloudclusters.net",port=18738,db='energy',user="test",password="test1234")
    cursor=mydb.cursor()
    sql = "TRUNCATE TABLE daily_overall_summary"
    cursor.execute(sql)
    sql = "INSERT INTO `daily_overall_summary` (`reco2`, `resolar`, `rewind`,`relocation`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (co2, solar, wind, location))
    mydb.commit()
    print(co2)
    
    
schedule.every(2).minutes.do(scrc)
while True:
    schedule.run_pending()
    time.sleep(1)
