# CS 198/199: Predicting Functional Groups of Genes Through Hierarchical and Dynamic Community Detection using Gene Co-expression Networks of Saccharomyces cerevisiae
Authors: Carmelo Ellezandro R. Atienza and Calvin James T. Maximo\
Adviser: Jhoirene B. Clemente

## How to run the code
1) Install Python `>= 3.12`.
2) Clone the repository using `git clone`.
3) Navigate to the `src` folder in your favorite IDE.
4) Open the `cho-170_network.ipynb` and/or `cho-384_network.ipynb` Jupyter Notebooks.
5) Run all the code starting from the `Import Dependencies` heading in both files.

## Required Dependencies/Libraries
The project requires the following dependencies/libraries:
* cdlib
* scikit-learn
* numpy
* pandas
* plotly
* hvplot
* community
* python-louvain
* networkx
* seaborn
* matplotlib

## Brief Description of File Structure and Purpose

```
├── README.md
├── classifications
│   ├── atienza_maximo
│   │   ├── kegg_classifications.csv
│   │   └── kegg_definitions.csv
│   └── ventures_calderon
│       └── for_groupings.xlsx
├── dataset
│   ├── cho-170
│   │   └── cho-170.txt
│   └── cho-384
│       └── cho-384.txt
├── literature
│   ├── Calderon and Ventures 2024.pdf
│   └── Clemente 2022.pdf
├── proposal
│   ├── final
│   │   ├── Atienza_Maximo_proposal_draftfinal.pdf
│   │   └── Atienza_Maximo_proposal_slidesfinal.pdf
│   ├── v1
│   │   ├── Atienza_Maximo_proposal_draft.pdf
│   │   └── Atienza_Maximo_proposal_slides.pdf
│   ├── v2
│   │   └── Atienza_Maximo_cs198cs199_v2.pdf
│   └── v3
│       ├── Atienza_Maximo_proposal_draftv3.pdf
│       ├── Atienza_Maximo_proposal_slidesv3.pdf
│       └── Atienza_Maximo_proposalv3.zip
├── results
│   ├── best_performing
│   │   └── best_results_per_delta.xlsx
│   ├── cho-170
│   │   ├── ari_vs_ri
│   │   │   ├── cho-170_ari_vs_ri_L1_0.15.png
│   │   │   ├── cho-170_ari_vs_ri_L1_0.5.png
│   │   │   ├── cho-170_ari_vs_ri_L1_0.85.png
│   │   │   ├── cho-170_ari_vs_ri_L2_0.15.png
│   │   │   ├── cho-170_ari_vs_ri_L2_0.5.png
│   │   │   └── cho-170_ari_vs_ri_L2_0.85.png
│   │   ├── community_detection_results
│   │   │   └── level2_cd_results.csv
│   │   ├── community_detection_results_by_delta
│   │   │   ├── cho-170_cd_results_delta_0.15.csv
│   │   │   ├── cho-170_cd_results_delta_0.50.csv
│   │   │   └── cho-170_cd_results_delta_0.85.csv
│   │   ├── graph_properties.csv
│   │   └── visualization
│   │       ├── cho-170_gcn_L1_0.15.png
│   │       ├── cho-170_gcn_L1_0.5.png
│   │       ├── cho-170_gcn_L1_0.85.png
│   │       ├── cho-170_gcn_L2_0.15.png
│   │       ├── cho-170_gcn_L2_0.5.png
│   │       ├── cho-170_gcn_L2_0.85.png
│   │       ├── cho-170_gn_0.15.png
│   │       ├── cho-170_gn_0.5.png
│   │       ├── cho-170_gn_0.85.png
│   │       ├── cho-170_infomap_0.15.png
│   │       ├── cho-170_infomap_0.5.png
│   │       ├── cho-170_infomap_0.85.png
│   │       ├── cho-170_lfm_0.15.png
│   │       ├── cho-170_lfm_0.5.png
│   │       ├── cho-170_lfm_0.85.png
│   │       ├── cho-170_paris_0.15.png
│   │       ├── cho-170_paris_0.5.png
│   │       ├── cho-170_paris_0.85.png
│   │       ├── cho-170_spinglass_0.15.png
│   │       ├── cho-170_spinglass_0.5.png
│   │       ├── cho-170_spinglass_0.85.png
│   │       ├── cho-170_walktrap_0.15.png
│   │       ├── cho-170_walktrap_0.5.png
│   │       ├── cho-170_walktrap_0.85.png
│   │       └── data_distribution.png
│   └── cho-384
│       ├── ari_vs_ri
│       │   ├── cho-384_ari_vs_ri_L1_0.15.png
│       │   ├── cho-384_ari_vs_ri_L1_0.5.png
│       │   ├── cho-384_ari_vs_ri_L1_0.85.png
│       │   ├── cho-384_ari_vs_ri_L2_0.15.png
│       │   ├── cho-384_ari_vs_ri_L2_0.5.png
│       │   └── cho-384_ari_vs_ri_L2_0.85.png
│       ├── community_detection_results_by_delta
│       │   ├── cho-384_cd_results_delta_0.15.csv
│       │   ├── cho-384_cd_results_delta_0.50.csv
│       │   └── cho-384_cd_results_delta_0.85.csv
│       ├── graph_properties.csv
│       └── visualization
│           ├── cho-384_gcn_L1_0.15.png
│           ├── cho-384_gcn_L1_0.5.png
│           ├── cho-384_gcn_L1_0.85.png
│           ├── cho-384_gcn_L2_0.15.png
│           ├── cho-384_gcn_L2_0.5.png
│           ├── cho-384_gcn_L2_0.85.png
│           ├── cho-384_gn_0.5.png
│           ├── cho-384_gn_0.85.png
│           ├── cho-384_infomap_0.15.png
│           ├── cho-384_infomap_0.5.png
│           ├── cho-384_infomap_0.85.png
│           ├── cho-384_lfm_0.15.png
│           ├── cho-384_lfm_0.5.png
│           ├── cho-384_lfm_0.85.png
│           ├── cho-384_paris_0.15.png
│           ├── cho-384_paris_0.5.png
│           ├── cho-384_paris_0.85.png
│           ├── cho-384_spinglass_0.15.png
│           ├── cho-384_spinglass_0.5.png
│           ├── cho-384_spinglass_0.85.png
│           ├── cho-384_walktrap_0.15.png
│           ├── cho-384_walktrap_0.5.png
│           ├── cho-384_walktrap_0.85.png
│           └── data_distribution.png
└── src
    ├── cho-170_network.ipynb
    ├── cho-384_network.ipynb
    ├── cho_network.ipynb
    ├── data_exploration.ipynb
    ├── lib
    │   ├── __pycache__
    │   │   ├── utils.cpython-312.pyc
    │   │   └── visualization.cpython-312.pyc
    │   ├── utils.py
    │   └── visualization.py
    └── statistical_analysis
        ├── cho-170_statistical_analysis.ipynb
        └── cho-384_statistical_analysis.ipynb

```

### 🧬 `classifications/`
Stores reference classification files for gene function annotations.
- `atienza_maximo/`: Custom KEGG-derived classifications and definitions.
- `ventures_calderon/`: Groupings used in Calderon & Ventures' study.

---

### 📊 `dataset/`
Raw gene expression datasets used in analysis.
- `cho-170/`: Level 2 gene expression data (subset of 170 genes).
- `cho-384/`: Level 1 gene expression data (full 384-gene set).

---

### 📚 `literature/`
Contains the main literature used throughout the thesis.
- `Calderon and Ventures 2024.pdf`
- `Clemente 2022.pdf`

---

### 📝 `proposal/`
Stores proposal drafts and slides across versions.
- `final/`, `v1/`, `v2/`, `v3/`: Tracks evolution of the thesis proposal and presentation decks.

---

### 📁 `results/`
Contains all experiment outputs and visualizations.

- `best_performing/`: Summary of best results per delta threshold.
- `cho-170/`, `cho-384/`: Results for each dataset, each with:
  - `ari_vs_ri/`: ARI and RI bar plots across deltas.
  - `community_detection_results/`: CSV outputs of clustering results.
  - `community_detection_results_by_delta/`: Fine-grained result breakdowns per delta.
  - `graph_properties.csv`: Graph statistics like density, clustering coefficient, etc.
  - `visualization/`: Network and community visualizations (per method and delta).

---

### 🧪 `src/`
Core notebooks and utility scripts for analysis.

- Main notebooks:
  - `cho-170_network.ipynb`, `cho-384_network.ipynb`: GCN construction and CD for respective datasets.
  - `data_exploration.ipynb`: Preliminary exploration and sanity checks.

- `lib/`: Python utility modules.
  - `utils.py`: Helper functions for graph construction and evaluation.
  - `visualization.py`: Graph plotting utilities.

- `statistical_analysis/`: Regression and metric analysis.
  - `cho-170_statistical_analysis.ipynb`
  - `cho-384_statistical_analysis.ipynb`


## Scripts for Data Preprocessing, Evaluation, and Visualization
This section outlines the main scripts and notebooks used throughout the pipeline:

### 📦 Data Preprocessing
- `src/data_exploration.ipynb`: Initial inspection of the Cho datasets, normalization checks, and verification of class distributions.
- `lib/utils.py`: Contains helper functions for Pearson correlation, value-based thresholding, singleton removal, and graph construction.

### 🧪 GCN Construction and Community Detection
- `src/cho-170_network.ipynb`: Constructs GCNs from Cho-170 dataset at multiple delta thresholds and applies community detection algorithms.
- `src/cho-384_network.ipynb`: Same process applied to the Cho-384 dataset.
- `src/cho_network.ipynb`: Optional integrated notebook for testing and comparing both datasets.
- Algorithms used: Paris, LFM, Girvan-Newman (Hierarchical); Infomap, Walktrap, Spinglass (Dynamic).

### 📊 Evaluation and Metrics
- Evaluation of Communities via ARI and RI
  - `src/cho-170_network.ipynb`: Contains the ARI and RI results for Cho-170
  - `src/cho-384_network.ipynb`: Same evaluation but for the Cho-384 dataset.
- Statistical Analysis (Not used in our manuscript)
  - `src/statistical_analysis/cho-170_statistical_analysis.ipynb`: Performs regression analysis on clustering metrics and ARI/RI scores for Cho-170.
  - `src/statistical_analysis/cho-384_statistical_analysis.ipynb`: Similar evaluation applied to Cho-384 results.
  - Evaluated using: Adjusted Rand Index (ARI), Rand Index (RI), modularity, closeness centrality, and graph-level properties.

### 🎨 Visualization
- `lib/visualization.py`: Contains reusable functions for visualizing GCNs, communities, and metric bar charts.
- Visual outputs stored in `results/<dataset>/visualization/`, including:
  - GCN plots for each delta and level (e.g., `cho-170_gcn_L1_0.15.png`)
  - Community plots per algorithm (e.g., `cho-384_infomap_0.85.png`)
  - Comparative metric plots (e.g., ARI vs RI bar plots)
- Visualization functions are invoked in `src/cho-170_network.ipynb` and `src/cho-384_network.ipynb`

## Configuration Files (e.g., .json, .yaml, .ini) for Reproducibility
No configuration files are relevant for the code used in our study. Please refer to the versions used in our Jupyter Notebook!


