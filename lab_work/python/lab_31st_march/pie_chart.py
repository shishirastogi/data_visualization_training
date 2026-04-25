import matplotlib.pyplot as plt
categories = ['Category 1', 'Category 2', 'Category 3']
values = [30, 50, 20]

plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.show()