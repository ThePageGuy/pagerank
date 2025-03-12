import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges (links between pages)
edges = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"),
    ("C", "D"), ("D", "A")
]
G.add_edges_from(edges)

# Compute PageRank
pagerank = nx.pagerank(G, alpha=0.85)

# Print results
for page, rank in pagerank.items():
    print(f"Page {page}: {rank:.4f}")
