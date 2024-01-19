import pandas as pd
import numpy as numpy
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

# Provide the full path to the CSV file
file_path = r'C:\Users\hinaa\Documents\Data Analyst\DataAnalysisUsingPythonproject\ScreenTimeAnalysis\Screentime-App-Details.csv'

# Read the CSV file
data = pd.read_csv(file_path)
print(data.head())

# Show the null values
print("______________________________")
print("Show the null values ")
print (data.isnull().sum()) 

#Show the description of data 
print("_______________________________")
print("Description of data")
print(data.describe())


#Show the usage of mobile app using bar chart
print("__________")
print(" Usage of Mobile App")
figure=px.bar(data_frame=data,x='Date',y='Usage',color='App',title='Usage of Mobile App')
figure.show()



#Show the notification  of mobile app using bar chart
print("__________")
print("Notification from Mobile App")
figure=px.bar(data_frame=data,x='Date',y='Notifications',color='App',title='Notifications from mobile app')
figure.show()

#Show the notification  of mobile app using bar chart
print("__________")
print("Time Opened  of Mobile App")
figure=px.bar(data_frame=data,x='Date',y='Times opened',color='App',title='Time Opened ')
figure.show()

#Show the relationship between notification and amount of usage
print("__________")
print("Number of Notification And Amount of usage")
figure=px.scatter(data_frame=data,x='Notifications',y='Usage',size='Notifications',title='Number of Notification And Amount of usag',trendline="ols")
figure.show()