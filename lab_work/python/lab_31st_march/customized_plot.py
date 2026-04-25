import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [2000, 3000, 2500, 4000, 3500]

plt.plot(months, revenue, marker='o', color='green')
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()