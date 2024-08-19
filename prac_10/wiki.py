import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def search_wikipedia():
    while True:
        search_query = input("Enter page title: ").strip()
        if not search_query:
            print("Thank you.")
            break

        try:
            # Attempt to retrieve the page with autosuggest off
            page = wikipedia.page(search_query, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary[:500]}...")  # Print a summary up to 500 characters
            print(page.url)

        except DisambiguationError as e:
            # Handle disambiguation (multiple possible pages)
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options)

        except PageError:
            # Handle page not found error
            print(f'Page id "{search_query}" does not match any pages. Try another id!')

        except Exception as e:
            # Handle other potential errors
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_wikipedia()