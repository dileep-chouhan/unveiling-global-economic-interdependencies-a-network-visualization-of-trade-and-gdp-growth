import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# --- 1. Synthetic Data Generation ---
# Number of countries
num_countries = 20
# Generate random GDP growth rates
gdp_growth = np.random.uniform(0.01, 0.05, num_countries)
# Generate random trade flows (adjacency matrix)
trade_flows = np.random.randint(0, 100, size=(num_countries, num_countries))
# Ensure diagonal is 0 (no self-trade)
np.fill_diagonal(trade_flows, 0)
# Make it symmetric to represent bilateral trade
trade_flows = np.triu(trade_flows) + np.triu(trade_flows, 1).T
# Create a Pandas DataFrame for easier handling
countries = [f"Country {i+1}" for i in range(num_countries)]
gdp_df = pd.DataFrame({'Country': countries, 'GDP Growth': gdp_growth})
trade_df = pd.DataFrame(trade_flows, index=countries, columns=countries)
# --- 2. Analysis ---
# Calculate correlation between GDP growth and trade flows (simplified example)
# In a real-world scenario, more sophisticated correlation analysis would be needed.
correlations = trade_df.corrwith(gdp_df['GDP Growth'])
# --- 3. Visualization ---
# Create a network graph using NetworkX
graph = nx.from_numpy_array(trade_flows)
nx.set_node_attributes(graph, dict(zip(range(num_countries), countries)))
nx.set_edge_attributes(graph, {(i,j): {'weight':trade_flows[i,j]} for i in range(num_countries) for j in range(num_countries) if trade_flows[i,j]>0})
# Draw the graph with node sizes reflecting GDP growth
node_sizes = [g * 1000 for g in gdp_growth] # Scale GDP growth for visualization
pos = nx.spring_layout(graph) #Layout algorithm
plt.figure(figsize=(12, 12))
nx.draw(graph, pos, with_labels=True, node_size=node_sizes, node_color=gdp_growth, cmap=plt.cm.viridis, width=[e[2]['weight']/10 for e in graph.edges(data=True)])
plt.title('Global Economic Interdependencies')
plt.colorbar(label='GDP Growth')
plt.savefig('economic_network.png')
print("Plot saved to economic_network.png")
#Further analysis and visualization could include:
# - Community detection to identify clusters of economically linked countries.
# - Centrality measures to identify key players in the global economy.
# - Interactive visualization using libraries like Plotly.