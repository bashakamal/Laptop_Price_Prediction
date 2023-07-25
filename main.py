import numpy as np
import pandas as pd
import pickle
import streamlit as lt

file = open(r"C:\Users\basha\Downloads\gradient_boosting_regression_model.pkl", 'rb')
gb=pickle.load(file)
file.close()

data = pd.read_csv(r"C:\Users\basha\Downloads\lasttrain.csv")
print(data.columns)
# streamlit run main.py

# lt run C:\Users\basha\PycharmProjects\pythonProject17\main.py



lt.title('Laptop price Predictor')
company=lt.selectbox('Brand',data['Company'].unique())
type=lt.selectbox('Type',data['TypeName'].unique())
ram=lt.selectbox('Ram',data['Ram'].unique())
os=lt.selectbox('Os',data['OpSys'].unique())
weight=lt.number_input('weight of the laptop')
touchscreen=lt.selectbox('touchscreen',['No','Yes'])
ips=lt.selectbox('IPS Panel',['No','Yes'])
screensize=lt.number_input('Screen Size')
resolution=lt.selectbox('Screen Resolution',['1920x1080','2880x1800','1366x768','1600x990','3840x2160'])
cpu=lt.selectbox('Cpu_name',data['Cpu_name'].unique())
hdd=lt.selectbox('HDD in GB',[0,128,256,512,1024,2048])
ssd=lt.selectbox('SSD in GB',[0,8,128,256,512,1024])
gpu=lt.selectbox('gpu brand',data['Gpu brand'].unique())

if lt.button('Predict Price'):
    ppi=None
    if touchscreen == 'Yes':
        touchscreen=1
    else:
        touchscreen=0

    if ips=='Yes':
        ips=1
    else:
        ips=0
    X_resolution=int(resolution.split('x')[0])
    Y_resolution=int(resolution.split('x')[1])
    ppi=((X_resolution * 2)+(Y_resolution*2))**0.5//(screensize)

    query=np.array(['Company', 'TypeName', 'Ram', 'OpSys', 'Weight', 'touchscreen',
       'IPS Panel', 'PPI', 'Cpu_name', 'SSD', 'HDD', 'Gpu brand'])

    query=query.shape(1,12)

    prediction=int(np.exp(gb.predict(query)[0]))

    lt.title("predict price of laptop could be between" +
             str(prediction-1000)+'Rs.'+"to"+str(prediction+1000)+'Rs.')












