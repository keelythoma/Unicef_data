# UNICEF Data Analysis Project
This repository contains a data analysis report on UNICEF indicators created for the BAA1030 assignment.
Project Overview
This project analyzes UNICEF data to raise awareness about a specific world issue. The analysis includes various visualizations created with the plotnine package and a narrative explaining the findings.
Data Sources
The analysis uses the following data files:

unicef_indicator_1.csv
unicef_indicator_2.csv
unicef_metadata.csv

Visualizations
The report includes:

A world map chart showing geographical distribution
A bar chart comparing key metrics
A scatterplot with a linear regression line showing relationships between variables
A time-series chart showing trends over time

Technical Implementation
The report is created using Quarto and published with GitHub Pages. The visualizations are generated using the plotnine package in Python.
Viewing the Report
The rendered report can be viewed at: https://yourusername.github.io/repository-name
Project Structure

index.qmd: Main Quarto document containing the analysis and narrative
data/: Directory containing the UNICEF data files
README.md: This file

How to Run Locally

Clone this repository
Install the required packages: pip install pandas numpy plotnine matplotlib geopandas
Open index.qmd in VS Code with the Quarto extension
Click "Render" to generate the HTML output