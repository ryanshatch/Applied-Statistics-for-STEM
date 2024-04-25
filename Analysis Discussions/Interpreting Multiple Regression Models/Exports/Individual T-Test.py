# %% [markdown]
# <hr>
# 
# # <center>**Multiple Regression**</center>
# 
# <hr>

# %% [markdown]
# <center>
# 
# ## **Generating cars dataset**
# the data set will be imported from a CSV file. To make the data unique, a random sample of size 30, without replacement, will be drawn from the data in the CSV file, and the data set will then be saved into a dataframe.
# 
# </center>

# %%
import pandas as pd
from IPython.display import display, HTML

# read data from mtcars.csv data set.
cars_df_orig = pd.read_csv("https://s3-us-west-2.amazonaws.com/data-analytics.zybooks.com/mtcars.csv")

# randomly pick 30 observations from the data set to make the data set unique to you.
cars_df = cars_df_orig.sample(n=30, replace=False)

# print only the first five observations in the dataset.
print("Cars data frame (showing only the first five observations)\n")
display(HTML(cars_df.head().to_html()))

# %% [markdown]
# <hr>

# %% [markdown]
# <center>
# 
# ## **Scatterplot of miles per gallon against weight**
# scatterplot of the variables ```miles per gallon``` (mpg) and ```weight``` of the car (wt).<br><br>The plot will be saved as a PNG file.
# 
# </center>

# %%
import matplotlib.pyplot as plt

# create scatterplot of variables mpg against wt.
plt.plot(cars_df["wt"], cars_df["mpg"], 'o', color='red')

# set a title for the plot, x-axis, and y-axis.
plt.title('MPG against Weight')
plt.xlabel('Weight (1000s lbs)')
plt.ylabel('MPG')

# show the plot.
plt.show()

# %% [markdown]
# <hr> 

# %% [markdown]
# <center>
# 
# ## **Scatterplot of miles per gallon against horsepower**
# Scatterplot of the variables ```miles per gallon``` (mpg) and ```horsepower``` of the car (hp). 
# 
# </center>

# %%
import matplotlib.pyplot as plt

# create scatterplot of variables mpg against hp.
plt.plot(cars_df["hp"], cars_df["mpg"], 'o', color='blue')

# set a title for the plot, x-axis, and y-axis.
plt.title('MPG against Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('MPG')

# show the plot.
plt.show()

# %% [markdown]
# <hr> 

# %% [markdown]
# <center>
# 
# ## **Correlation matrix for miles per gallon, weight and horsepower**
# calculate the correlation coefficient between the variables ```miles per gallon``` and ```weight```. Also calculating the correlation coefficient between the variables ```miles per gallon``` and ```horsepower```.<br><br>The **corr** method of a dataframe returns the correlation matrix with the correlation coefficients between all variables in the dataframe.
# 
# </center>

# %%
# create correlation matrix for mpg, wt, and hp. 
# The correlation coefficient between mpg and wt is contained in the cell for mpg row and wt column (or wt row and mpg column).
# The correlation coefficient between mpg and hp is contained in the cell for mpg row and hp column (or hp row and mpg column).
mpg_wt_corr = cars_df[['mpg','wt','hp']].corr()
print(mpg_wt_corr)

# %% [markdown]
# <hr> 

# %% [markdown]
# <center>
# 
# ## **Multiple regression model to predict miles per gallon using weight and horsepower**
# 
# multiple regression model with ```miles per gallon``` as the response variable, and ```weight``` and ```horsepower``` as predictor variables.<br><br>The **ols** method in statsmodels.formula.api submodule returns all statistics for this multiple regression model. 
# 
# </center>

# %%
from statsmodels.formula.api import ols

# create the multiple regression model with mpg as the response variable; weight and horsepower as predictor variables.
model = ols('mpg ~ wt+hp', data=cars_df).fit()
print(model.summary())

# %% [markdown]
# <hr>
# 
# # <center>**End of Analysis**</center>

# %% [markdown]
# <hr>


