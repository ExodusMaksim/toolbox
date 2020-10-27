import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

db = cx_Oracle.connect('demeter_utils', 'password', '172.16.129.148:1521/ubsp')

print (db.version)

cr=db.cursor()

sql='select * from sys_user'

cr.execute(sql)

rs=cr.fetchall()

zz=pd.DataFrame(rs);

print (zz)

db.close()