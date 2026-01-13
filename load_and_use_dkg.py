import csv
import networkx as nx

def load_dkg(triple_file):
    G = nx.MultiDiGraph()
    with open(triple_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            h = row['head']
            t = row['tail']
            r = row['relation']
            G.add_node(h, type=row['head_type'])
            G.add_node(t, type=row['tail_type'])
            G.add_edge(h, t, relation=r)
    return G

if __name__ == "__main__":
    graph = load_dkg("data/dkg_triples.csv")
    print(f"Nodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}")
