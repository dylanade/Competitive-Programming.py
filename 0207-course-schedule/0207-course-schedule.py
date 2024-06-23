class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no cycles
        # directed graph without both directions

        graph = collections.defaultdict(list)

        # building a directed graph 
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = set()

        def dfs(course):
            # detected a cycle/loop 
            if course in visited:
                return False

            if graph[course] == []:
                return True

            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            # remove from the visited set because we finish visit it
            visited.remove(course)
            # setting course to [] because it works
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True