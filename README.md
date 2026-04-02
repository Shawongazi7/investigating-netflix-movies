# Investigating Netflix Movies

This project explores Netflix movie data through a notebook-first exploratory data analysis workflow. The main goal is to look at how movie duration changes over time, while also surfacing genre patterns, country trends, and a few focused insights around 1990s movies.

## Main Notebook

- `Investigating_Netflix_Movies.ipynb`

This notebook is the main project artifact and brings the code, findings, and visuals together in one place for GitHub review.

## Highlights

- 7,787 total Netflix titles in the dataset
- 5,377 movie entries used for the movie-focused analysis
- Average movie duration: 99.31 minutes
- 194 movies released in the 1990s
- Dramas, Comedies, and Documentaries appear most often among movie titles

## Questions Explored

- Are Netflix movie durations getting shorter over time?
- What does the duration-by-year pattern look like?
- Which genres appear most often in the movie catalog?
- Which countries contribute the most movie titles?
- What stands out about movies from the 1990s?

## Project Structure

```text
investigating-netflix-movies/
├── Investigating_Netflix_Movies.ipynb
├── netflix_data.csv
├── README.md
├── requirements.txt
├── .gitignore
└── plots/
    ├── movie_duration_by_year.png
    ├── top_countries.png
    └── top_genres.png
```

## Visual Snapshot

### Movie Duration by Release Year

![Movie Duration by Release Year](plots/movie_duration_by_year.png)

### Top Movie Genres

![Top Movie Genres](plots/top_genres.png)

### Top Movie Countries

![Top Movie Countries](plots/top_countries.png)

## Running the Project

```bash
pip install -r requirements.txt
jupyter notebook Investigating_Netflix_Movies.ipynb
```

You can also preview the notebook directly on GitHub.
