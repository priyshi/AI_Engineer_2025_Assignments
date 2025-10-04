import matplotlib.pyplot as plt
import pandas as pd
from csv_project import CovidAnalysis  

class CovidVisualization(CovidAnalysis):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    # 1. Bar Chart of Top 10 Countries by Confirmed Cases
    def bar_top10_confirmed(self):
        top10 = self.df.nlargest(10, 'Confirmed')[['Country/Region', 'Confirmed']]
        plt.figure(figsize=(10, 6))
        plt.bar(top10['Country/Region'], top10['Confirmed'], color='skyblue')
        plt.xticks(rotation=45)
        plt.title("Top 10 Countries by Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.show()

    # 2. Pie Chart of Global Death Distribution by Region
    def pie_deaths_by_region(self):
        deaths = self.df.groupby('WHO Region')['Deaths'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(deaths, labels=deaths.index, autopct='%1.1f%%', startangle=140)
        plt.title("Global Death Distribution by WHO Region")
        plt.show()

    # 3. Line Chart comparing Confirmed and Deaths for Top 5 Countries
    def line_confirmed_vs_deaths_top5(self):
        top5 = self.df.nlargest(5, 'Confirmed')[['Country/Region', 'Confirmed', 'Deaths']]
        plt.figure(figsize=(10, 6))
        for _, row in top5.iterrows():
            plt.plot(['Confirmed', 'Deaths'], [row['Confirmed'], row['Deaths']], marker='o', label=row['Country/Region'])
        plt.title("Confirmed vs Deaths (Top 5 Countries)")
        plt.ylabel("Cases")
        plt.legend()
        plt.show()

    # 4. Scatter Plot of Confirmed Cases vs Recovered Cases
    def scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['Confirmed'], self.df['Recovered'], alpha=0.6, color='green')
        plt.title("Confirmed vs Recovered Cases")
        plt.xlabel("Confirmed Cases")
        plt.ylabel("Recovered Cases")
        plt.show()

    # 5. Histogram of Death Counts across all Regions
    def hist_deaths(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['Deaths'], bins=20, color='orange', edgecolor='black')
        plt.title("Distribution of Death Counts")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.show()

    # 6. Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
    def stacked_bar_selected_countries(self, countries=['India', 'US', 'Brazil', 'Russia', 'UK']):
        selected = self.df[self.df['Country/Region'].isin(countries)][['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
        selected.set_index('Country/Region').plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title("Stacked Bar: Confirmed, Deaths, Recovered")
        plt.ylabel("Cases")
        plt.show()

    # 7. Box Plot of Confirmed Cases across Regions
    def boxplot_confirmed_by_region(self):
        grouped = [group['Confirmed'].values for _, group in self.df.groupby('WHO Region')]
        plt.figure(figsize=(10, 6))
        plt.boxplot(grouped, labels=self.df['WHO Region'].unique())
        plt.title("Box Plot of Confirmed Cases by Region")
        plt.xticks(rotation=45)
        plt.ylabel("Confirmed Cases")
        plt.show()

    # 8. Trend Line: India vs Another Country
    def trendline_india_vs(self, other_country='US'):
        india = self.df[self.df['Country/Region'] == 'India']
        other = self.df[self.df['Country/Region'] == other_country]

        plt.figure(figsize=(10, 6))
        plt.plot(india['Confirmed'], label="India", marker='o')
        plt.plot(other['Confirmed'], label=other_country, marker='o')
        plt.title(f"Trend Line: India vs {other_country}")
        plt.ylabel("Confirmed Cases")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    covid_vis = CovidVisualization("country_wise_latest.csv")

    covid_vis.bar_top10_confirmed()
    covid_vis.pie_deaths_by_region()
    covid_vis.line_confirmed_vs_deaths_top5()
    covid_vis.scatter_confirmed_vs_recovered()
    covid_vis.hist_deaths()
    covid_vis.stacked_bar_selected_countries()
    covid_vis.boxplot_confirmed_by_region()
    covid_vis.trendline_india_vs("Brazil")
