class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(graph, source, quietness, output):
            least_quiet = source
            for neighbour in graph[source]:
                if output[neighbour] is None:
                    dfs(graph, neighbour, quietness, output)
                least_quiet = min(least_quiet, output[neighbour], 
                                key=lambda x: quietness[x])
            output[source] = least_quiet        

        def loud_and_rich(richer, quietness):
            n = len(quietness)
            graph = [set() for i in range(n)]

            for relation in richer:
                graph[relation[1]].add(relation[0])

            output = [None for i in range(n)]

            for person in range(n):
                if output[person] is None:
                    dfs(graph, person, quietness, output)

            return output

        return loud_and_rich(richer, quiet)