import collections
from typing import List, Dict, DefaultDict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Function to perform topological sort on a graph
        def topoSort(nodes: List[int], graph: Dict[int, List[int]], in_degree: Dict[int, int]) -> List[int]:
            queue = collections.deque([node for node in nodes if node not in in_degree])

            result = []

            while queue:
                current_node = queue.popleft()
                result.append(current_node)

                for neighbor in graph[current_node]:
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return result

        group_items = collections.defaultdict(list)
        next_group_id = m

        # Assign groups to items and organize items by group
        for i in range(n):
            if group[i] == -1:
                group[i] = next_group_id
                next_group_id += 1

            group_items[group[i]].append(i)

        item_graph = collections.defaultdict(list)
        item_indegree = collections.defaultdict(int)

        # Build item graph and calculate in-degrees
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1

        sorted_group_items = {}

        # Perform topological sort for items within each group
        for group_id in group_items:
            sorted_items = topoSort(group_items[group_id], item_graph, item_indegree)

            if len(sorted_items) != len(group_items[group_id]):
                return []

            sorted_group_items[group_id] = sorted_items

        group_graph = collections.defaultdict(list)
        group_indegree = collections.defaultdict(int)

        # Build group graph and calculate in-degrees
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        groups = set(group)

        # Perform topological sort for groups
        sorted_groups = topoSort(groups, group_graph, group_indegree)
        if len(groups) != len(sorted_groups):
            return []
        result = []
        # Generate the final result by appending items from sorted groups
        for group_id in sorted_groups:
            result.extend(sorted_group_items[group_id])
        return result