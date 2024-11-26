# Scatter Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, color='blue', alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(alpha=0.5)
plt.show()

# Regression Plot
x = np.linspace(0, 10, 100)
y = 2 * x + np.random.randn(100) * 2 

plt.scatter(x, y, color='blue', alpha=0.5, label='Data points')
plt.plot(x, 2 * x, color='red', label='Regression Line')  
plt.title('Regression Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(alpha=0.5)
plt.show()

# Count Plot
categories = ['A', 'B', 'C', 'D', 'E']
counts = [10, 15, 7, 12, 9]

plt.bar(categories, counts, color='skyblue', edgecolor='black')
plt.title('Count Plot')
plt.xlabel('Category')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.5)
plt.show()

# Bar Plot
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
values = [20, 34, 30, 35]

plt.bar(labels, values, color='lightgreen', edgecolor='black')
plt.title('Bar Plot')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# Violin Plot
data = [np.random.normal(loc=0, scale=1, size=100),
        np.random.normal(loc=1, scale=1.5, size=100),
        np.random.normal(loc=-1, scale=0.8, size=100)]

plt.boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'))
plt.title('Violin Plot (Box Plot Approximation)')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Category 1', 'Category 2', 'Category 3'])
plt.grid(alpha=0.5)
plt.show()

# Heat Map
matrix = np.random.rand(10, 10)

plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Value')
plt.title('Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Swarm Chart
categories = ['A', 'B', 'C']
values = [np.random.rand(30) * 10 for _ in categories]

for i, (cat, val) in enumerate(zip(categories, values)):
    jitter = np.random.uniform(-0.2, 0.2, size=len(val))
    plt.scatter(np.full_like(val, i) + jitter, val, alpha=0.7, label=f'Category {cat}')

plt.xticks(range(len(categories)), categories)
plt.title('Swarm Chart Approximation')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.grid(alpha=0.5)
plt.show()


