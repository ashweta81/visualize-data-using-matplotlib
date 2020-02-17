# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)

# Plot a bar chart to compare the number of male and female candidates in the election
MFC =candidate_2009['Candidate_Sex'].value_counts()
plt.figure(figsize=(10,10))
plt.xlabel('Candidate Sex')
plt.title('Number of Male and Female Candidates')
MFC.plot(kind='bar')
# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
CA = candidate_2009['Candidate_Age']
plt.figure(figsize=(10,10))
plt.xlabel('Candidate Age')
plt.title('Distribution of Age of all Candidates')
CA.hist(bins=20)

WA = candidate_2009[candidate_2009['Position']== 1]['Candidate_Age']
plt.figure(figsize=(10,10))
plt.xlabel('Winners Age')
plt.title('Distribution of Age of Winners')
WA.hist(bins=20)

# Plot a bar graph to get the vote shares of different parties
SP = candidate_2009['Party_Abbreviation'].value_counts(normalize=True).head(10)
plt.figure(figsize=(20,10))
plt.title('Vote Share of Different Parties')
SP.plot(kind='bar')

# Plot a barplot to compare the mean poll percentage of all the states
MPP = electors_2009.groupby('STATE').agg({'POLL PERCENTAGE':'mean'}).sort_values(by='POLL PERCENTAGE', ascending= False)
plt.figure(figsize=(20,10))
plt.title('Mean Poll Percentage of All States')
MPP.plot(kind='bar')

# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh
UPR = candidate_2009[(candidate_2009['State_name']=='Uttar Pradesh') & (candidate_2009['Position']==1)]['Party_Abbreviation'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(20,10))
plt.title('Seats won by parties in UP')
UPR.plot(kind='bar')

# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
GS = candidate_2009[(candidate_2009['Position']==1 ) & (candidate_2009['State_name']=='Gujarat')]['Alliance'].value_counts()
MS = candidate_2009[(candidate_2009['Position']==1 ) & (candidate_2009['State_name']=='Maharashtra')]['Alliance'].value_counts()
MPS = candidate_2009[(candidate_2009['Position']==1 ) & (candidate_2009['State_name']=='Madhya Pradesh')]['Alliance'].value_counts()
states = ['Gujarat','Maharashtra','Madhya Pradesh']


# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka


# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
TV = electors_2009[electors_2009['Total voters']<100000][['PARLIAMENTARY CONSTITUENCY','Total voters']]
plt.figure(figsize=(10,10))
TV.plot(kind='barh')
# Plot a pie chart with the top 10 parties with majority seats in the elections

# Plot a pie diagram for top 9 states with most number of seats


