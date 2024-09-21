import requests

# Replace with your actual LinkedIn access token
LINKEDIN_ACCESS_TOKEN = "AQU_VKqEd5ygqDVl7LD2qY0WDYEF5MnX33f0E0Erb1KiI-lr0ZFBugVP9YJuyD1QYIkrcixpojh4lDsDJpoCiC50IFE7iNyPyVGy0F8VM98gZNP47RzrZMSL6I6UJj31tjDI5FoQdrIm3xhXgPzMvmafmkHfGHzjFQl7D-y7B2E3t0CyXnhHKb049MybNJ9HzmqIA092l6ZT5ZhcNiI_ma0G9WpafIwbCi23bO_-T75ixqJ-lijdKrCK8Bryov-lzhYlXHBwS3RJ6j22JFLbYHLclT2jYoiKSrKNd6IEwXioXlD-ZxOxxJw0N-HJvYWk0Ti1owDDr2z38QfXpsHPBLdqDYvUpA"

def search_linkedin(query):
    # Adjust the endpoint if needed
    search_url = f"https://api.linkedin.com/v2/userinfo?q={query}"
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}'
    }
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Print detailed response for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.text}")

        search_results = response.json()

        # Process the search results (customize based on actual response structure)
        profiles = search_results.get("elements", [])
        return profiles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.status_code == 401:
            print("Unauthorized: Check if your token has the necessary permissions.")
        elif response.status_code == 403:
            print("Forbidden: Check if you have access to the resource.")
        elif response.status_code == 404:
            print("Not Found: Verify the endpoint.")
    except Exception as err:
        print(f"Other error occurred: {err}")

def main():
    query = input("Enter the search query (e.g., name, company): ").strip()
    
    if not query:
        print("Search query is required.")
        return
    
    profiles = search_linkedin(query)
    
    if profiles:
        print("LinkedIn Profiles Found:")
        for profile in profiles:
            # Adjust the fields based on actual response structure
            name = profile.get("name", "N/A")
            headline = profile.get("headline", "N/A")
            print(f"Name: {name}")
            print(f"Headline: {headline}")
            print()
    else:
        print("No profiles found or error occurred.")

if __name__ == '__main__':
    main()
