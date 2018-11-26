import pandas as pd
import numpy as np
import math as mth
import os
import requests
import shutil
import time
import sys

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
        Total: {i} out of {st.index.size} ({(100/st.index.size) * i:.2f}%)""")
        # Wait for 6 miliseconds (200 request/s limit, 1/200)
        # Wait for 10 miliseconds (200 request/s limit, 1/200)
        time.sleep(0.1)
        try:
            # get request for wikipedia API
            # https://en.wikipedia.org/api/rest_v1/#!/Page_content/get_page_media_title_revision
            imageRequest = requests.get(f'https://es.wikipedia.org/api/rest_v1/page/media/{taxa.replace(" ","_")}')
            descriptionRequest = requests.get(f'https://es.wikipedia.org/api/rest_v1/page/summary/{taxa.replace(" ","_")}')
            imageUrl = imageRequest.json()["items"][0]["original"]["source"]
            description = descriptionRequest.json()["extract"]
            print(f"""
        Image URL: {imageUrl}
        Description: {description}
        """)
        except:
            print("there is no picture")

        try:
            xeno = requests.get(f'https://www.xeno-canto.org/api/2/recordings?query={taxa.replace(" ","%20")}')
            # xeno = requests.get(f'https://www.xeno-canto.org/api/2/recordings?query={taxa.replace(" ","%20")}')
            recording = xeno.json()["recordings"][0]
            print(f"""
        Recording: {recording['url']}
        Quality: {recording["q"]}
        """)
        except Exception as ex:
            print(ex)
            print("theres no recordings or error")
        
        print("""
        -------------------------------------------------------""")



        
# print(var1[1]) #1 is the row number...