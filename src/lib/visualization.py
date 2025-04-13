from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def hello_world():
    print("Hello, world!")

def visualize_disconnected_communities(
    G,
    communities,
    color_map,
    color_by="level_1",
    title="Community Visualization"
):
    """
    Visualizes detected communities as separate disconnected subgraphs
    while optionally coloring by Level 1 or Level 2 classifications.

    Parameters:
    - G: NetworkX graph
    - communities: CDLib NodeClustering object
    - color_map: Dict for Level 1 colors (required)
    - level_2_colors: Dict for Level 2 colors (optional, required if color_by="level_2")
    - color_by: "level_1" or "level_2" (default: "level_1")
    - title: Title for the plot
    """

    if color_by not in {"level_1", "level_2"}:
        raise ValueError("color_by must be either 'level_1' or 'level_2'")

    num_communities = len(communities.communities)
    fig, ax = plt.subplots(figsize=(12, 8))

    layouts = []
    for i in range(num_communities):
        layouts.append(nx.spring_layout(G.subgraph(communities.communities[i]), seed=42))

    spacing = 3
    for i, layout in enumerate(layouts):
        for node in layout:
            layout[node] += [i * spacing, 0]

    for i, community in enumerate(communities.communities):
        valid_nodes = [node for node in community if node in G]
        if not valid_nodes:
            continue
        subG = G.subgraph(valid_nodes)
        pos = layouts[i]

        if color_by == "level_1":
            node_colors = [color_map.get(G.nodes[n]["level_1"], "#808080") for n in subG.nodes()]
        else:
            node_colors = [color_map.get(G.nodes[n]["level_2"], "#808080") for n in subG.nodes()]

        nx.draw_networkx_nodes(subG, pos, node_color=node_colors, node_size=200, alpha=1, edgecolors="black")
        nx.draw_networkx_edges(subG, pos, alpha=0.3, edge_color="black")

    # Legend
    # if color_by == "level_1":
    #     cell_cycle_phases = ["Early G1 Phase", "Late G1 Phase", "S Phase", "G2 Phase", "M Phase"]
    #     legend_handles = [Patch(color=color_map[cls], label=f'{cell_cycle_phases[cls-1]}') for cls in sorted(color_map)]
    #     legend_title = "Level 1 Classification"
    # else:
    #     legend_handles = [Patch(color=color, label=f"Level 2: {cls}") for cls, color in color_map.items()]
    #     legend_title = "Level 2 Classification"

    # plt.legend(handles=legend_handles, loc="best", fontsize=8, title=legend_title)
    plt.title(title)
    plt.axis("off")
    plt.show()

def visualize_hierarchical_communities(
    G, top_level_communities, bottom_level_communities, bottom_to_top_map, color_map,
    color_by="level_1", title="Hierarchical Community Visualization",
    spacing_x=5, spacing_y=1.5
):
    fig, ax = plt.subplots(figsize=(14, 10))
    pos_dict = {}
    top_positions = {}
    bottom_positions = {}
    top_layouts = {}

    # Bottom-level communities (row 2)
    for i, community in enumerate(bottom_level_communities):
        subG = G.subgraph(community)
        pos = nx.spring_layout(subG, seed=42)
        for node in pos:
            pos[node][0] += i * spacing_x
            pos[node][1] -= spacing_y
            pos_dict[node] = pos[node]
        bottom_positions[i] = np.mean([pos[n] for n in pos], axis=0)

        colors = [color_map.get(G.nodes[n][color_by], "#888888") for n in subG.nodes()]
        nx.draw_networkx_nodes(subG, pos, node_color=colors, node_size=120, ax=ax, edgecolors="black")
        nx.draw_networkx_edges(subG, pos, ax=ax, alpha=0.3)

    # Top-level layouts computed first (but not yet drawn)
    for i, community in enumerate(top_level_communities):
        subG = G.subgraph(community)
        pos = nx.spring_layout(subG, seed=42)
        for node in pos:
            pos[node][0] += i * spacing_x
            pos[node][1] += spacing_y
        top_layouts[i] = pos
        top_positions[i] = np.mean([pos[n] for n in pos], axis=0)

    # Center the top row over the bottom row
    top_xs = np.array([pt[0] for pt in top_positions.values()])
    bottom_xs = np.array([pt[0] for pt in bottom_positions.values()])
    x_shift = np.mean(bottom_xs) - np.mean(top_xs)

    for i, pos in top_layouts.items():
        for node in pos:
            pos[node][0] += x_shift
            pos_dict[node] = pos[node]  # update global pos_dict
        top_positions[i][0] += x_shift

    # Draw top-level communities
    for i, community in enumerate(top_level_communities):
        subG = G.subgraph(community)
        pos = top_layouts[i]
        colors = [color_map.get(G.nodes[n][color_by], "#888888") for n in subG.nodes()]
        nx.draw_networkx_nodes(subG, pos, node_color=colors, node_size=120, ax=ax, edgecolors="black")
        nx.draw_networkx_edges(subG, pos, ax=ax, alpha=0.3)
		    # Annotate top-level community sizes
    for i, community in enumerate(top_level_communities):
        if i in top_positions:
            x, y = top_positions[i]
            ax.text(
                x, y + 1.1,  # small offset above
                f"Size: {len(community)}",
                fontsize=12, ha='center', va='bottom', fontweight='bold'
            )

    # --- Draw arrows ---
    for bottom_idx, top_idx in bottom_to_top_map.items():
        if top_idx in top_positions and bottom_idx in bottom_positions:
            arrow = FancyArrowPatch(
                posA=top_positions[top_idx],
                posB=bottom_positions[bottom_idx],
                arrowstyle="->",
                color="black",
                alpha=1,
                connectionstyle="arc3,rad=0.0"
            )
            ax.add_patch(arrow)
		    # Annotate bottom-level community sizes
    for i, community in enumerate(bottom_level_communities):
        if i in bottom_positions:
            x, y = bottom_positions[i]
            ax.text(
                x, y - 1.1,  # small offset below
                f"Size: {len(community)}",
                fontsize=10, ha='center', va='top', fontweight='bold'
            )

    ax.set_title(title)
    ax.axis("off")
    plt.tight_layout()
    plt.show()
