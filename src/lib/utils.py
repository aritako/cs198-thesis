import itertools
from cdlib import algorithms, evaluation
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.metrics import rand_score
from sklearn.metrics import adjusted_rand_score

def modified_rand_score(labels_true, labels_pred, nodes_true_list, nodes_pred_list):
    """
    Compute the Modified Rand Index (MRI), an extension of the Rand Index
    that accounts for missing elements between partitions.

    Parameters
    ----------
    labels_true : list
        True labels corresponding to the nodes.
    labels_pred : list
        Predicted labels corresponding to the nodes.
    nodes_true_list : list
        An ordered list of nodes corresponding to labels_true.
    nodes_pred_list : list
        An ordered list of nodes corresponding to labels_pred.

    Returns
    -------
    mri : float
        The Modified Rand Index score.
    """

    n = len(labels_true)
    total_pairs = n * (n - 1) // 2  # All possible unique node pairs
    n_00, n_11, n_xx = 0, 0, 0  # Initialize counts

    # Convert lists to sets for fast lookup
    nodes_true_set = set(nodes_true_list)
    nodes_pred_set = set(nodes_pred_list)

    # Identify common nodes between the two partitions
    common_nodes = nodes_true_set.intersection(nodes_pred_set)

    # Iterate over all node pairs
    for i, j in itertools.combinations(range(n), 2):  # Iterate over all unique pairs
        node_i, node_j = nodes_true_list[i], nodes_true_list[j]

        # If either node is missing from the common set, count this pair as n_xx.
        if node_i not in common_nodes or node_j not in common_nodes:
            n_xx += 1
        else:
            same_true = (labels_true[i] == labels_true[j])
            same_pred = (labels_pred[i] == labels_pred[j])
            if same_true and same_pred:
                n_11 += 1  # Agreeing pair (same in both)
            elif not same_true and not same_pred:
                n_00 += 1  # Agreeing pair (different in both)

    # Compute MRI Score
    if total_pairs == 0:
        return 1.0  # Perfect match in trivial cases

    MRI = (n_00 + n_11 + n_xx) / total_pairs
    return MRI

def evaluate_level1_communities(delta, G_subgraph, communities):
    num_communities = len(communities.communities)
    largest_community_size = max(len(c) for c in communities.communities)
    community_sizes = [len(c) for c in communities.communities]
    num_singletons = sum(1 for c in communities.communities if len(c) == 1)
    modularity_score = evaluation.newman_girvan_modularity(G_subgraph, communities).score

    community_centralities = []
    for community in communities.communities:
        if len(community) > 1:
            subgraph = G_subgraph.subgraph(community)
            centralities = nx.closeness_centrality(subgraph).values()
            community_centralities.extend(centralities)
    avg_closeness_centrality = np.mean(community_centralities) if community_centralities else 0.0

    predicted_labels_dict = {node: -1 for node in G_subgraph.nodes()}
    for i, community in enumerate(communities.communities):
        for node in community:
            predicted_labels_dict[node] = i
    predicted_labels = [predicted_labels_dict[node] for node in G_subgraph.nodes()]
    true_labels = [G_subgraph.nodes[n].get("level_1") for n in G_subgraph.nodes()]

    return pd.DataFrame({
        "Level": ["L1"],
        "Delta": [delta],
        "Number of Communities": [num_communities],
        "Nodes in Largest Community": [largest_community_size],
        "Community Sizes": [community_sizes],
        "Singletons": [num_singletons],
        "Modularity": [modularity_score],
        "Closeness Centrality": [avg_closeness_centrality],
        "ARI (L1)": [adjusted_rand_score(true_labels, predicted_labels)],
        "RI (L1)": [rand_score(true_labels, predicted_labels)],
        "Communities": [communities.communities]
    })

def evaluate_level2_communities(delta, G_subgraph, communities):
    num_communities = len(communities.communities)
    largest_community_size = max(len(c) for c in communities.communities)
    community_sizes = [len(c) for c in communities.communities]
    num_singletons = sum(1 for c in communities.communities if len(c) == 1)
    modularity_score = evaluation.newman_girvan_modularity(G_subgraph, communities).score

    community_centralities = []
    for community in communities.communities:
        if len(community) > 1:
            subgraph = G_subgraph.subgraph(community)
            centralities = nx.closeness_centrality(subgraph).values()
            community_centralities.extend(centralities)
    avg_closeness_centrality = np.mean(community_centralities) if community_centralities else 0.0

    predicted_labels_dict = {node: -1 for node in G_subgraph.nodes()}
    for i, community in enumerate(communities.communities):
        for node in community:
            predicted_labels_dict[node] = i

    # Evaluate only on nodes with Level 2 annotations
    nodes_with_lvl2 = [n for n in G_subgraph.nodes() if G_subgraph.nodes[n].get("level_2") is not None]
    pred_labels = [predicted_labels_dict[n] for n in nodes_with_lvl2]
    true_labels = [G_subgraph.nodes[n]["level_2"] for n in nodes_with_lvl2]

    return pd.DataFrame({
        "Level": ["L2"],
        "Delta": [delta],
        "Number of Communities": [num_communities],
        "Nodes in Largest Community": [largest_community_size],
        "Community Sizes": [community_sizes],
        "Singletons": [num_singletons],
        "Modularity": [modularity_score],
        "Closeness Centrality": [avg_closeness_centrality],
        "ARI (L2)": [adjusted_rand_score(true_labels, pred_labels)],
        "RI (L2)": [rand_score(true_labels, pred_labels)],
        "Communities": [communities.communities]
    })

def format_results(results_df):
		"""Format the results DataFrame for better readability."""
		desired_column_order = [
            "Level",
            "Delta",
            "Number of Communities",
            "Nodes in Largest Community",
            "Community Sizes",
            "Singletons",
            "Modularity",
            "Closeness Centrality",
            "ARI (L1)",
            "RI (L1)",
            "ARI (L2)",
            "RI (L2)",
            "Communities"
		]
		available_columns = [col for col in desired_column_order if col in results_df.columns]
		return results_df[available_columns]

def generate_missing_row(algorithm, level, delta):
    missing_row = {
        "Level": level,
        "Delta": delta,
        "Number of Communities": np.nan,
        "Nodes in Largest Community": np.nan,
        "Community Sizes": np.nan,
        "Singletons": np.nan,
        "Modularity": np.nan,
        "Closeness Centrality": np.nan,
        "ARI (L1)": np.nan,
        "RI (L1)": np.nan,
        "ARI (L2)": np.nan,
        "RI (L2)": np.nan,
        "Communities": np.nan
    }
    return pd.DataFrame([missing_row])