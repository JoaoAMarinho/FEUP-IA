from random import randint
from model.Row import Row
from model.Server import Server

class DataCenter:
    def __init__(self, filename = 'input.txt'):
        self.rows = []
        self.servers = []
        self.parse_file(self, filename)
        self.solution = self.initial_solution(self)

    def parse_file(self, filename):
        file = open(f'./src/inputs/{filename}', 'r')
        rows, slots, unavailable, self.pools, servers = (
            map(int, file.readline().strip().split()))
       
        for i in range(rows):
            self.rows.append(Row(slots))

        for i in range(unavailable):
            slot, row_index = map(int, file.readline().strip().split())
            row = self.rows[row_index]
            row.set_unavailable(slot)
            
        for i in range(servers):
            size, capacity = map(int, file.readline().strip().split())
            server = Server(i, size, capacity)
            self.servers.append(server)
        
        file.close()
    
    def initial_solution(self):
        allocated = []
        not_allocated = [server.id for server in self.servers]
        
        for row in self.rows:
            for server in self.servers:
                if server.id in allocated: continue

                if row.allocate_server(row, server): 
                    allocated.append(server.id)
                    not_allocated.remove(server.id)
                

