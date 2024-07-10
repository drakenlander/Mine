import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

server = 'localhost'
database = 'StagingRealEstate'
driver = 'ODBC Driver 17 for SQL Server'

connection_string = f'mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes'
engine = create_engine(connection_string, connect_args = {'autocommit':True})

with open('Extract.sql', 'r') as file:
    query = file.read()

with engine.connect() as conn:
    df = pd.read_sql(query, conn.connection)

df['Date_Recorded'] = pd.to_datetime(df.Date_Recorded)
df['Date_Recorded'] = df['Date_Recorded'].dt.strftime('%d/%m/%Y')

df['Location'] = df['Location'].str.slice(start=7)
df['Location'] = df['Location'].str.slice(0, -1)

df.fillna("No aplica", inplace=True)

print(df.head())

with engine.connect() as conn:
    with open("ChangeDatabase.sql") as file:
        query = text(file.read())
        conn.execute(query)

    with open("CreateTables.sql") as file:
        query = text(file.read())
        conn.execute(query)

df_fact = df[['Serial_Number', 'List_Year', 'Address', 'Assessed_Value', 'Sale_Amount', 'Sales_Ratio', 'Assessor_Remarks', 'OPM_remarks', 'Location']]

df_fact.to_sql('Fact_RealEstate', con=engine, if_exists='replace', index=False)

df['Date_Recorded'].to_sql('Dim_Date', con=engine, if_exists='replace', index=False)
df['Town'].to_sql('Dim_Town', con=engine, if_exists='replace', index=False)
df['Property_Type'].to_sql('Dim_PropertyType', con=engine, if_exists='replace', index=False)
df['Residential_Type'].to_sql('Dim_ResidentialType', con=engine, if_exists='replace', index=False)
df['Non_Use_Code'].to_sql('Dim_NonUseCode', con=engine, if_exists='replace', index=False)
