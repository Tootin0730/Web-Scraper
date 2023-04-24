from requests import get
# installed requests
websites = {
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "tiktok.com"
}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)