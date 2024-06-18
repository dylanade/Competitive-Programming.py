class ThroneInheritance:
	def __init__(self, kingName: str):
		self.hashmap = defaultdict(list)
		self.king = kingName
		self.dead = set()

	def birth(self, parentName: str, childName: str) -> None:
		if parentName in self.hashmap:
			self.hashmap[parentName].append(childName)
		else:
			self.hashmap[parentName] = [childName]

	def death(self, name: str) -> None:
		self.dead.add(name)

	def getInheritanceOrder(self) -> List[str]:
		visited = set()
		inheritance = []

		if self.king not in self.dead:
			inheritance.append(self.king)

		def DFS(parent , inheritance):
			if parent not in visited:
				visited.add(parent)
				for child in self.hashmap[parent]:
					if child not in self.dead:
						inheritance.append(child)
					DFS(child , inheritance)
			return inheritance
		return DFS(self.king , inheritance)
		
# Time Complexity : O(N)
# Space Complexity : O(N)