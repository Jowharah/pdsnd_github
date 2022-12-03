
#importing necessacry library 
import time
import pandas as pd
import numpy as np
from tabulate import tabulate

#Global values to be used in all funtions 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

#functions 
def get_city():
    """
    Asks user to specify a city to be used in get_filters

    Returns:
        (str) city - name of the city to analyze
    """
    flag=True
    while (flag):
        city = str(input("Enter the city name you would like to view (chicago), (new york city) or (washington): "))
        if city in CITY_DATA.keys():
            flag=False 
        else:
            print("your input is wrong \n")
    return city

def get_day():
    """
    Asks user to specify a day to be used in get_filters

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    flag=True
    while (flag):
        day = str(input("input for day of week (all, monday, tuesday, ... sunday): "))
        if day.lower() in days or day.lower() == 'all':
            flag=False 
            day = day
        else:
            print("your input is wrong \n")
    return day

def get_month():
    """
    Asks user to specify a month to be used in get_filters

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    flag=True
    while (flag):
        month = str(input("input for month (all, january, february, ... , june): "))
        if month.lower() in months or month.lower() == 'all':
            flag=False 
            month = month
        else:
            print("your input is wrong")
    return month

def check_data_entry(prompt, valid_entries): 
    """
    Asks user to type some input and verify if the entry typed is valid.
    Since we have 3 inputs to ask the user in get_filters(), it is easier to write a function.
    Args:
        (str) prompt - message to display to the user
        (list) valid_entries - list of string that should be accepted 
    Returns:
        (str) user_input - the user's valid input
    """
    try:
        user_input = str(input(prompt)).lower()

        while user_input not in valid_entries : 
            print('Sorry... it seems like you\'re not typing a correct entry.')
            print('Let\'s try again!')
            user_input = str(input(prompt)).lower()

        print('Great! the chosen entry is: {}\n'.format(user_input))
        return user_input

    except:
        print('Seems like there is an issue with your input')



def get_filters(): 
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hi there! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = CITY_DATA.keys()
    prompt_cities = 'Please choose one of the 3 cities (chicago, new york city, washington): '
    city = check_data_entry(prompt_cities, valid_cities)


    # get user input for month (all, january, february, ... , june)
    valid_months = ['all','january','february','march','april','may','june']
    prompt_month = 'Please choose a month (all, january, february, ... , june): '
    month = check_data_entry(prompt_month, valid_months)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday', 'sunday']
    prompt_day = 'Please choose a day (all, monday, tuesday, ... sunday): '
    day = check_data_entry(prompt_day, valid_days)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file = CITY_DATA[city]
    df = pd.read_csv(file)
    
    #convert column to date time type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create two columns for month and date
    df['month'] = df['Start Time'].dt.month_name() 
    df['day'] = df['Start Time'].dt.day_name()
    
    if month is not "":
        if month != 'all':
            df = df[ df['month'] == month.title()]

    if day is not "":
        if day != 'all':
            df = df[ df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
       df - the loaded data frame to be used in statistics analysis  
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_commen_month = df["month"].mode()[0]
    print("The most commen month is: " + most_commen_month)

    # TO DO: display the most common day of week
    most_commen_day = df["day"].mode()[0]
    print("The most commen day is: " + most_commen_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_commen_hour = df["hour"].mode()[0]
    print("The most commen hour is: " + str(most_commen_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
       df - the loaded data frame to be used in statistics analysis  
    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commen_start_station = df["Start Station"].mode()[0]
    print("The most commen start station: " + most_commen_start_station)


    # TO DO: display most commonly used end station
    most_commen_end_station = df["End Station"].mode()[0]
    print("The most commen end station: " + most_commen_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["start_and_end_station"] = df["Start Station"] + df["End Station"]
    most_commen_start_and_end_station = df["start_and_end_station"].mode()[0]
    print("The most commen start station and end station: " + most_commen_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
       df - the loaded data frame to be used in statistics analysis      
    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time: " + str(total_travel_time))

    # TO DO: display mean travel time
    total_travel_time = df["Trip Duration"].mean()
    print("The mean (average) travel time: " + str(total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
       df - the loaded data frame to be used in statistics analysis  
       (str) city - name of the city to analyze       
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The user types: \n" + str(user_types) +"\n")


    
    if city != "washington":
        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print("The user gender counts: \n" + str(user_gender)+"\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        most_commen_year = int(df['Birth Year'].value_counts().idxmax())
        print("The most commen year: " + str(most_commen_year)+"\n")
        
        most_recent_year = int(df['Birth Year'].max())
        print("The most recent year: " + str(most_recent_year)+"\n")
        
        earliest_year = int(df['Birth Year'].min())
        print("The earliest year: " + str(earliest_year)+"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw date to the user 5 each time

    Args:
       df - the loaded data frame to be used in statistics analysis  
    
    """    
    
    flag = True
    i = 0
    max_value = len(df.index) - 5
    while (flag and i < max_value):
        answer = input("Do you want to print 5 rows of raw data? (yes) to show or (no) to skip: ")
        if answer.lower() != 'yes':
            flag=False
        else :
            print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
            i+=5    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print(df.head())
        print(df.tail())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
