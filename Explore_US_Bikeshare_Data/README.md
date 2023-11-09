# US Bikeshare <h2>

### Overview <h3>
It requires the use of Python language to import data related to bike share systems for three major cities in the US-Chicago, New York City, and Washington. The resulting program will compute descriptive statistics to uncover bike share usage patterns questions. Plus, the program takes in raw input interactively and responds back with computed statistics. 

### Datasets <h3>
These datasets contain randomly selected data for the first six months of 2017 of the three cities. All three data files contain the same six columns: Start Time, End Time, Trip Duration, Start Station, End Station, User Type.

The files for Chicago and New York City have two additional columns: Gender, Birth Year.

### Statistics computed to answer these questions <h3>
#1 Popular times of travel (i.e., statistics based on start time)
   What is the most popular month?
   What is the most popular day of week?
   What is the most popular hour of day?

#2 Popular stations and trip 
   What is the most popular start station?
   What is the most popular end station?
   What is the most popular trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration 
   What is the total travel time?
   What is the average travel time?

#4 User information 
   What are the counts of each user type (Subscriber, Customer)?
   What are the counts of each gender type (Female, Male)?
   What is the earliest year of birth (i.e. oldest person), most recent year of birth (i.e. youngest person), and the most common year of birth? (Only available for NYC and Chicago)

In addition to statistic questions, this script can display raw data upon a user's request:
* Prompt a user if he/she wants to see raw data
* Display the data if the answer is 'yes'
* Continue to display the next 5 lines of raw data for reach iteration
* Stop the processing or if there is no more data to display
