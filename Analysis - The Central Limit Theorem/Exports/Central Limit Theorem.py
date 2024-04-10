import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# using gamma distribution to randomly generate 500 observations.
shape, scale = 1.95, 2.5
tpcp = 100*np.random.gamma(shape, scale, 500)
# pandas library can be used to convert the array into a dataframe with the column name TPCP.
tpcp_df = pd.DataFrame(tpcp, columns=['TPCP'])
tpcp_df = tpcp_df.round(0)
# print the dataframe to see the first 5 and last 5 observations (note that the index of dataframe starts at 0)
print("TPCP data frame\n")
print(tpcp_df)

# create a figure for the plot.
fig, ax = plt.subplots()
# a histogram plot with 50 bins of TPCP population data.
plt.hist(tpcp_df['TPCP'], bins=50)
# setting a title for the plot, x-axis and y-axis
plt.title('TPCP population distribution', fontsize=20)
ax.set_xlabel('TPCP')
ax.set_ylabel('Frequency')
# show the plot
plt.show()

# the population mean
pop_mean = tpcp_df['TPCP'].mean()
print("Population mean =",pop_mean)

# using sample method of the dataframe to select a random sample, with replacement, of size 50.
tpcp_sample_df = tpcp_df.sample(50, replace=True)
# the sample mean
sample_mean = tpcp_sample_df['TPCP'].mean()
print("Sample mean =",sample_mean)

# A for loop will be used to repeat step 4 a thousand times. A python list called means_list can be used to save each mean
means_list = []
for i in range(1000):
    tpcp_sample_df = tpcp_df.sample(50, replace=True)
    sample_mean = tpcp_sample_df['TPCP'].mean()
    means_list.append(sample_mean)

# creating a python dataframe of means
means_df = pd.DataFrame(means_list, columns=['means'])
print("Dataframe of 1000 means\n")
print(means_df)

# create a figure for the plot.
fig, ax = plt.subplots()
# a histogram plot with 50 bins of 1000 means.
plt.hist(means_df['means'], bins=50)
# setting a title for the plot, x-axis and y-axis
plt.title('Distribution of 1000 sample means', fontsize=20) # title
ax.set_xlabel('Means')
ax.set_ylabel('Frequency')
# show the plot
plt.show()

# calculate the mean and standard deviation of the 1000 sample means
mean1000 = means_df['means'].mean()
std1000 = means_df['means'].std()
print("Grand mean (mean of 1000 sample means) =",mean1000)
print("Std Deviation of 1000 sample means =",std1000)