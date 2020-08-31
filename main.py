import pandas as pd
import re
import csv

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


#nombre correo telefono
df =  pd.read_csv('MOCK_DATA.csv')
# print(df)

for index, row in df.iterrows():
    #filtrado de correos invalidos (que no contengan @ o .xxxxx)
    tempEmail = row['Correo Electronico']
    if(re.search(regex,str(tempEmail)) == False):
        df.drop(row, inplace = True)

    # eliminar las filas que tengan la información (las 3 columnas) duplicadas
    df.drop_duplicates(subset=None, inplace= True)



df.to_html('myTable.htm')

htmTable = df.to_html()

