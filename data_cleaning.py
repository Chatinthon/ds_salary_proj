# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:05:27 2020

@author: Chatinthon
"""

import pandas as pd

df = pd.read_csv("datascience_glassdoor.csv")

#salary parsing

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['min_salary'] = minus_kd.apply(lambda x: x.split('-')[0])
df['min_salary'] = df['min_salary'].astype('int')
df['min_salary'].dtype

df['max_salary'] = minus_kd.apply(lambda x: x.split('-')[1])
df['max_salary'] = df['max_salary'].astype('int')
df['max_salary'].dtype

df['avg_salary'] = (df.min_salary + df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(",")[1] if ',' in x else (' UT' if x.lower() == 'utah' else (' CA' if x.lower() == 'california' else (' NJ' if x.lower() == 'new jersey' else (' NY' if x.lower() == 'new york state' else (' VA' if x.lower() == 'virginia' else x))))))
df.job_state.value_counts()


"""df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)"""

#age of company
df['age_of_company'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)
#parsing of job description
#df['Job Description'][0]

#python
df['python_yu'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yu.value_counts()
#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()
#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()
#SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.sql.value_counts()

df.to_csv('salary_data_cleaned.csv', index = False)