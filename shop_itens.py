
class ShopItem:
    def __init__(self):
        self.nome = ""
        self.quantidade = 0
        self.valor = 0
        
    def retorna_valor(self):
        valor_final = self.quantidade * self.valor
        return valor_final

class ShopList: 
    def __init__(self):
        self.shop_list = []
    
    def adicionar_item(self, item: ShopItem):
        self.shop_list.append(item)
    
    def soma_lista(self):
        valor = 0  
        for item in self.shop_list:
            valor += item.retorna_valor()
        return valor

if __name__ == "__main__":
    lista = ShopList()
    
    while lista.soma_lista() < 100:
        item = ShopItem()
        item.nome = input("Digite o nome do item: ")
        item.quantidade = int(input("Digite a quantidade do item: "))
        item.valor = float(input("Digite o valor do item: "))
        