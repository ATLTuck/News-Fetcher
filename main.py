import requests
from colorama import Fore, Style
from bs4 import BeautifulSoup

API_KEY = ""
recent_fetches = []

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
        print(Fore.WHITE + "Author:", Fore.WHITE + (author or "N/A"))
        print(Fore.WHITE + "Title:", Fore.MAGENTA + title)
        print(Fore.WHITE + "Description:", Fore.GREEN + (description or "N/A"))
        print(Fore.WHITE + "URL:", Fore.BLUE + url)
        print(Fore.WHITE + "Published Date:", published_date)

        print("------------------------")
        print(Style.RESET_ALL)

    recent_fetches.append(keyword)
    if len(recent_fetches) > 5:
        recent_fetches.pop(0)

def fetch_news_with_keyword(keyword):
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
        print(Fore.WHITE + "Author:", Fore.WHITE + (author or "N/A"))
        print(Fore.WHITE + "Title:", Fore.MAGENTA + title)
        print(Fore.WHITE + "Description:", Fore.GREEN + (description or "N/A"))
        print(Fore.WHITE + "URL:", Fore.BLUE + url)
        print(Fore.WHITE + "Published Date:", published_date)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            content = soup.get_text().strip()  # Remove leading/trailing whitespace
            print(Fore.CYAN + "Content:", content)
        except Exception as e:
            print(Fore.RED + "Error occurred while scraping content:", str(e))

        print("------------------------")
        print(Style.RESET_ALL)

    save_recent_fetches()

def save_recent_fetches():
    with open("recent_fetches.txt", "w") as file:
        for keyword in recent_fetches:
            file.write(keyword + "\n")

def load_recent_fetches():
    try:
        with open("recent_fetches.txt", "r") as file:
            lines = file.readlines()
            recent_fetches.extend([line.strip() for line in lines])
    except FileNotFoundError:
        pass

def display_recent_fetches():
    for i, keyword in enumerate(recent_fetches, start=1):
        print(f"{i}. {keyword}")

def main_menu():
    load_recent_fetches()

    while True:
        print("1. Fetch News")
        print("2. Recent Fetches")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fetch_news()
        elif choice == "2":
            display_recent_fetches()
            choice = input("Enter the number next to the keyword or 0 to go back to the main menu: ")
            if choice == "0":
                continue
            elif choice.isdigit() and int(choice) <= len(recent_fetches):
                fetch_news_with_keyword(recent_fetches[int(choice)-1])
            else:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
