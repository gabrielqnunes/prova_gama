sku = ""
estoque = 0 

def ajustar_estoque(collection):
  collection.update({"sku": sku}, {"$set": {"estoque": estoque}})

