import matplotlib.pyplot as plt
left=[1,2,3,4,5]
height=[10,20,30,40,800]
tick_label=['one','two','three','four','five']
plt.bar(left, height, tick_label= tick_label, width=1.2,color=['black','red'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My Bar Chart')
plt.show()

