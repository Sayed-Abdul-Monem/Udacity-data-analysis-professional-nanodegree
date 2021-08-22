import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities = ['chicago', 'new york city', 'washington']
months = ['all of them', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all of them', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs

    while True:
        city: str = input("select the wanted city to explore :chicago or new york or washington \n")
        city = city.lower()
        if city in cities:
            break
        else:
            print("wrong selection,please enter valid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month: str = input("please select a month to filter or all of them \n")
        month = month.lower()
        if month in months:
            break
        else:
            print("wrong selection ,please enter valid month \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("please select a specific day or all of them \n")
        day = day.lower()
        if day in days:
            break
        else:
            print("wrong selection ,please enter valid day")

    print('-' * 40)
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
    # load the data
    df = pd.read_csv(CITY_DATA[city])

    # convert the start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month ,day ,hour
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all of them':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)

        # create month frame
        df = df[df['month'] == month]
        # df = df.loc[df['month'] == month]
    if day != 'all of them':
        df = df[df['week_day'] == day.title()]
    # df = df.loc[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print(" most common month is ", months[month-1].title(), "\n")
    # TO DO: display the most common day of week

    print("most common day of week  is ", df['week_day'].mode()[0], "\n")

    # TO DO: display the most common start hour
    print("most common start hour is ", df['hour'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most common start station is", df['Start Station'].mode()[0], "\n")
    # TO DO: display most commonly used end station
    print("most common end station is", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip

    print("most common combination stations is", (df['Start Station'] + df['End Station']).mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travelling time ", total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Total travelling time ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Number of Counts of user types :", df['User Type'].value_counts(), "\n")
    # TO DO: Display counts of gender
    print("Number of Counts of gender :", df['Gender'].value_counts(), "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("the earliest year is ", df['Birth Year'].min())
    print("the most common year is ", df['Birth Year'].mode()[0])
    print("the recent year is ", df['Birth Year'].max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
    x = 1
    while True:
        raw = input('\n Would you like to see some raw data? type yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break


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
