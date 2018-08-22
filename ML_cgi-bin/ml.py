#!/usr/bin/python3
import cgi
import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.cross_validation import train_test_split
import mysql.connector
mydb = mysql.connector.connect(host="34.215.84.191",user="root",passwd="redhat",database="dell")
data=pd.read_csv('user_data.csv')
df=DataFrame(data,columns=['IssuesResolved','IssuesUnresolved','AvgTimePerResolvedIssue','RateOfIssue','TimeSpentDuringSearching','Sentiment'])

X=df[['IssuesResolved','IssuesUnresolved','AvgTimePerResolvedIssue','RateOfIssue','TimeSpentDuringSearching']].astype(float)
Y=df['Sentiment'].astype(float)

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.20)

regr=linear_model.LinearRegression()
l=regr.fit(xtrain,ytrain)

#print('Intercept: \n',regr.intercept_)
#print('Coefficients: \n', regr.coef_)

ir=10
iu=8
apri=20
roi=100
tds=10
def pre(a):
	result= regr.predict([a])
	d=int(result)
	return d
result= regr.predict([[ir,iu,apri,roi,tds]])
#print ('Predicted Sentiment: \n', pre(result))
