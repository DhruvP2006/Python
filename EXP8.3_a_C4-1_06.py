# Write Python programming to display a bar chart of the popularity of programming Languages. Also, draw a Pie chart for popularity Data values.
import matplotlib.pyplot as plt
import numpy as np

languages = np.array(["Java", "Python", "PHP", "JavaScript", "C#", "C++"])
popularity_lang = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])

data_types = np.array(['Integer', 'String', 'Float', 'Boolean', 'List/Array'])
popularity_types = np.array([30, 25, 20, 15, 10])

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(languages, popularity_lang, color='skyblue')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Language')
plt.ylabel('Popularity (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
plt.pie(popularity_types, labels=data_types, colors=['red', 'blue', 'green', 'orange', 'pink'])
plt.title('Popularity of Data Types')

plt.tight_layout()  
plt.show()