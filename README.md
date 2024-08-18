NBA Player Impact Analysis

1. Project Overview

Objective:
The main goal of this project is to analyze how the points scored by key NBA players (Giannis Antetokounmpo, Joel Embiid, and Anthony Davis) correlate with their respective teams' performance over the last five seasons (2018-2023).
Purpose:
To understand the influence of star players on their team's success, measured by regular-season wins.
2. Setup and Configuration

Prerequisites:
Python 3.8 or higher
Required Python libraries: pandas, matplotlib
Data files:
nba_giannis_embiid_ad_stats_last_5_seasons.json
team_stats.json
Installation:
Clone the repository: git clone [repository link]
Navigate to the project directory: cd NBA-Player-Impact-Analysis
Install the required libraries: pip install -r requirements.txt
3. Project Structure

data/raw/: Contains raw data files.
scripts/data_collection/: Scripts for collecting and preparing data.
scripts/analysis/: Scripts for analyzing data and generating visualizations.
reports/figures/: Output graphs and figures.
README.md: Project documentation.
README_SUMMARY.md: Summary of key findings.
4. Data Collection

Sources:
Data on player stats and team performance was gathered from publicly available APIs and resources.
Injuries and specific data points were manually researched to fill gaps.
5. Analysis Performed

Player Performance vs. Team Success:

Analyzed the relationship between the points scored by each player and the number of wins their team secured during the regular season.
Generated scatter plots and bar charts to visualize correlations.
Impact by Season:

Tracked the performance of players and their respective teams across multiple seasons.
Visualized the progression of points and wins season by season.
6. Results

The analysis demonstrated varying levels of impact for each player on their team's performance.
Giannis Antetokounmpo’s points were consistently correlated with high team performance, particularly in the 2018-19 and 2021-22 seasons.
Joel Embiid showed a strong correlation in the 2021-22 season, reflecting his significant contribution to the Philadelphia 76ers' success.
Anthony Davis’s performance was more volatile, with injury seasons showing a noticeable dip in team success.
7. How to Interpret Results

Scatter Plot: Illustrates the relationship between individual player performance and team success.
Bar Charts: Compare the total points scored by the player and the corresponding team victories per season.
8. Conclusion

The project successfully highlighted the impact of star players on their teams' performance.
It emphasizes the importance of player health and consistency in maintaining team success.
