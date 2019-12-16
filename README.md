# Movie Success Prediction with Dataming

## Current Status on Code
The artifical neural network currently isn't predicting anything. It needs configuration and more data.  Currently my dataset used for training (movies.csv) only contains movie budget, runtime, genre and ratings.

### prototype.py
This is the code that complies and trains the artificial neural network using TensorFlow

### clean_data.py
This prases through massive downloaded datasets (2gb worth) and merges movie metadata from multiple datasets into one. Exlcuding all uncessaary info and pre-formating some categorical data like genre into a binary representation.

### missingBudgetMovies.py
This scripts web scrapes IMDb website for movie's budget. Using a list of movies (with their IMDb code) which didn't have budget in the orginal dataset, it web scraped for missing movie budgets.

### web_scrape.py
Just a prototype web scrape script I was experimenting with

### movies.csv
This is the dataset that's used as input in prototype.py to train the neueral nwtwork. As I was working on adding more data and cleaning the data, I kept the previously used versions of the movies.csv file for reference, but just renamed them as v1 or v2, "movies.csv" is the current version.
