#Abraham Tabarani
#November 8, 2022

#Web Scanner - InfoStorage

import csv
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.types import Integer, Text, String, DateTime

#Store in text file
def storeText(dictionary, fileName):
    path='C:\\Users\\ATaba\\Desktop\\Coding\\Python\\Website Email Scraper\\' + fileName + '.txt'
    try:
        with open(path, 'w+', encoding='utf-8') as f: 
            for key, value in dictionary.items(): 
                f.write(key + '\n\n')
                for text in value:
                    f.write(text + '\n')
                f.write('\n')
    finally:
        print('Stored in '+fileName+'.txt')

#Store in csv file
def storeExcel(dictionary, fileName):
    path='C:\\Users\\ATaba\\Desktop\\Coding\\Python\\Website Email Scraper\\' + fileName + '.csv'
    try:
        with open(path, 'w+', encoding='utf-8') as f:
            writer=csv.writer(f)
            for key, value in dictionary.items():
                rowList=[key]
                for text in value:
                    rowList.append(text)
                writer.writerow(rowList)
    finally:
        print('Stored in '+fileName+'.csv')

#Store in SQL
def storeSQL(dictionary, fileName):
    Server='LAPTOP-GTK8NJI1\MSSQLSERVER01'
    Database='ScannerData'
    Driver='ODBC Driver 17 for SQL Server'
    databaseConn=f'mssql://@{Server}/{Database}?driver={Driver}'

    engine=create_engine(databaseConn)
    conn=engine.connect()

    df = pd.read_sql("Select * from [dbo].[ScannerData]", conn) 

    ids=[]
    links=[]
    info=[]

    #Add Indexes to Ids
    for i in range(len(dictionary)):
        ids.append(i)

    #Add links and info
    for key, value in dictionary.items():
        links.append(key)
        tempString=''
        for text in value:
            tempString=tempString+text+', '
        tempString=tempString[0:-2]
        info.append(tempString)

    #Create pandas intermediate dataframe
    fdf = pd.DataFrame({
        'ids':ids,
        'link':links,
        'info':info
    })

    #Upload to SQL
    try:
        fdf.to_sql(
            fileName,
            engine,
            index=False,
            chunksize=500,
            dtype={
                'id': Integer,
                'link': String(8000),
                'info': String(8000),
            })
    finally:
        conn.close()
        print('Stored in '+fileName)