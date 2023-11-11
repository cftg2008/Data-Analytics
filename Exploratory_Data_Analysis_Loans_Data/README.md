## ProsperLoanData Exploration <h2>

### Overview <h3>

In this project, we are going to approach the ProsperLoanData dataset with Exploratory Data Analysi (EDA) techniques. The dataset contains loans and related information, including loan amount, interest rate, income range, and other details. After data wrangling, a subset of the dataset was created and included as part of the final submission. 

## Summary of Findings <h3>

In the exploration step, we found there were varying degree of impacts on the outcomes of a loan by different features we were interested in.

We found BorrowerAPR is positively correlated to Loan Status when it is in the Past Due/Chargedoff/Defaulted stages. Borrowers have to pay more when the lender decided a loan's condition was deteriorating and needed to manage risks accordingly. The other variables also appear to have some effects on a loan's status. In comparison with different types of borrower, the lender clearly has offered better incentives to those Employed borrowers. Employed is one of the the JobStatus (EmploymentStatus) categories. The lender gives bigger loan amounts at lower APR rates to the Employed ones. In turn, those Employed borrowers have the largest share of keeping Loan Status Current rather than in declining status. This track record perhaps is the reason the lender offers more favorable terms to those Employed borrowers. ProsperRating is another variable that shows correlation with Loan Status somewhat, at least for some individual values. For instance, Defaulted percentage goes up when the ProsperRating moves from high rating to lower grades. Meanwhile, the highest ProsperRating AA grade had the largest Completed percentage of Loan Status while other grades did not display comparable bents. The Term feature appears to have some impacts on a loan's outcome, depending on certain values. As an example, Past Due or Chargedoff have higher APR across 12- to 60-month Terms. 

Loan Original Amount is a feature that did not show an obvious relationship with the Loan Status variable. Even though there were some interesting interactions between features, like Default had larger amount than the Completed ones or the Current type had the largest loan sizes out of all other categories. IncomeRange is another feature that did not display direct relationship with the outcome of a loan. When we looked at this variable in combination with another feature JobStatus, however, we found Full-time/Self-employed borrowers can get better APR rates with larger loan sizes when they reached a certain income bracket.

## Key Insights for Presentation

For the presentation, I'll focus on those features that appear to have more influences in the outcomes of a loan. I start by introducing the BorrowerAPR, followed by JobStatus, then succeeded by showing ProsperRating and Term features interactions. 

Afterwards, variables with lesser impacts would be discussed. Example likes Loan Original Amount exhibits no direct correlation with Loan Status but display some interesting results after interactions with other variables.
