# src/visualizer.py

import matplotlib.pyplot as plt
import networkx as nx
import logging

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def show_graph(heroes_df, links_df):
    try:
        required_hero_cols = {"id", "name"}
        required_link_cols = {"source", "target"}

        if heroes_df.empty:
            print(" No superheroes to display in the graph.")
            return
        if links_df.empty:
            print(" No connections to display in the graph.")
            return
        if not required_hero_cols.issubset(heroes_df.columns):
            print(" Missing required columns in heroes data.")
            return
        if not required_link_cols.issubset(links_df.columns):
            print(" Missing required columns in links data.")
            return

        # Create graph
        G = nx.Graph()
        for _, row in heroes_df.iterrows():
            G.add_node(row["id"], label=row["name"])
        for _, row in links_df.iterrows():
            G.add_edge(row["source"], row["target"])

        if G.number_of_nodes() == 0:
            print(" Graph has no nodes.")
            return
        if G.number_of_edges() == 0:
            print(" Graph has no connections.")
            return

        # Prepare attributes
        labels = nx.get_node_attributes(G, "label")
        degrees = dict(G.degree())

        node_sizes = [300 + degrees[n] * 150 for n in G.nodes()]
        node_colors = ['lightcoral' if degrees[n] >= 3 else 'skyblue' for n in G.nodes()]
        edge_widths = [1.2 for _ in G.edges()]

        # Draw graph
        plt.figure(figsize=(12, 9))
        pos = nx.spring_layout(G, seed=42, k=0.5)

        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)
        nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color="gray", alpha=0.5)
        nx.draw_networkx_labels(G, pos, labels, font_size=9, font_family="sans-serif")

        plt.title(" Superhero Universe Network", fontsize=16, fontweight='bold')
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        logger.error(f"Error generating graph: {e}")
        print(" An unexpected error occurred while generating the graph. Please check logs for more details.")
