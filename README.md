# SmartTank

⛽ SmartTank: European Fuel Prices Data Pipeline
SmartTank is a fully automated data pipeline project built on an ELT architecture, designed to monitor and analyze fuel prices across Europe. 💸

A Python script autonomously extracts raw price reports and historical exchange rates (EUR/PLN) from the National Bank of Poland (NBP) API. The data is then cleaned using the Pandas library and rapidly loaded into a PostgreSQL relational database. At the database level, a Medallion Architecture is implemented, where prices are calculated on-the-fly and converted to Polish Zloty (PLN) in the Gold Layer. The entire process is fully orchestrated and feeds a ready-to-use, interactive data model in Power BI. ✨

Tech Stack:
* Language: Python (Pandas, Requests, psycopg2)
* Database: PostgreSQL (SQL, Views)
* Data Visualization: Power BI (Data Modeling, DAX)
* Orchestration: Custom execution script (main.py)
