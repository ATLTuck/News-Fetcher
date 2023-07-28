# News Scraper

A simple Python script to fetch and display news articles based on user input.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The News Scraper is a Python script that utilizes the News API to fetch news articles based on user input. It allows users to search for news articles using keywords and displays relevant information such as the source, author, title, description, URL, and published date. Additionally, it uses BeautifulSoup to scrape the content of each article's webpage and displays the first 500 characters.

## Features

- Fetch news articles based on user input
- Display relevant information about each article
- Scrape and display the content of each article's webpage
- Remove excessive whitespace from the scraped content

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ATLTuck/news-scraper.git
   ```

2. Install the required dependencies:

   Python3
   beatifulsoup4

4. Obtain an API key from [News API](https://newsapi.org/) and replace `API_KEY` in `main.py` with your own API key.

## Usage

1. Run the script:

   ```shell
   python main.py
   ```

2. Follow the on-screen prompts to fetch news articles and view the results.

3. Use the menu options to view recent fetches or exit the program.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
