# Capstone Project
# LendingClub
## Data Cleanup

# Data Preprocessing Template

#####################
# Importing the libraries
##import numpy as np
##import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
ds2016q1 = pd.read_csv('LoanStats_2016Q1.csv')
ds2016q2 = pd.read_csv('LoanStats_2016Q2.csv')
ds2016q3 = pd.read_csv('LoanStats_2016Q3.csv')
ds2016q4 = pd.read_csv('LoanStats_2016Q4.csv')
ds2017q1 = pd.read_csv('LoanStats_2017Q1.csv')

ds = pd.concat([ds2016q1, ds2016q2, ds2016q3, ds2016q4, ds2017q1], axis=0)

del ds2016q1, ds2016q2, ds2016q3, ds2016q4, ds2017q1

#####################
## Dataset Cleaning - Start
#####################

## drop unwanted columns - No data
ds.drop('id', axis=1, inplace=True)
ds.drop('member_id', axis=1, inplace=True)
ds.drop('url', axis=1, inplace=True)
ds.drop('desc', axis=1, inplace=True)
ds.drop('title', axis=1, inplace=True)
ds.drop('revol_bal_joint', axis=1, inplace=True)
ds.drop('sec_app_earliest_cr_line', axis=1, inplace=True)
ds.drop('sec_app_inq_last_6mths', axis=1, inplace=True)
ds.drop('sec_app_mort_acc', axis=1, inplace=True)
ds.drop('sec_app_open_acc', axis=1, inplace=True)
ds.drop('sec_app_revol_util', axis=1, inplace=True)
ds.drop('sec_app_open_il_6m', axis=1, inplace=True)
ds.drop('sec_app_num_rev_accts', axis=1, inplace=True)
ds.drop('sec_app_chargeoff_within_12_mths', axis=1, inplace=True)
ds.drop('sec_app_collections_12_mths_ex_med', axis=1, inplace=True)
ds.drop('sec_app_mths_since_last_major_derog', axis=1, inplace=True)

## drop unwanted columns - irrelevant data
ds.drop('emp_length', axis=1, inplace=True)
ds.drop('issue_d', axis=1, inplace=True)
ds.drop('pymnt_plan', axis=1, inplace=True)
ds.drop('zip_code', axis=1, inplace=True)
ds.drop('earliest_cr_line', axis=1, inplace=True)


## drop unwanted columns - irrelevant data- Need to check first
ds.drop('funded_amnt', axis=1, inplace=True) 
ds.drop('funded_amnt_inv', axis=1, inplace=True) 
ds.drop('last_pymnt_d', axis=1, inplace=True) 
ds.drop('last_credit_pull_d', axis=1, inplace=True)
ds.drop('collections_12_mths_ex_med', axis=1, inplace=True)
##ds2016q1.drop('mths_since_last_major_derog', axis=1, inplace=True)
ds.drop('policy_code', axis=1, inplace=True)
ds.drop('annual_inc_joint', axis=1, inplace=True)
ds.drop('dti_joint', axis=1, inplace=True)
ds.drop('verification_status_joint', axis=1, inplace=True)

ds.drop('emp_title', axis=1, inplace=True)  ## There are 142K unique values so decided to drop this column


## ===================================================================
# Finding Null values
len(ds[(pd.isnull(ds['loan_amnt']) == True)])  ## This one works
# If any such rows found, then delete the said rows
ds.dropna(subset=['loan_amnt'], inplace = True)

# Finding values containing 0
ds[(ds['annual_inc']==0)]
# Replace 0 with Mean annual_inc values containing 0
ds['annual_inc'].replace(0, ds['annual_inc'].mean(), inplace = True)

# Finding values containing 0 or ''
ds[(ds['dti']==0)]
# Replace 0 with Mean annual_inc values containing 0
ds['dti'].replace(0, ds['dti'].mean(), inplace = True)

# Finding Null values
len(ds[(pd.isnull(ds['inq_last_6mths']) == True)])  ## This one works
# If any such rows found, then delete the said rows
ds.dropna(subset=['inq_last_6mths'], inplace = True)

# Finding Null values
len(ds[(pd.isnull(ds['mths_since_last_delinq']) == True)])  ## This one works
# Fill any null values with some valid values. In this case mean of all the values in that column
ds['mths_since_last_delinq'].fillna(value = ds['mths_since_last_delinq'].mean(), inplace=True)

# Fill null values in column mths_since_last_record with some valid values. In this case mean of all the values in that column
ds['mths_since_last_record'].fillna(value = ds['mths_since_last_record'].mean(), inplace=True)

# Delete rows where revol_util column contains null. There are 315 rows and I can't find how to impute missing data so removed.
ds.dropna(subset=['revol_util'], inplace = True)

# Fill null values in column mths_since_last_major_derog with some valid values. In this case mean of all the values in that column as loan_status wise means are quite similar, no significant diff found
ds['mths_since_last_major_derog'].fillna(value = ds['mths_since_last_major_derog'].mean(), inplace=True)

# Fill null values in column mths_since_rcnt_il with some valid values. In this case mean of all the values in that column
ds['mths_since_rcnt_il'].fillna(value = int(ds['mths_since_rcnt_il'].mean()), inplace=True)

# Fill null values in column il_util with some valid values. In this case mean of all the values in that column
ds['il_util'].fillna(value = ds['il_util'].mean(), inplace=True)

# Fill null values in column all_util with some valid values. In this case mean of all the values in that column
ds['all_util'].fillna(value = ds['all_util'].mean(), inplace=True)

# Fill null values in column bc_open_to_buy with some valid values. In this case mean of all the values in that column
ds['bc_open_to_buy'].fillna(value = ds['bc_open_to_buy'].mean(), inplace=True)

# Fill null values in column bc_util with some valid values. In this case mean of all the values in that column
ds['bc_util'].fillna(value = ds['bc_util'].mean(), inplace=True)

# Fill null values in column mo_sin_old_il_acct with some valid values. In this case mean of all the values in that column
ds['mo_sin_old_il_acct'].fillna(value = int(ds['mo_sin_old_il_acct'].mean()), inplace=True)

# Fill null values in column mths_since_recent_bc with some valid values. In this case mean of all the values in that column
ds['mths_since_recent_bc'].fillna(value = int(ds['mths_since_recent_bc'].mean()), inplace=True)

# Fill null values in column mths_since_recent_bc_dlq with some valid values. In this case mean of all the values in that column
ds['mths_since_recent_bc_dlq'].fillna(value = int(ds['mths_since_recent_bc_dlq'].mean()), inplace=True)

# Fill null values in column mths_since_recent_inq with some valid values. In this case mean of all the values in that column
ds['mths_since_recent_inq'].fillna(value = int(ds['mths_since_recent_inq'].mean()), inplace=True)

# Fill null values in column mths_since_recent_revol_delinq with some valid values. In this case mean of all the values in that column
ds['mths_since_recent_revol_delinq'].fillna(value = int(ds['mths_since_recent_revol_delinq'].mean()), inplace=True)

# Fill null values in column num_tl_120dpd_2m with some valid values. In this case mean of all the values in that column
ds['num_tl_120dpd_2m'].fillna(value = int(ds['num_tl_120dpd_2m'].mean()), inplace=True)

# Fill null values in column percent_bc_gt_75 with some valid values. In this case mean of all the values in that column
ds['percent_bc_gt_75'].fillna(value = ds['percent_bc_gt_75'].mean(), inplace=True)

## ===================================================================

## Some More Data Cleaning 
# Removed % symbol from int_rate so that it can be used for sorting and binning properly
ds['int_rate'] = ds['int_rate'].apply(lambda numval: float(numval.strip('%')))

sds = ds[9000:90000:]  ## This is just the temp dataset. This is required to play around as the 
## main dataset is too huge to load

#####################
## Dataset Cleaning - End
#####################


#####################
## Preliminary Data Analysis starts here 
#####################
##==============================================================================

##ds.count()

alpha_color = .5

ds['term'].value_counts().plot(kind='bar', color = ['b', 'r'], alpha = alpha_color)

ds['int_rate'].value_counts().sort_index().plot(kind='bar', alpha = alpha_color)
## Int_rate vary from 3 - 35
intratebin = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
## Add a new column IntRateBin to the dataset to better analize the distribution vis a vis Interest Rates.
ds['IntRateBin'] = pd.cut(ds['int_rate'], intratebin)

ds['IntRateBin'].value_counts().sort_index().plot(kind='bar', alpha = alpha_color)

ds['grade'].value_counts().sort_index().plot(kind='bar', alpha = alpha_color)


##==============================================================================
#####################
## Preliminary Data Analysis - End
#####################





