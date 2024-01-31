import pandas as pd
import numpy as np
def get_data(df, station, param):
    df = df[["code","station","annee","mois","jours",param]]
    df = df.loc[df['station'] == station]
    return df    
def transform_data(df) : 
    df_np = np.array(df)
    Station = []
    Date = []
    Valuee = []
    CumulValue = []
    Source = []
    Code = []
    for row in df_np :
        Station.append(row[0])
        Date.append(str(int(row[2]))+"/"+str('{:02d}'.format(int(row[3])))+"/"+str('{:02d}'.format(int(row[4]))))
        Valuee.append(row[5])
        CumulValue.append(0)
        Code.append([])
        Source.append("METEO-BENIN")
    data = pd.DataFrame({
        "Station" : Station,
        "Date" : Date,
        "Valuee" : Valuee,
        "Codee" : Code, 
        "CumulValue" : CumulValue,
        "Source" : Source
        })
    return data
def load_data(file, formats):
  if formats == "csv":
    data = pd.read_csv(file, sep=",")
  else :
      data = pd.read_excel(file)
  return data