from abc import abstractmethod
from math import inf


class Algorithm():
    def __init__(self, max_iterations=10000, max_iterations_no_imp=1000):
        self.max_iterations = max_iterations
        self.max_iterations_no_imp = max_iterations_no_imp

    @abstractmethod
    def execute(self):
        pass

    def stop(self, iteration, iteration_no_imp):
        return iteration >= self.max_iterations or iteration_no_imp >= self.max_iterations_no_imp

    def evaluate(self, solution):
        rows, servers, pools = solution.values()
        guaranteed_capacity = [ 0 for _ in range(pools) ]
        max_row_capacity = [ 0 for _ in range(pools) ]
        for row in rows:
            idx = 0
            row_capacity = [ 0 for _ in range(pools) ]
            slots = row.slots
            
            while idx < len(slots):
                if server_idx:=slots[idx] < 0:
                    idx += 1
                    continue

                server = servers[server_idx]
                row_capacity[server.pool] += server.capacity
                idx += server.size
            
            for idx in range(pools):
                max_row_capacity[idx] = max(max_row_capacity[idx], row_capacity[idx])
                guaranteed_capacity[idx] += row_capacity[idx]

        evaluation = inf
        for idx in range(pools):
            guaranteed_capacity = guaranteed_capacity[idx] - max_row_capacity[idx]
            evaluation = min(evaluation, guaranteed_capacity)
