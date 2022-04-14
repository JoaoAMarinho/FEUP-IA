class Server:
    def __init__(self, id, size, capacity):
        self.id = id
        self.size = size
        self.capacity = capacity
        self.pool = -1
        self.row = -1
        self.slot = -1

    def __str__(self):
        return f"Server: {self.id}, Cap: {self.capacity}, Size: {self.size}"

    def set_pool(self, pool):
        self.pool = pool

    def set_postition(self, slot, row):
        self.slot = slot
        self.row = row