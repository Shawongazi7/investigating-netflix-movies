# Importing necessary libraries
import pandas as pd            # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting data

# Load the dataset from a CSV file into a pandas DataFrame
netflix_df = pd.read_csv('netflix_data.csv')

# Filter out rows where the 'type' is 'TV Show', keeping only movies
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# Select only the columns relevant for the analysis
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Further filter the dataset to include only movies with a duration less than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Initialize a list to hold color codes for each movie based on its genre
colors = []

# Iterate over each row in the netflix_movies DataFrame
for x, y in netflix_movies.iterrows():
    # Get the genre of the current movie
    gen = y['genre']
    
    # Assign a color based on the genre of the movie
    if 'Children' in gen:
        colors.append('blue')        # Blue for Children's movies
    elif 'Documentaries' in gen:
        colors.append('yellow')      # Yellow for Documentaries
    elif 'Stand-Up' in gen:
        colors.append('pink')        # Pink for Stand-Up Comedy
    else:
        colors.append('gray')        # Gray for all other genres

# Create a new figure for the scatter plot with specified size
fig = plt.figure(figsize=(10, 10))

# Create a scatter plot of movie duration by release year
# Color the points based on the previously assigned colors
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors, alpha=0.7)

# Label the x-axis
plt.xlabel('Release Year')

# Label the y-axis
plt.ylabel('Duration (min)')

# Add a title to the plot
plt.title('Movie Duration by Year of Release')

# Enable grid lines for better readability of the plot
plt.grid(True)

# Display the plot
plt.show()

#whether movie lengths are actually getting shorter
answer = "no"

