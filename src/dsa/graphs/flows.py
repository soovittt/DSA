from __future__ import annotations
from collections import deque
from typing import Deque, Dict, Hashable, List

Node = Hashable


def edmonds_karp(capacity: Dict[Node, Dict[Node, int]], s: Node, t: Node) -> int:
    flow: Dict[Node, Dict[Node, int]] = {u: {v: 0 for v in capacity.get(u, {})} for u in capacity}

    def bfs() -> Dict[Node, Node] | None:
        parent: Dict[Node, Node] = {}
        q: Deque[Node] = deque([s])
        parent[s] = s
        while q:
            u = q.popleft()
            for v, cap in capacity.get(u, {}).items():
                if v not in parent and cap - flow[u].get(v, 0) > 0:
                    parent[v] = u
                    if v == t:
                        return parent
                    q.append(v)
            for v in capacity:  # residual for reverse edges
                if u in capacity.get(v, {}) and v not in parent and flow[v].get(u, 0) > 0:
                    parent[v] = u
                    if v == t:
                        return parent
                    q.append(v)
        return None

    max_flow = 0
    while True:
        parent = bfs()
        if parent is None or t not in parent:
            break
        # find bottleneck
        v = t
        bottleneck = float('inf')
        while v != s:
            u = parent[v]
            if v in capacity.get(u, {}):
                bottleneck = min(bottleneck, capacity[u][v] - flow[u].get(v, 0))
            else:
                bottleneck = min(bottleneck, flow[v][u])
            v = u
        # augment
        v = t
        while v != s:
            u = parent[v]
            if v in capacity.get(u, {}):
                flow[u][v] = flow[u].get(v, 0) + bottleneck
            else:
                flow[v][u] = flow[v][u] - bottleneck
            v = u
        max_flow += int(bottleneck)
    return max_flow


def dinic(capacity: Dict[Node, Dict[Node, int]], s: Node, t: Node) -> int:
    nodelist = list(capacity.keys())
    level: Dict[Node, int] = {}
    it: Dict[Node, int] = {}

    # build residual graph structure
    graph: Dict[Node, List[tuple[Node, int, int]]] = {u: [] for u in capacity}
    for u in capacity:
        for v, c in capacity[u].items():
            graph[u].append([v, c, len(graph.setdefault(v, []))])  # type: ignore
            graph[v].append([u, 0, len(graph[u]) - 1])  # type: ignore

    def bfs() -> bool:
        from collections import deque
        nonlocal level
        level = {u: -1 for u in graph}
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level.get(t, -1) >= 0

    def dfs(u: Node, f: int) -> int:
        if u == t:
            return f
        for i in range(it.get(u, 0), len(graph[u])):
            it[u] = i
            v, cap, rev = graph[u][i]
            if cap > 0 and level.get(v, -1) == level[u] + 1:
                d = dfs(v, min(f, cap))
                if d > 0:
                    graph[u][i][1] -= d
                    graph[v][rev][1] += d
                    return d
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it = {u: 0 for u in graph}
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            flow += pushed
    return flow
