# Write a Python program to display a horizontal bar chart showing the popularity of programming languages. 
import matplotlib.pyplot as plt
import numpy as np

languages = np.array(["Java", "Python", "PHP", "JavaScript", "C#", "C++"])
popularity_lang = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])

plt.bar(languages, popularity_lang, color='skyblue')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Language')
plt.ylabel('Popularity (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()