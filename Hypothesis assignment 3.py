# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:51:15 2023

@author: kailas
"""
1) Problem

DATA SET: Cutlets.csv

import pandas as pd
import matplotlib.pylab as plt
import statsmodels.stats.descriptivestats as sd
from statsmodels.stats import weightstats as stests
from scipy import stats
import pylab


#Problem Statement:-
H0:-There is no significant differnce between diameter of two cutlet unit.
H1:-There is significant differnce between diameter of two cutlet unit..


# datset to be load
data=pd.read_csv("D:/data science assignment/Assignments/Hypothesis Testing/Cutlets.csv")


#DATA CLEANING
data1=data.iloc[0:35]

FROM ABOVE PROBLEM,
WE CONCLUDE THAT DATA ARE NORMAL.


#GRAPHICAL REPRESENTATION
stats.probplot(data1['Unit B'],plot=pylab,dist='norm')
stats.probplot(data1['Unit B'],plot=pylab,dist='norm')


#CHECK VARAIENCE EQUAL OR NOT
stats.levene(data1['Unit A'],data1['Unit B'])
pvalue=0.4176162212502553>0.05

FROM ABOVE,
WE CONCLUDE THAT VARIENCE ARE EQUAL.


#SO at last WE USE:
#2 SAMPLE 'T-TEST' FOR EQUAL VARIENCE
stats.ttest_ind(data1['Unit A'],data1['Unit B'])
pval=0.4722394724599501>0.05

WE CONCLUDE THAT, 
THERE IS NO SIGNIFICANT DIFFERNCE BETWEEN DIAMETER OF TWO CUTLET UNIT 





2)Problem

DATA SET: LabTAT.csv

import pandas as pd
import scipy
from scipy import stats


#Problem Statement:
    
H0=There is NO difference in the Turn Around Time (TAT) of reports of the laboratories on their preferred list. 
H1=There is difference in the Turn Around Time (TAT) of reports of the laboratories on their preferred list. 


# DATASET
data=pd.read_csv("D:/data science assignment/Assignments/Hypothesis Testing/LabTAT.csv")
data.info()
#EDA
#Rename the columns

data=data.rename(columns={'Laboratory 1':'lab1','Laboratory 2':'lab2','Laboratory 3':'lab3','Laboratory 4':'lab4'})
data.info()

#HO=Data are Normal
#H1=Data are not Normal
#For all column Accept H0 Data are normal

#Check Varience HO=Equal Varience,H1=Not Equal Varience

stats.levene(data['lab1'],data['lab2'],data['lab3'],data['lab4'])
pvalue=0.05161343808309816>0.05
ACCEPT THAT H0


# ANOVA TEST
stats.f_oneway(data['lab1'],data['lab2'],data['lab3'],data['lab4'])
pvalue=2.1156708949992414e-57<0.05
NOT ACCEPT H0

WE CONCLUDE THAT,
H0 There are some difference in the Turn Around Time (TAT) of reports of the laboratories on their preferred of list. 




3)Problem
    
DATA SET = Buyer Ratio.csv

import pandas as pd
import scipy
from scipy import stats
from scipy.stats import chi2_contingency


#Problem Statement:-
H0:- Male and female are similar
H1:- Male and female are not similar 

# DATSET
data=pd.read_csv("D:/data science assignment/Assignments/Hypothesis Testing/BuyerRatio (1).csv")

# TABLE DATA
data1=[[50,142,131,70],[435,1523,1356,750]]

# CHI_CONTINGENCY TEST
stat,p,dof,expected=scipy.stats.chi2_contingency(data1)
pvalue= 0.6603094907091882>0.05

Hence,we accept HO
Male and Female ratio are similar across regions



4)Problem
              
DATA SET: CustomerOrderForm.mtw
              
HO=Defective varies
H1=Defective Not varies

# dataset
data=pd.read_csv("D:/data science assignment/Assignments/Hypothesis Testing/Costomer+OrderForm.csv")

#Data Organizing
India=data.India.value_counts()
Phillippines=data.Phillippines.value_counts()
Indonesia=data.Indonesia.value_counts()
Malta=data.Malta.value_counts()

#AFTER THAT DFEINING THE TABLE
data1=[[280,271,267,269],[20,29,33,31]]

#APPLY CHI2
stat,p,dof,expected = scipy.stats.chi2_contingency(data1)
pvalue=0.2771020991233135>0.05

ACCPET Defective Varies (HO)


