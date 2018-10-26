import pandas as pd
import numpy as np
import math as mth
import os
import requests
import shutil
import time

# copy images to harddrive
# r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
# if r.status_code == 200:
#     with open(path, 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f) 





script_directory = os.path.split(os.path.abspath(__file__))[0]
print(script_directory)
abs_filename = os.path.join(script_directory, "lista-julio-18.xlsx")



# xls = pd.ExcelFile("../lista-julio-18.xlsx")
xls = pd.ExcelFile(abs_filename)

st = xls.parse(0) #0 is the sheet number

print("Column headings:")
print(st.columns)
print(st.index)


orden = ""
familia = ""
taxa = ""
nombreIngles = ""
nombreEsp = ""
estatus = ""

for i in st.index:
    ordenTemp = st['Orden'][i]
    familiaTemp = st['Familia'][i]
    taxaTemp = st['Taxa'][i]
    nombreInglesTemp = st['Nombre en Inglés'][i]
    nombreEspTemp = st['Nombre en Español / (Común en Costa Rica)'][i]
    estatusTemp = st['Estatus'][i]

    if pd.notnull(ordenTemp):
        orden = ordenTemp

    if pd.notnull(familiaTemp):
        familia = familiaTemp

    if pd.notnull(taxaTemp):
        taxa = taxaTemp

    if pd.notnull(nombreEspTemp):
        nombreEsp = nombreEspTemp

    if pd.notnull(estatusTemp):
        estatus = estatusTemp


    if pd.notnull(nombreInglesTemp):
        nombreIngles = nombreInglesTemp
        # remove (#) from the string
        familiaT = ' '.join(familia.split(' ')[:-1])
        print(f"""
        -------------------------------------------------------
        Orden: {orden}
        Familia: {familiaT}
        Taxa: {taxa}
        Nombre Ingles: {nombreIngles}
        Nombre Espa: {nombreEsp}
        Estatus: {estatus}
        -------------------------------------------------------""")
        # get request for wikipedia API
        # https://en.wikipedia.org/api/rest_v1/#!/Page_content/get_page_media_title_revision
        r = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/media/{taxa.replace(" ","_")}')
        # Wait for 6 miliseconds (200 request/s limit, 1/200)
        time.sleep(0.006)
        print(r.json()["items"][0]["original"]["source"])



        
# print(var1[1]) #1 is the row number...