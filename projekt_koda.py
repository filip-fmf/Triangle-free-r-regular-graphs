import networkx as nx
import itertools

# ---------- POMOŽNE FUNKCIJE ----------

def is_triangle_free(G):
    """Preveri, ali graf nima trikotnikov."""
    return sum(nx.triangles(G).values()) == 0

def is_independent_set(G, S):
    """Preveri, ali je S neodvisna množica."""
    for u, v in itertools.combinations(S, 2):
        if G.has_edge(u, v):
            return False
    return True

def odd_independent_sets(G):
    """Vrne vse lihe neodvisne množice."""
    nodes = list(G.nodes())
    odd_sets = []

    for r in range(1, len(nodes) + 1, 2):  # samo lihe velikosti
        for subset in itertools.combinations(nodes, r):
            if is_independent_set(G, subset):
                odd_sets.append(set(subset))
    return odd_sets

def alpha_od(G):
    """Največja velikost lihe neodvisne množice."""
    odd_sets = odd_independent_sets(G)
    return max(len(S) for S in odd_sets) if odd_sets else 0

def is_maximum_odd_independent(G, S):
    """Preveri, ali je S maksimalna liha neodvisna množica."""
    S = set(S)
    size = len(S)
    for T in odd_independent_sets(G):
        if len(T) > size:
            return False
    return True

def N(G, v):
    """Sosedstvo vozlišča v."""
    return set(G.neighbors(v))

# ---------- PREVERJANJE POGOJEV ----------

def condition_i(G):
    """(i): N(v) je maksimalna močna liha neodvisna množica za vsak v."""
    for v in G.nodes():
        Nv = N(G, v)
        if len(Nv) % 2 == 0:
            return False
        if not is_independent_set(G, Nv):
            return False
        if not is_maximum_odd_independent(G, Nv):
            return False
    return True

def condition_ii(G):
    """(ii): N(v) je maksimalna močna liha neodvisna množica za vsaj en v."""
    for v in G.nodes():
        Nv = N(G, v)
        if len(Nv) % 2 == 1 and is_independent_set(G, Nv):
            if is_maximum_odd_independent(G, Nv):
                return True
    return False

def condition_iii(G, r):
    """(iii): alpha_od(G) = r"""
    return alpha_od(G) == r

# ---------- GLAVNO ISKANJE ----------

def search_graphs(n, r):
    """
    Sistematično iskanje r-regularnih grafov na n vozliščih.
    Deluje za zelo majhne n (n <= 8).
    """
    results_i = []
    results_ii = []
    results_iii = []

    nodes = list(range(n))
    possible_edges = list(itertools.combinations(nodes, 2))
    m = n * r // 2  # število povezav v r-regularnem grafu

    print(f"Iščem {r}-regularne grafe na {n} vozliščih...")

    for edges in itertools.combinations(possible_edges, m):
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        if not nx.is_connected(G):
            continue

        degrees = [d for _, d in G.degree()]
        if not all(d == r for d in degrees):
            continue

        if not is_triangle_free(G):
            continue

        if nx.diameter(G) <= 3:
            if condition_i(G):
                results_i.append(G)
            if condition_ii(G):
                results_ii.append(G)

        if condition_iii(G, r):
            results_iii.append(G)

    return results_i, results_ii, results_iii

# ---------- ZAGON PROGRAMA ----------

if __name__ == "__main__":
    n = 8
    r = 3

    res_i, res_ii, res_iii = search_graphs(n, r)

    print(f"Rezultati za n={n}, r={r}")
    print("Pogoj (i):", len(res_i), "grafov")
    print("Pogoj (ii):", len(res_ii), "grafov")
    print("Pogoj (iii):", len(res_iii), "grafov")
