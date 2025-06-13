import pandas as pd
RUTA = "data/inventario.csv"

def cargar_datos():
    try:
        return pd.read_csv(RUTA)
    except:
        return pd.DataFrame(columns=["id", "nombre", "categoria", "stock", "precio"])

# Función para guardar los datos en el archivo CSV
def guardar_datos(df):
    df.to_csv(RUTA, index=False)
