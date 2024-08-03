class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build an adjacency list of prereqs

        graph = collections.defaultdict(int)

        answer = []
        degrees = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}

        # Initialize the graph
        for target, pre in prerequisites:
            graph[pre].append(target)
            degrees[target] += 1
        
        # Find all courses with no prerequisites
        queue = collections.deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        
        # Process each course
        while queue:
            node = queue.popleft()
            answer.append(node)
            
            for neighbour in graph[node]:
                degrees[neighbour] -= 1
                if degrees[neighbour] == 0:
                    queue.append(neighbour)
        
        return answer if len(answer) == numCourses else []
        