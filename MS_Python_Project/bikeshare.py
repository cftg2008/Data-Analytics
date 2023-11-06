#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

filter_months = ['all','january','february','march','april','may','june']
filter_week_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
cities = ['chicago', 'new york city', 'washington']

def get_filters():
    """
    -> Gets user to enter city, month, day for analysis
    -> Validates inputs and request to retry for invalid inputs
    -> Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    while True:
        print('\nWhich city would you like to get data for analysis?')
        city= input('Chicago, New York City, or Washington? ').lower()
        if city in cities:
            break
        else:
            print('Please re-enter a valid city...')
            continue
            
    # get user input for month (all, january, february, ... , june)
    while True:
        print('\nWhich month? Or enter all for six months of data...')
        month = input('All, January, February, March, April, May, or June? ').lower()
        if month in filter_months:
            break
        else:
            print('Please re-enter a valid month or all for 6 months...')
            continue
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\nWhich day? or enter all for whole week...')
        day = input('All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
        if day in filter_week_days:
            break
        else:
            print('Please re-enter a valid day or all for 7 days...')
            continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    -> Gets file path from CITY_DATA 
    -> Loads data based on city, month, day arguments

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    -> Returns:
        df - Pandas DataFrame containing city data filtered by month and day for statistics computation
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['day_number'] = df['Start Time'].dt.day_of_week


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = filter_months.index(month)
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        day = day.title()
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """
    -> Gets df from load_data
    -> Returns:
        Displays statistics on the most popular times of travel
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most popular month to travel
    most_common_mth = df['month'].mode()[0]
    print('Most Popular Month to Travel: ', filter_months[most_common_mth].title())
    
    # display the most popular day of week to travel
    most_common_day = df['day_number'].mode()[0]
    print('Most Popular Day of Week to Travel: ', filter_week_days[most_common_day + 1].title())
    
    # display the most popular start hour to travel
    df['hour'] = df['Start Time'].dt.hour
    most_common_hr = df['hour'].mode()[0]
    print('Most Popular Start Hour to Travel :', most_common_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """
    -> Gets df from load_data
    -> Returns:
        Displays statistics on the most popular stations and trip
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display the most popular start station
    most_common_start_stn = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', most_common_start_stn)

    # display the most popular end station
    most_common_end_stn = df['End Station'].mode()[0]
    print('Most Popular End Station: ', most_common_end_stn)

    # display most popular trip from start to end 
    df['Combined Station'] = df['Start Station'] +" "+ df['End Station']
    most_combined_stn = df['Combined Station'].mode()[0]
    print('Most Popular Trip - Start and End Stations: {}'.format(most_combined_stn))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """
    -> Gets df from load_data
    -> Returns:
        Displays statistics on the total trip duration and average travel time
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display the total travel duration
    total_travel_time = df['Trip Duration'].sum()
    print('Total Trip Duration: ', total_travel_time)

    # display the average travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """
    -> Gets df from load_data and city from get_filters
    -> Returns:
        Displays statistics on the bikeshare users information
        Displays message certain data is not available in the Washington file 
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_type_cnt = df['User Type'].value_counts().rename_axis('User Type').to_frame('Counts')
    print(user_type_cnt)
    print(' ')
    
    if city == 'washington':
        print('The data for Gender and Birth Year is not available in the Washington file')

    # Display counts of gender
    if city != 'washington':
        if 'Gender' in df.columns: 
            gender_cnt = df['Gender'].value_counts().rename_axis('Gender').to_frame('Counts')
            print(gender_cnt)
            print(' ')

    # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns: 
            earliest_yr = df['Birth Year'].min()
            print('Earliest Year of Birth: ', int(earliest_yr))
            most_recent_yr = df['Birth Year'].max()
            print('Most Recent Year of Birth: ', int(most_recent_yr))
            most_common_yr = df['Birth Year'].mode()[0]
            print('Most Common Year of Birth: ', int(most_common_yr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_chunks(city):
    """
    -> Gets user to enter confirmation if raw data display is needed
    -> Returns:
        Displays 5 rows of data
        Asks user if to continue to view data
    """
    file_name = CITY_DATA.get(city)
    while True:
        for chunk in pd.read_csv(file_name, chunksize=5):
            uGet = input('\nContinue to view? yes/no: ')
            if uGet.lower() == 'yes':
                print(chunk)
            elif uGet.lower() == 'no':
                break 
            else:
                print('Please re-enter valid value to continue...')
                continue
            
        if uGet.lower() in ['no','yes']:
            break
            
def main():
    
    while True:
        
        city, month, day = get_filters() 
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df) 
        user_stats(df,city)
        
        while True:
            view_data = input('\nWould you like to view raw data? yes/no:\n')
            if view_data.lower() == 'yes':
                view_chunks(city)
            elif view_data.lower() == 'no':
                break
            else:
                print('please re-enter valid confirmation...')
                continue
            
            if view_data.lower() in['yes','no']:
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()

