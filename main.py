from requests import get
# installed requests
websites = {
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "tiktok.com"
}

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"
        
    print(website)