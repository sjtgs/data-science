#simple plot application
import matplotlib.pyplot as plt

#create a list of year
year = [1994 , 1995, 1996,1997 , 1998, 1999,2000,2001, 2002, 2003,2004,2005,2006,2007,2008,2009,2010,2011, 2012, 2020]
#create a list of age
age = [1, 2, 3, 5, 6, 7 , 8, 9 , 10, 11 , 12, 13, 14 , 15, 16, 17, 18, 19, 20]

#assign what to plot
plt.plot(year,age)

# Display the plot with plt.show()
plt.show()
