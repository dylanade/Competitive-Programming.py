class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # DAG (directed acyclic graph) is a tree
        list_v = set()
        answer = set()

        for u, v in edges:
            if v not in list_v:
                list_v.add(v)

        for u, v in edges:
            if u not in list_v and u not in answer:
                answer.add(u)

        return answer