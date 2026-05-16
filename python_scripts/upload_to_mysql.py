import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Read CSV file
df = pd.read_csv("data/Student_Data.csv")

# MySQL connection
username = "root"
password = quote_plus("Hrs5882@")

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost/student_performance"
)

# Upload data to MySQL
df.to_sql(
    name="students",
    con=engine,
    if_exists="append",
    index=False
)

print("Data uploaded successfully!")