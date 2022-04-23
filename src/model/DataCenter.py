from model.Row import Row
from model.Server import Server
from model.Solution import Solution
from random import randint


class DataCenter:
    """
    Data Center class model
    """

    def __init__(self, filename='input.txt'):
        self.rows = []
        self.servers = []
        self.parse_file(filename)
        self.solution = self.initial_solution()

    def parse_file(self, filename):
        file = open(f'src/inputs/{filename}', 'r')
        rows, slots, unavailable, self.pools, servers = (
            map(int, file.readline().strip().split()))

        self.rows = [Row(slots) for _ in range(rows)]

        for i in range(unavailable):
            row_idx, slot_idx = map(int, file.readline().strip().split())
            row = self.rows[row_idx]
            row.set_unavailable(slot_idx)

        for i in range(servers):
            size, capacity = map(int, file.readline().strip().split())
            server = Server(i, size, capacity)
            self.servers.append(server)

        file.close()

    def initial_solution(self):
        for server in self.servers:
            for row_idx, row in enumerate(self.rows):
                slot = row.allocate_server(server)

                # impossible to allocate in row
                if slot == -1: continue

                server.set_position(slot, row_idx)
                server.pool = randint(0, self.pools-1)
                break
        
        return Solution(self.rows, self.servers, self.pools)
