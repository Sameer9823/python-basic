import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user = data["data"]
        username = user["login"]["username"]
        country = user["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch random user")
    
    
def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username},\n Country: {country}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()