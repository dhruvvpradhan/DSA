
from collections import defaultdict
class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Euler tour and parent/depth information
        tin = [0] * n
        tout = [0] * n
        parent = [-1] * n
        depth = [0] * n
        timer = 0

        # Iterative DFS avoids recursion-depth issues.
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[-1]
            up.append([
                -1 if prev[i] == -1 else prev[prev[i]]
                for i in range(n)
            ])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick Tree supporting range XOR updates and point queries.
        bit = [0] * (n + 2)

        def add(i, value):
            i += 1
            while i <= n + 1:
                bit[i] ^= value
                i += i & -i

        def range_xor(left, right, value):
            add(left, value)
            add(right + 1, value)

        def point_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def char_mask(c):
            return 1 << (ord(c) - ord('a'))

        # Initial root-to-node prefix masks
        prefix = [0] * n
        stack = [(0, -1, 0)]

        while stack:
            u, p, mask = stack.pop()
            prefix[u] = mask ^ char_mask(s[u])

            for v in graph[u]:
                if v != p:
                    stack.append((v, u, prefix[u]))

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    delta = char_mask(chars[u]) ^ char_mask(c)
                    chars[u] = c

                    # Every descendant's root-prefix mask changes.
                    range_xor(tin[u], tout[u], delta)

            else:
                u = int(parts[1])
                v = int(parts[2])

                pu = prefix[u] ^ point_query(tin[u])
                pv = prefix[v] ^ point_query(tin[v])

                w = lca(u, v)
                path_mask = pu ^ pv ^ char_mask(chars[w])

                answer.append(
                    path_mask == 0
                    or (path_mask & (path_mask - 1)) == 0
                )

        return answer
        