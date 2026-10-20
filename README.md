GitHub Repository Analyzer

A Python project that uses the GitHub REST API to search and analyze public GitHub repositories.

Features

- Search public repositories by keyword
- Display repository information
- Find the most-starred repository
- Filter repositories by programming language
- Save repository data to a JSON file
- Load previously saved repository data
- Avoid duplicate repositories when saving new results

Technologies Used

- Python
- Requests
- GitHub REST API
- JSON
- pathlib

Requirements

- Python 3
- Internet connection
- "requests" library

Installation

Install the required library:

pip install requests

How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the Python file:

python github_repo_search.py

4. Follow the menu displayed by the program.

API

This project uses the GitHub REST API repository search endpoint:

https://api.github.com/search/repositories

The API can be used for basic public repository searches without an API key, subject to GitHub's unauthenticated rate limits.

Learning Objectives

This project helped me practise API requests, JSON processing, dictionaries, lists, sets, functions, file handling, duplicate checking, and exception handling.

Future Improvements

- Add pagination
- Improve error handling
- Add more repository sorting and filtering options

License

See the LICENSE file for licensing information.
