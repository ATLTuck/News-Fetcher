import requests
from colorama import Fore, Style

API_KEY = "384a0c1d5c6c4bb3941cb3360afdb681"

def fetch_news():
    keyword = input(Fore.WHITE + "Enter a keyword to search for: ")
    num_articles = int(input("Enter the number of articles to return: "))

    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(Fore.RED + "Error occurred while fetching news. Please try again later.")
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        print(Style.RESET_ALL)
        return

    articles = data.get("articles", [])[:num_articles]
    if not articles:
        print(Fore.YELLOW + "No articles found for the given keyword.")
        print(Style.RESET_ALL)
        return

    for article in articles:
        source = article.get("source", {}).get("name")
        author = article.get("author")
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        published_date = article.get("publishedAt")

        print(Fore.WHITE + "Source:", Fore.RED + source)
        print(Fore.WHITE + "Author:", Fore.WHITE + author)
        print(Fore.WHITE + "Title:", Fore.MAGENTA + title)
        print(Fore.WHITE + "Description:", Fore.GREEN + description)
        print(Fore.WHITE + "URL:", Fore.BLUE + url)
        print(Fore.WHITE + "Published Date:", published_date)
        print("------------------------")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    fetch_news()
