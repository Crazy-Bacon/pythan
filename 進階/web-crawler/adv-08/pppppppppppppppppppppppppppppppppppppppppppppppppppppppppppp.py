import matplotlib.pyplot as plt

listx = [1, 2, 3, 4, 5, 6]
listy = [20, 30, 37, 21, 33, 40]

fig, ax = plt.subplots()
ax.plot(listx, listy)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_title('My Title')
plt.show()