## Capstone Project - Customer Churn Analysis <h2>

## Overview <h3>
- This project is based on a bank's credit card data. And the bank's management is concerned that many customers are leaving its card services.
- The bank would like you to analyze the data for them, so as to figure out why customers are leaving, and to come up with recommendations for how the bank can alleviate the outflow. Lastly, the bank would like to implement these measures so that their customers are happy to stay put.   


## Technologies Used <h3>
This project is to demonstrate many of the skills learned in the Masterschool Data Analytics program:
- PostgreSQL
- Tableau
- Python
- Deep-dive Analysis


## Datasets <h3>
Three datasets are provided (full list of attributes are embedded in the Jupyter Notebook):
- BankChurners.csv: this file contains basic information about each client.
- Basic_client_info.csv: this file contains some basic client info per each client.
- Enriched_churn_data.csv: this file contains some enriched data about each client.
- A full ERD to depict the relationships among attributes and datasets.


## SQL Analysis <h3>
Based on the SQL analysis results, the bank intends to create a dedicated campaign and target these specific clients moving forward. This step helps the bank to find these clients. Specifically, the bank needs to get answers from the following questions.
- How many clients does the bank have and are above the age of 50?
- What’s the distribution (in %) between male and female clients?
- Find out these values: Churn_rate (in %), Average Total_Relationship_Count, Minimum value of Total_Amt_Chng_Q4_Q1, Count of customers
- Out of the male clients, who holds the “blue” card, how many (in %) hold the income category 40K - 60K?
- Without the usage of group by at all, find the 3rd and 4th highest client IDs (CLIENTNUM’s) of Total_Amt_Chng_Q4_Q1?
- Which client (CLIENTNUM) has the 2nd highest Total_Trans_Amt, Per each Marital_Status?


## Tableau Analysis <h3>
This dashboard helps the bank to identify below trends and patterns through graphical representations. 
- Multiple KPIs
- Churn Rate by Credit Limit and Income Category
- Compare Total Transaction Amount and Total Transaction Count for Churned and Existing Customers
- Churn Rate by Number of Products per Customer
- Churn Rate by Age Groups  
- Churn Rate by Income Category and Education Level
[Link to Dashboard - Customer Churn Analysis](https://public.tableau.com/views/proj2_16761751070630/CustomerChurnAnalysis?:language=en-US&:display_count=n&:origin=viz_share_link)

## Deep Dive Analysis <h3>
By applying various features of Python, this step executes the following tasks to determine if conclusive answers could be uncovered:
- Summary Statistics
- Data Cleaning
- Distribution Analysis for each attribute
- Cross-Correlation Analysis
- Raising Data Questions
- Data Enrichment 

## Recommendations
Per insights gathered in early analysis, a written description on specific steps the bank's management can take to lessen the customer churn.
