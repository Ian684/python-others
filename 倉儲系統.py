class container_system:
    def __init__(self , data):
        self.data = data
    def search(search_id):
        print(search_id , end = ' ')
        for value in data[search_id]:
            print(value , end = ' ')
    def put(product):
        name , plus , side , price = product.split()
        if name in data:
            data[name][1] += int(plus)
        else:
            data[name] = [int(plus) , side , float(price)] 
    def take(product):
        name , minus , side , price = product.split()
        if name in data:
            if data[name][1] - minus >= 0:
                data[name][1] -= minus
        else:
            print("error")
    def inspect():
        for key , value in data:
            quantity , side , price = value
            print(key , quantity , side , price)
    def history():









if __name__ == "__main__":
    from collections import defaultdict 
    data = defaultdict(list)
    arr = []
    container_system = container_system(data)
    # name : quantity , side , price
    choice = input()
    if choice == 'put':container_system.put(input())
    elif choice == 'take':container_system.take(input())
    elif choice == 'search':container_system.search(input())
    elif choice == 'inspect':container_system.inspect()
    elif choice == 'history':container_system.history(input())
