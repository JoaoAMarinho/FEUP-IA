from random import randint
from model.Row import Row
from model.Server import Server


class DataCenter:
    def __init__(self, filename='input.txt'):
        self.rows = []
        self.servers = []
        self.parse_file(filename)
        self.initial_solution()

    def parse_file(self, filename):
        file = open(f'./src/inputs/{filename}', 'r')
        rows, slots, unavailable, self.pools, servers = (
            map(int, file.readline().strip().split()))

        for i in range(rows):
            self.rows.append(Row(slots))

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
        allocated = []
        not_allocated = [server.id for server in self.servers]

        for server in self.servers:
            for row in self.rows:
                if server.id in allocated:
                    break
                if server.size > row.max_available_slots:
                    continue

                if row.allocate_server(server):
                    allocated.append(server.id)
                    not_allocated.remove(server.id)

        self.solution = self.rows
