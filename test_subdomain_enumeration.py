import requests

# Define the API endpoints
api_endpoints = {
    "SecurityTrails": "https://api.securitytrails.com/v1/domain/example.com/subdomains?apikey=YOUR_API_KEY",
    "RiskIQ": "https://api.riskiq.net/pt/v2/account/quota",
    "PassiveTotal": "https://api.passivetotal.org/v2/enrichment/subdomains?query=example.com",
}


def test_api_endpoints():
    for service, url in api_endpoints.items():
        print(f"Testing {service} API...")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{service} API is valid (Status Code: {response.status_code})")
            else:
                print(f"{service} API returned an unexpected status code: {response.status_code}")
                print(response.text)  # Print the response content for debugging
        except requests.exceptions.RequestException as e:
            print(f"Error while testing {service} API: {e}")


if __name__ == "__main__":
    test_api_endpoints()
