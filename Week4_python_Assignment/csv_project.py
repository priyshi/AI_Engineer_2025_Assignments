import pandas as pd

class CovidData:
    def __init__(self, csv_path):
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(csv_path)
    
    def filter_low_cases(self, min_cases=10):
        # Keep only rows where Confirmed cases >= min_cases
        self.df = self.df[self.df['Confirmed'] >= min_cases]
    
    def summarize_by_region(self):
        # Group by WHO Region and sum Confirmed, Deaths, and Recovered
        return self.df.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered']].sum()
    
    def region_highest_confirmed(self):
        # Find the region with the highest total confirmed cases
        return self.df.groupby('WHO Region')['Confirmed'].sum().idxmax()
    
    def sort_by_confirmed(self, output_csv):
        # Sort the DataFrame by Confirmed cases (descending) and save to CSV
        sorted_df = self.df.sort_values(by='Confirmed', ascending=False)
        sorted_df.to_csv(output_csv, index=False)
        return sorted_df
    
    def top5_countries(self):
        # Get the top 5 countries by confirmed cases
        return self.df.nlargest(5, 'Confirmed')[['Country/Region', 'Confirmed']]
    
    def region_lowest_deaths(self):
        # Find the region with the lowest total deaths
        return self.df.groupby('WHO Region')['Deaths'].sum().idxmin()
    
    def india_summary(self):
        # Show India's case summary (Confirmed, Deaths, Recovered, Active)
        india = self.df[self.df['Country/Region'] == 'India']
        return india[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    
    def mortality_rate_by_region(self):
        # Calculate mortality rate (deaths/confirmed) by region
        region = self.df.groupby('WHO Region')[['Confirmed', 'Deaths']].sum()
        region['MortalityRate'] = region['Deaths'] / region['Confirmed']
        return region[['MortalityRate']]
    
    def recovery_rate_by_region(self):
        # Calculate recovery rate (recovered/confirmed) by region
        region = self.df.groupby('WHO Region')[['Confirmed', 'Recovered']].sum()
        region['RecoveryRate'] = region['Recovered'] / region['Confirmed']
        return region[['RecoveryRate']]
    
    def detect_outliers(self):
        # Detect outliers in confirmed cases using mean ± 2*std deviation
        mean = self.df['Confirmed'].mean()
        std = self.df['Confirmed'].std()
        outliers = self.df[(self.df['Confirmed'] > mean + 2*std) | (self.df['Confirmed'] < mean - 2*std)]
        return outliers[['Country/Region', 'Confirmed']]
    
    def group_by_country_region(self):
        # Group data by Country and Region, summing up cases
        return self.df.groupby(['Country/Region', 'WHO Region'])[['Confirmed', 'Deaths', 'Recovered']].sum()
    
    def regions_zero_recovered(self):
        # List regions where total recovered cases are zero
        region = self.df.groupby('WHO Region')['Recovered'].sum()
        return region[region == 0].index.tolist()

class CovidAnalysis(CovidData):
    def __init__(self, csv_path):
        # Inherit all methods from CovidData
        super().__init__(csv_path)

if __name__ == "__main__":
    covid = CovidAnalysis('country_wise_latest.csv')
    print("1. Case summary by region:\n", covid.summarize_by_region())
    covid.filter_low_cases()
    print("\n2. Filtered data (Confirmed >= 10):\n", covid.df)
    print("\n3. Region with highest confirmed cases:", covid.region_highest_confirmed())
    print("\n4. Sorted data saved to sorted_covid.csv")
    covid.sort_by_confirmed('sorted_covid.csv')
    print("\n5. Top 5 countries by case count:\n", covid.top5_countries())
    print("\n6. Region with lowest death count:", covid.region_lowest_deaths())
    print("\n7. India's case summary:\n", covid.india_summary())
    print("\n8. Mortality rate by region:\n", covid.mortality_rate_by_region())
    print("\n9. Recovery rate by region:\n", covid.recovery_rate_by_region())
    print("\n10. Outliers in case counts:\n", covid.detect_outliers())
    print("\n11. Grouped by country and region:\n", covid.group_by_country_region())
    print("\n12. Regions with zero recovered cases:\n", covid.regions_zero_recovered())