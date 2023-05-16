from sqlalchemy import create_engine,MetaData

engine=create_engine('mysql+pymysql://admin:!PAssw0rd2@los-database.cj9vmy6xz4qz.us-east-1.rds.amazonaws.com:3306/sys')
meta=MetaData()
conn=engine.connect()