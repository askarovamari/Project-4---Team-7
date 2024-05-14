# Project-4---Team-7

## About the project

The goal of the project is to analyze a dataset retrieved from [Savant](https://baseballsavant.mlb.com/statcast_search) and build a predictive model for one of the major stats of baseball - Batting Average. The original dataset baseballData.csv consists of 1416 lines and 65 columns with Baseball Stats from 2015 through 2024.

## Overview

With ETL we shaped the original dataset and kept . We use Pandas to extract and transform the data, then save it to new CSV files. To demonstrate one possible option for the load step, we used PGAdmin to create tables using SQL; five tables in total. An ERD document is included in multiple formats in the folder named "ERD".

The output of ETL is presented in the Pandas DataFrame and being saved into the SQLite database. 


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

