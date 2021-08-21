import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['January','February','March','April','May','June','All']
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    while True:
        try:
            city = input('Enter a city to analyze chicago, new york city, washington ').lower()
            while city not in CITY_DATA.keys():
                if city in CITY_DATA.keys():
                    return print('Done')
                else: city = input('Try again enter a city to analyze chicago, new york city, washington ').lower()

            # TO DO: get user input for month (all, january, february, ... , june)
            month = months.index(input("Enter a month to filter or 'All' for all months ").lower().title())

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = days.index(input("Enter a day to filter or 'All' for all days ").lower().title())

            return city, months[month].lower().title(), days[day].lower().title()
        except ValueError:
            print('Sorry try again')


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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("The popular month is ",popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print("The popular day is ",popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The popular hour is ",popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index[0]
    print('The most used start station is ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]
    print('The most used end station is ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + df['End Station']
    popular_combined_station = df['Combined Station'].value_counts().index[0]
    print('The most used combined station are {}'.format(popular_combined_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except KeyError:
        print('There is no data for gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldestYear = df['Birth Year'].min()
        youngestYear = df['Birth Year'].max()
        commonYear = df['Birth Year'].mode()
        print('The oldest year is ',oldestYear)
        print('The youngest year is ',youngestYear)
        print('The most common year is ',commonYear)
    except KeyError:
        print('There is no data for birth year')

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
        add_rows = input('\nWould you like to see the raw data? Enter yes or no.\n')
        if add_rows.lower() == 'yes':
            print(df.head())
        # Restart the code
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
