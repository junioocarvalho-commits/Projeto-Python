
import requests

url_base = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"

endpoint = (
    "/CotacaoDolarDia(dataCotacao=@dataCotacao)"
    "?@dataCotacao='08-02-2025'&$format=json"
)

response = requests.get(url_base + endpoint)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print("Erro:", response.status_code, response.text)
    
from datetime import datetime, timedelta

def cotacao_dolar_segura(data):
    data_str = data.strftime("%m-%d-%Y")

    endpoint = (
        "/CotacaoDolarDia(dataCotacao=@dataCotacao)"
        f"?@dataCotacao='{data_str}'&$format=json"
    )

    r = requests.get(url_base + endpoint)
    dados = r.json()

    if dados["value"]:
        return dados["value"][0]
    else:
        return None
    
dados = response.json()
resultado = dados.get("value", [])

if resultado:
    print(resultado[0])
else:
    print("Não há cotação disponível para essa data.")

