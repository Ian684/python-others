class container_system:
    def __init__(self, data):
        self.data = data

    def search(self, search_id):
        if search_id not in self.data:
            print("error")
            return
        print(search_id, *self.data[search_id])

    def put(self, product):
        name, plus, side, price = product.split()
        quantity = int(plus)
        if name in self.data:
            self.data[name][0] += quantity
        else:
            self.data[name] = [quantity, side, float(price)]

    def take(self, product):
        name, minus, *_ = product.split()
        quantity = int(minus)
        if name in self.data and self.data[name][0] >= quantity:
            self.data[name][0] -= quantity
        else:
            print("error")

    def inspect(self):
        for key, value in sorted(self.data.items()):
            quantity, side, price = value
            print(key, quantity, side, price)

    def history(self, _command=None):
        print("history is not available")




if __name__ == "__main__":
    from collections import defaultdict 
    data = defaultdict(list)
    arr = []
    system = container_system(data)
    # name : quantity , side , price
    choice = input()
    if choice == 'put':
        system.put(input())
    elif choice == 'take':
        system.take(input())
    elif choice == 'search':
        system.search(input())
    elif choice == 'inspect':
        system.inspect()
    elif choice == 'history':
        system.history(input())
