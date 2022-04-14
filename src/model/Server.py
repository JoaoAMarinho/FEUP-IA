class Server:
    def __init__(self, id, size, capacity):
        self.id = id
        self.size = size
        self.capacity = capacity
        self.pool = -1
        self.row = -1
        self.slot = -1

    def __str__(self):
        return f"\n{self.id}, Cap: {self.capacity}, Size: {self.size}, Row: {self.row}, Slot: {self.slot}, Pool: {self.pool}"
    
    def __repr__(self): 
        return self.__str__()

    def set_pool(self, pool):
        self.pool = pool

    def set_position(self, slot, row):
        self.slot = slot
        self.row = row
