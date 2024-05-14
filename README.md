# Project-4---Team-7

## Overview

The project uses ETL workflows to ingest data into the database. We use Pandas to extract and transform the data, then save it to new CSV files. To demonstrate one possible option for the load step, we used PGAdmin to create tables using SQL; five tables in total. An ERD document is included in multiple formats in the folder named "ERD".

To display the data created after the ETL process is complete, we use Pandas DataFrames. We use the Seaborn library (https://seaborn.pydata.org/examples/index.html) to create a set of visualizations demonstrating how data might be analyzed within and across tables. We also serve data via a Flask application to allow for additional functionality on the most significant tables: listings and hosts.

Our project does not include any borrowed code; citations are included in-line where code was built based on external guidance or significant documentation.

The cleaned and transformed dataset could be used to answer the following questions:

What factors are most strongly linked with good ratings / high prices / frequent bookings?
What outliers exist for the above major factors?
What is the correlation between these major factors and do they have any significant correlation with other minor factors?
Can we observe any fluctuations in price based on month / season?
If you want to start hosting in Seattle (or generally), what factors correlate with success or positive host ratings?
Are hosts with many Airbnb listings significantly different from hosts with fewer listings?


## Dependencies

Pandas
Seaborn
Numpy
Sklearn
Matplotlib
Sqlite3
OS
Pathlib

## Contributors

-[Mari Awaisi]

-[Ricky Bialick]

-[Nathan Transon]

-[Thomas Depew]

## Acknowledgments

- Berkeley Data Analytics for providing code snippets and resources used in this project. UC Berkeley Extension
- Contributors of the [UCB-VIRT-DATA-PT-11-2023-U-LOLC](https://github.com/UCB-VIRT-DATA-PT-11-2023-U-LOLC) GitHub repository for providing valuable code and resources used in this project.
- ChatGPT for providing assistance and guidance during the development of these projects.
  
## Resources

- [MLB Glossary](https://www.mlb.com/glossary)
- [Baseball Savant Glossary](https://baseballsavant.mlb.com/statcast_search)

