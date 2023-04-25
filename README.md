# pokemon-stat-checker
This project is a Python and Streamlit web application that allows users to view the stats of a Pokemon at level 100 by specifying its nature, EVs, and IVs. The application utilizes data from the PokeAPI, which is an API that provides comprehensive information on all Pokemon species, their moves, abilities, and more.

To run the application, the user must first install the required Python packages, which can be found in the requirements.txt file. Once the packages are installed, the application can be launched by running the app.py file.

The user interface of the application is designed using Streamlit, which is a Python library for building interactive web applications. The user can input the name of the Pokemon they want to view, and select its nature, EVs, and IVs using the input sliders. The application then uses the PokeAPI to retrieve the base stats of the selected Pokemon species, and calculates the final stats at level 100 based on the user inputs.

The output is displayed in a table that shows the final stats of the Pokemon, including its HP, Attack, Defense, Special Attack, Special Defense, and Speed. The user can also view a bar chart that shows the distribution of the Pokemon's EVs among its stats.

This project is useful for Pokemon trainers who want to plan their Pokemon's stats in advance, and for anyone who is interested in learning more about how Pokemon stats are calculated. It demonstrates the use of Python for data processing and visualization, and the use of an API for retrieving data from a remote server.
