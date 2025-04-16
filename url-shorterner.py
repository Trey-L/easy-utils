import pyshorteners
import sys 

def create_short_url(long_url):
    """
    Shortens a given URL using the TinyURL service via pyshorteners.
    """
    # Basic check if the URL seems somewhat valid (starts with http)
    # You could add more robust validation if needed
    if not long_url.startswith(('http://', 'https://')):
        print("Warning: URL might be invalid (doesn't start with http:// or https://).", file=sys.stderr)
        # Optionally return None here if you want to enforce http/https
        # return None

    try:
        # Initialize the Shortener object
        s = pyshorteners.Shortener()

        # Use the TinyURL shortener service
        # You can explore other services like s.chilpit.short(long_url) etc.
        # Some services (like Bitly) might require API keys:
        # s = pyshorteners.Shortener(api_key='YOUR_BITLY_KEY')
        # short_url = s.bitly.short(long_url)

        short_url = s.tinyurl.short(long_url)
        return short_url

    except pyshorteners.exceptions.ShorteningErrorException as e:
        # Handle errors specifically from the shortening service (e.g., invalid URL format for them)
        print(f"Error: Could not shorten URL. The service reported an error: {e}", file=sys.stderr)
        return None
    except pyshorteners.exceptions.BadAPIResponseException as e:
         print(f"Error: Bad response from the shortening service API: {e}", file=sys.stderr)
         return None
    except Exception as e:
        # Catch other potential errors (like network connection issues)
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        print("Please check your internet connection and if the URL is valid.", file=sys.stderr)
        return None

if __name__ == "__main__":
    print("--- Simple URL Shortener (using TinyURL) ---")
    original_url_input = input("Enter the full URL you want to shorten: ").strip() # .strip() removes leading/trailing whitespace

    if not original_url_input:
        print("Error: You didn't enter a URL.", file=sys.stderr)
    else:
        shortened_url_result = create_short_url(original_url_input)
      
        if shortened_url_result:
            print("\n--- Result ---")
            print(f"Original URL: {original_url_input}")
            print(f"Shortened URL: {shortened_url_result}")
        else:
            print("\nFailed to shorten the URL.")

