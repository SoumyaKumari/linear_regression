# linear_regression
A simple way to understand how a linear regression works without using any library
Here, I have taken predefined inputs of x and y in array format and plotted graph showing our prediction line. 
I've also shown how does prediction works for a single point if you specify value of x.
Packages to install - numpy and matplotlib.
You can also directly import a csv file. Just write -  
 import pandas as pd
  data = pd.read_csv('filename.csv')
  x = data.iloc[: , 0]
  y = data.iloc[: , 1]
  x = np.array(x)
  y = np.array(y)
