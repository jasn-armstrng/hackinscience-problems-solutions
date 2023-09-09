# https://www.hackinscience.org/exercises/doing-http-requests
import requests
from requests.exceptions import RequestException
from typing import Dict, Any

def fetch(url: str) -> Dict[str, Any]:
    """
    Fetch JSON data from a specified URL.

    :param url: A string containing the URL to fetch data from.
    :return: A dictionary containing the JSON response data.
    :raises RequestException: If there is a problem with the network request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"An error occurred during the request: {e}")
        return {}  # return an empty dict or any other default value

def main() -> None:
    data = fetch('https://api.github.com/users/python')
    print(data)

if __name__ == "__main__":
    main()
