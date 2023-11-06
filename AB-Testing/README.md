# MS-AB-Test
Mastery Project 1: 

Overview

In this project, we will analyze the results of an A/B test and create a presentation of data-driven recommendations based on our findings. 
 
Datasets
This is a case for an e-commerce company called GloBox. GloBox is an online marketplace that specializes in sourcing unique and high-quality 
products from around the world. GloBox is primarily known amongst its customer base for boutique fashion items and high-end decor products. However, 
their food and drink offerings have grown tremendously in the last few months, and the company wants to bring awareness to this product category to 
increase revenue. Managment decides to run an A/B test that highlights key products in the food and drink category as a banner at the top
of the website. The control group does not see the banner, and the test group sees it.

GloBox stores its data in a database with three main tables:
Users (user demographic data): id, country, gender.
Groups (user A/B test group assignment): uid, group, join_dt, device.
Activity (user purchase activity): uid, dt, device, spent.

The task at hand is to analyze the results of the A/B test and provide a recommendation to the stakeholders about whether GloBox should launch 
the experience to all users.
