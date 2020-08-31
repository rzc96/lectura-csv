import pandas as pd
import re
import csv
from styleframe import StyleFrame, Styler

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

df =  pd.read_csv('MOCK_DATA.csv')

for index, row in df.iterrows():
    # filtrado de correos invalidos (que no contengan @ o .xxxxx)
    tempEmail = row['Correo Electronico']
    if(re.search(regex,str(tempEmail)) == False):
        df.drop(row, inplace = True)

    # eliminar las filas que tengan la información (las 3 columnas) duplicadas
    df.drop_duplicates(subset = None, inplace= True)


# agregar estilo de subrayado para filas que tengan información duplicada
# print(df.loc[[5]]['Nombre'])
sf = StyleFrame(df)

green = Styler(bg_color="#B7F985")

sf.apply_style_by_indexes(sf[df.duplicated(subset=["Nombre", "Nombre"], keep= False)], styler_obj=green)
sf.apply_style_by_indexes(sf[df.duplicated(subset=["Correo Electronico", "Correo Electronico"], keep= False)], styler_obj=green)
sf.apply_style_by_indexes(sf[df.duplicated(subset=["Telefono", "Telefono"], keep= False)], styler_obj=green)

sf.to_excel("test.xlsx").save()

df.to_html('myTable.htm')

htmTable = df.to_html()

