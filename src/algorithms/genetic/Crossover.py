from abc import ABC, abstractmethod
from copy import deepcopy
from random import randint


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

        firsts1 = []
        seconds1 = []
        firsts2 = []
        seconds2 = []

        ''' 
            deallocate servers
            servers allocated first are inserted in firsts array
            servers allocated last are inserted in seconds array
            crossover point is the index that defines the barrier between firsts and lasts
        '''
        for idx in range(0, len(servers1)):
            server1, server2 = servers1[idx], servers2[idx]
            if idx < crossover_point:
                firsts1.append(server1)
                firsts2.append(server2)
            else:
               seconds1.append(server1)
               seconds2.append(server2)
            # if server is allocated
            if server1.pool != -1:
                rows1[server1.row].unset_server(server1)
                server1.unset()
            
            if server2.pool != -1:
                rows2[server2.row].unset_server(server2)
                server2.unset()
            
        
        # try to allocate seconds
        for idx in range(0, len(seconds1)):
            server1, server2 = seconds1[idx], seconds2[idx]
            for row_idx in range(len(rows1)):
                slot = rows1[row_idx].allocate_server(server1)

                # impossible to allocate in row
                if slot == -1: continue

                server1.set_position(slot, row_idx)
                server1.pool = randint(0, offspring1.pools-1)

                slot = rows2[row_idx].allocate_server(server2)
                if slot == -1: continue

                server2.set_position(slot, row_idx)
                server2.pool = randint(0, offspring2.pools-1)
                break

        # try to allocate firsts
        for idx in range(0, len(firsts1)):
            server1, server2 = firsts1[idx], firsts2[idx]
            for row_idx in range(len(rows1)):
                slot = rows1[row_idx].allocate_server(server1)

                # impossible to allocate in row
                if slot == -1: continue

                server1.set_position(slot, row_idx)
                server1.pool = randint(0, parent1.pools-1)

                slot = rows2[row_idx].allocate_server(server2)
                if slot == -1: continue

                server2.set_position(slot, row_idx)
                server2.pool = randint(0, parent1.pools-1)
                break
    
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
