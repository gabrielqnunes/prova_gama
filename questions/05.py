from pymongo import MongoClient

CONNECTION_STRING = "mongodb://admin:admin@localhost:27017/"

def obter_colecao_mongodb(url_conexao, colecao):
  client = MongoClient(url_conexao)
  return client[colecao]

print(obter_colecao_mongodb(CONNECTION_STRING, 'admin'))

