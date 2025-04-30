
'''import geopandas as gpd
import matplotlib.pyplot as plt

# Load the world map dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Generate a colorful visualization
# Assign a column to color countries differently (e.g., population or random color)
world['color'] = world.index % 10  # Using modulo for simple color variety

# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(column='color', cmap='tab10', legend=True, ax=ax)

# Customize the visualization
ax.set_title("World Map Visualization", fontsize=16)
ax.set_axis_off()

# Show the plot
plt.show()


my_list = [10, 20, 30]
print("Original List:", my_list)
my_list[1] = 25  # Modifying an element
print("Modified List:", my_list)
'''

my_tuple = (10, 20, 30)
print("\nOriginal Tuple:", my_tuple)
#my_tuple[1] = 25  # Uncommenting this will cause an error, as tuples are immutable
