import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os
import platform

# Clear the terminal screen based on the OS
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(14, 7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051)) 
    sea_level_fit = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit, color='purple')
    
    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Only predict from 2000 to 2050 for the second line of best fit
    years_recent_extended = pd.Series(range(2000, 2051)) 
    sea_level_fit_recent = slope_recent * years_recent_extended + intercept_recent
    plt.plot(years_recent_extended, sea_level_fit_recent, color='violet')

    # Add labels and title
    plt.title('Rise in Sea Level', fontsize=18)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Sea Level (inches)', fontsize=14)
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()