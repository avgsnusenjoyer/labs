import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('A', 'B', 4),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 2),
    ('C', 'D', 4),
    ('D', 'E', 2),
    ('C', 'E', 5)
]

def build_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G

def compute_mst_and_stats(G):
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    total_weight = lambda g: sum(d['weight'] for _, _, d in g.edges(data=True))
    return {
        "mst": mst,
        "original_length": total_weight(G),
        "mst_length": total_weight(mst),
    }

def draw_graph(G, title, highlight_edges=None):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, width=3, edge_color='red')
    plt.title(title)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    G = build_graph(edges)
    results = compute_mst_and_stats(G)
    mst = results["mst"]

    print("📊 Результати аналізу мережі:")
    print(f"🔹 Кількість колодязів: {G.number_of_nodes()}")
    print(f"🔹 Загальна довжина всіх з'єднань: {results['original_length']} м")
    print(f"🔹 Мінімальна довжина резервного з'єднання (MST): {results['mst_length']} м")
    print(f"🔹 Зекономлено кабелю: {results['original_length'] - results['mst_length']} м")
    print("\n🔍 Ребра MST:")
    for u, v, d in mst.edges(data=True):
        print(f"  {u} — {v}: {d['weight']} м")

    draw_graph(G, "Повний граф")
    draw_graph(G, "MST (резервні з'єднання)", highlight_edges=mst.edges(data=False))