from algorithms.search.SearchAlgorithm import SearchAlgorithm


class TabuSearch(SearchAlgorithm):
    def __init__(self, max_iterations=10000, max_execution_time=300, tabu_tenure=3):
        self.max_iterations = max_iterations
        self.max_execution_time = max_execution_time
        self.tabu_tenure = tabu_tenure
        self.tabu_memory = {}  # a solução devia ser hashable, assim faríamos uma hash table em que cada entrada key:value continha a solução como key e o respetivo valor de tt como value

    def execute(self):
        """
        ver slides mas a ideia geral passa por
        - obter solução inicial
        - gerar todas as soluções candidatas a partir da inicial e a respetiva avaliação
        - inicializar a tabu memory com as soluções acima com tt=0 para todas (ainda nenhuma é tabu)
        - até critério de paragem não se verificar
          - selecionar melhor solução da lista de candidatas que não seja tabu (vamos querer ter aspiration criteria??)
          - se avaliação for melhor que a da atual, atualizar solução atual e tabu memory
        """
        return
