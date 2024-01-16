class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = {i:[] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            if node in visited:
                continue

            for child in adj[node]:
                if child not in visited:
                    stack.append(child)
            visited.add(node)
        
        return False

