import time
import pandas as pd
import numpy as np
# i made the second chage for git hub train
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Prints instructions and validates inputs until correct values are provided >>>

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    while True:
        city = input("Would you like to see data for chicago, new york city, or washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter chicago, new york city, or washington.")

    # get user input for month (all, january, february, ... 
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
                'august', 'september', 'october', 'november', 'december', 'all']
    while True:
        month = input("Please enter the month you want to investigate (january, february, ... , june) or 'all' for all months: ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday',  'all']
    while True:
        day = input("Please enter the day you want to investigate (monday, tuesday, ... sunday) or 'all' for all days: ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day or 'all'.")

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
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all' :
        df = df.loc[df['Start Time'].dt.month_name().str.lower() == month]
    if day != 'all' :
        df = df.loc[df['Start Time'].dt.day_name().str.lower() == day]
    row = input("do you want to see a row data ? yes or no ").lower()
    if (row == 'yes') :
        i=0
        while(True):
            print(df.iloc[i:i+5])
            i += 5
            if (input('do you want to see the next 5 lines of row data ? No or Yes  ').lower() == 'no') :
                break
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\n the most common month is : ', df['Start Time'].dt.month_name().value_counts().idxmax())

    # display the most common day of week
    print('\n the most common day of the week is ', df['Start Time'].dt.day_name().value_counts().idxmax())

    # display the most common start hour
    print('\n the most common start hour is :' ,df['Start Time'].dt.hour.value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\n most commonly used start station :',df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('\n most commonly used end station :' ,df['End Station'].value_counts().idxmax())
    # display most frequent combination of start station and end station trip
    print('\nmost freaquent of start station grouped by end station ',df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\n the total travel time : ' ,df['Trip Duration'].sum())


    # display mean travel time
    print('\n avarage travel time is : ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\n counts of user types ', df['User Type'].value_counts())
    # Display counts of gender
    if ('Gender' in df.columns) :
        print(' \n counts of gender ', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df.columns) :
        print('\n the most comon birth year  is : ', df['Birth Year'].mode()[0])
        print('\n the most recent birth year is ',df['Birth Year'].max())
        print('the earliest birth year is :',df['Birth Year'].min())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()