from functools import reduce
from math import inf

class Solution:
    """
    Solution class model
    """
    def __init__(self, rows=[], servers=[], pools=1):
        self.rows = rows
        self.servers = servers
        self.pools = pools
        self.evaluate()
    
    def __str__(self):
        str_repr = ':::::::::::::::::::::::::::::::: rows ::::::::::::::::::::::::::::::::n'
        for row in self.rows: str_repr += f'{row}\n'

        str_repr += '\n\n:::::::::::::::::::::::::::::::: servers ::::::::::::::::::::::::::::::::\n'
        for server in self.servers: str_repr += f'{server}\n'

        str_repr += '\n\n:::::::::::::::::::::::::::::::: pools ::::::::::::::::::::::::::::::::\n'
        str_repr += f'{self.pools}\n'

        return str_repr

    def __repr__(self):
        return self.__str__()

    def __eq__(self, sol):
        if not isinstance(sol, self.__class__): return False
        return sol.rows == self.rows and sol.servers == self.servers and sol.pools == self.pools

    def __hash__(self):
        return reduce(lambda hash, s2: hash * abs(s2.id + s2.row + s2.pool + s2.slot), self.servers, 0)

    def evaluate(self):
        """
        Updates the evaluation of the current solution state
        """
        guaranteed_capacity = [0 for _ in range(self.pools)]
        max_row_capacity = [0 for _ in range(self.pools)]

        for row in self.rows:
            idx = 0
            row_capacity = [0 for _ in range(self.pools)]
            slots = row.slots

            while idx < len(slots):
                server_idx = slots[idx]
                if server_idx < 0:
                    idx += 1
                    continue

                server = self.servers[server_idx]
                row_capacity[server.pool] += server.capacity
                idx += server.size

            for idx in range(self.pools):
                max_row_capacity[idx] = max(max_row_capacity[idx], row_capacity[idx])
                guaranteed_capacity[idx] += row_capacity[idx]

        evaluation = inf
        for idx in range(self.pools):
            guaranteed_cap = guaranteed_capacity[idx] - max_row_capacity[idx]
            evaluation = min(evaluation, guaranteed_cap)

        self.evaluation = evaluation
