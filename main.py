import csv

df =  pd.read_csv('MOCK_DATA.csv')

df.to_html('myTable.htm')

htmTable = df.to_html()

