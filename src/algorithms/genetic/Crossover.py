from abc import ABC, abstractmethod
from copy import deepcopy


class CrossoverMethod(ABC):
    """
    General abstract crossover class
    Crossover, also called recombination, is a genetic operator used to combine the genetic information of two parents to generate new offspring
    """

    @abstractmethod
    def run(self, parent1, parent2):
        pass

class ServersCrossover(CrossoverMethod):

    def run(self, parent1, parent2):
        """
        Runs the server crossover
        ...
        Returns:
            The newly generated offsprings
        """
        
        offspring1, offspring2 = deepcopy(parent1), deepcopy(parent2)
        servers1, rows1 = offspring1.servers, offspring1.rows
        servers2, rows2 = offspring2.servers, offspring2.rows

        crossover_point = len(servers1) // 2

        # deallocate right half of servers
        for idx in range(crossover_point, len(servers1)):
            server1, server2 = servers1[idx], servers2[idx]
            
            # if server is allocated
            if server1.pool != -1:
                rows1[server1.row].unset_server(server1)
                server1.unset()
            
            if server2.pool != -1:
                rows2[server2.row].unset_server(server2)
                server2.unset()
        
        # try to allocate new right half of servers
        for idx in range(crossover_point, len(servers1)):
            server1, server2 = servers1[idx], servers2[idx]
            initial_server1, initial_server2 = parent1.servers[idx], parent2.servers[idx]

            if initial_server1.pool != -1:
                row, slot = initial_server1.row, initial_server1.slot
                if rows2[row].allocate_server_to_slot(server2, slot):
                    server2.set_position(slot, row)
                    server2.set_pool = initial_server1.pool

            if initial_server2.pool != -1:
                row, slot = initial_server2.row, initial_server2.slot
                if rows1[row].allocate_server_to_slot(server1, slot):
                    server1.set_position(slot, row)
                    server1.set_pool = initial_server2.pool
    
        return [offspring1, offspring2]

class PoolsCrossover(CrossoverMethod):

    def run(self, parent1, parent2):
        """
        Runs the pools crossover
        ...
        Returns:
            The newly generated offsprings
        """

        offspring1, offspring2 = deepcopy(parent1), deepcopy(parent2)
        servers1 = offspring1.servers
        servers2 = offspring2.servers

        crossover_point = len(servers1) // 2
        for idx in range(crossover_point, len(servers1)):
            server1 = servers1[idx]
            server2 = servers2[idx]

            if server1.pool != -1:
                server1.pool = new_pool if (new_pool:=parent2.servers[idx].pool) != -1 else server1.pool
            if server2.pool != -1:
                server2.pool = new_pool if (new_pool:=parent1.servers[idx].pool) != -1 else server2.pool

        return [offspring1, offspring2]
