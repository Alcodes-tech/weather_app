import requests

def fetch_capitals():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    response.raise_for_status()  # Will raise an error if request failed

    countries_data = response.json()
    capitals = []

    for country in countries_data:
        country_name = country.get('name', {}).get('common', '')
        capital_list = country.get('capital', [])  # capital is a list

        if capital_list:  # Some countries have no capital listed
            capital = capital_list[0]  # Take first capital if multiple
            capitals.append((capital, country_name))

    return capitals

if __name__ == "__main__":
    capitals = fetch_capitals()
    for capital, country in capitals:
        print(f"{capital} - {country}")