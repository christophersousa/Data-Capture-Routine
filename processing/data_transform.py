import pandas as pd

def create_dataframe(data):
    return pd.DataFrame(data)

def transform_uuid(data):
    if len(data) < 32:
        # Adiciona zeros à esquerda para preencher até 32 caracteres
        data = data.zfill(32)
    elif len(data) > 32:
        raise ValueError("A string UUID não pode ter mais de 32 caracteres.")
    
    formatted_uuid = f"{data[:8]}-{data[8:12]}-{data[12:16]}-{data[16:20]}-{data[20:]}"
    return formatted_uuid
