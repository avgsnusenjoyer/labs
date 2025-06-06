import networkx as nx
import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from main import build_graph, compute_mst_and_stats

def test_mst_properties():
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 2),
        ('C', 'D', 4),
        ('D', 'E', 2),
        ('C', 'E', 5)
    ]
    G = build_graph(edges)
    results = compute_mst_and_stats(G)
    mst = results["mst"]
    
    assert len(mst.nodes) == len(G.nodes), "MST має містити всі вузли"
    assert len(mst.edges) == len(G.nodes) - 1, "MST повинно мати n-1 ребро"
    assert results["mst_length"] <= results["original_length"], "MST довше за оригінал"

    print("MST проходить всі тести")

if __name__ == "__main__":
    test_mst_properties()
