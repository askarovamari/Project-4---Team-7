# Project-4---Team-7

## About the project

The goal of the project is to analyze a dataset retrieved from [Savant](https://baseballsavant.mlb.com/statcast_search) and build a predictive model for one of the major stats of baseball - Batting Average. The original dataset baseballData.csv consists of 1416 lines and 65 columns with Baseball Stats from 2015 through 2024.

At the end, we conducted exploratory analysis on feature importance and correlation, and created a flask app to predict player batting average.

## Overview

With ETL we shaped the original dataset and kept only 30 columns needed for the model, omitting player name and ID, as they are not relevant for prediction. The output of ETL is presented in the Pandas DataFrame and being saved into the SQLite database & new Baseball_stats_cleaned.csv. 


Graphs

Graphs were made to indicate the ammount of importance in which each feature had in determining batting average. Analysis of importance then was conducted through groups pre-determined by our ETL. Analysis was then conducted to see if correlation increased as importance increased. 
...

Random Forest

...

Flask App

In the back end of the app, we start with saving our model into a joblib file and then we are retrieving it with the Flask through the same job lib library. We are using HTML to visually display data and rendering this html template in the Flask App. 

## Dependencies

Pandas /
Seaborn /
Numpy /
Sklearn /
Matplotlib /
Sqlite3 /
OS /
Pathlib

## Contributors

-[Ricky Bialick] / [Thomas Depew] - ETL / plotting trend graphs

-[Nathan Transon] - Predictive model "Random Forest"

-[Mari Awaisi] - Flask App / SQLite DB


## Acknowledgments

- Berkeley Data Analytics for providing code snippets and resources used in this project. UC Berkeley Extension
- Contributors of the [UCB-VIRT-DATA-PT-11-2023-U-LOLC](https://github.com/UCB-VIRT-DATA-PT-11-2023-U-LOLC) GitHub repository for providing valuable code and resources used in this project.
- ChatGPT for providing assistance and guidance during the development of these projects.
  
## Resources

- [MLB Glossary](https://www.mlb.com/glossary)
- [Baseball Savant Glossary](https://baseballsavant.mlb.com/statcast_search)

