from sqlalchemy import create_engine,MetaData

engine=create_engine('mysql+pymysql://admin:!PAssw0rd2@los81.cksdrck8oq7j.ap-southeast-1.rds.amazonaws.com:3306/LOSMSG81')
meta=MetaData()
conn=engine.connect()