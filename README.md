1. Data Scraping with Selenium
Objective: Automate the extraction of data from the Redbus website, including routes, schedules, prices, and seat availability.
Approach:
Set Up: Use Selenium WebDriver to navigate the Redbus site.
Scraping: Identify and extract data elements such as route_names, route_links, bus_names, bus_types, departing_time, duration, reaching_time, star_rating, prices, and seats_available.
Storage: Store the extracted data directly into a MySQL database.
2. Data Storage in SQL
Objective: Efficiently store the scraped data for further analysis and retrieval.
Approach:
Database Design: Use a MySQL database with a table structure similar to your Redbus table.
Data Insertion: Insert the scraped data into the database in real-time or batch mode using SQL queries.
3. Streamlit Application for Dynamic Filtering
Objective: Create an interactive dashboard where users can view and filter bus data.
Approach:
Filters: Implement filters for bus_types, route_names, prices, star_ratings, and seats_available.
SQL Integration: Use SQL queries to dynamically fetch and filter data based on user inputs.
User Interface: Display the filtered data using Streamlit's interactive components, such as sliders, dropdowns, and buttons.
4. Data Analysis/Filtering
Objective: Provide insights and customized options based on filtered data.
Approach:
SQL Queries: Write SQL queries that can be dynamically adjusted based on user input from the Streamlit app.
Visualization: Use Streamlit to visualize data trends, patterns, and comparisons (e.g., price trends across different routes).
Business Use Cases
Travel Aggregators: Provide real-time data to customers for better decision-making.
Market Analysis: Analyze user preferences and travel patterns to identify emerging trends.
Customer Service: Enhance user experience by offering customized travel options.
Competitor Analysis: Compare offerings with competitors to stay competitive in pricing and services.
Skills You Will Develop
Web Scraping: Master data extraction techniques using Selenium.
SQL: Learn how to store, retrieve, and filter data in a SQL database.
Streamlit: Gain experience in building interactive applications.
Python: Develop expertise in integrating these technologies to create a seamless workflow.
This project covers the full stack of data extraction, storage, and presentation, offering a comprehensive learning experience.
