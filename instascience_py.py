import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl

URL = "https://www.instagram.com/"

# Create an unverified SSL context
context = ssl._create_unverified_context()

# Function to fetch data from Instagram
def fetch_data():
    username = username_entry.get()
    final_url = URL + username

    request = Request(final_url, headers={"User-Agent": "Mozilla/5.0"})
    html_data = urlopen(request, context=context).read()

    soup = BeautifulSoup(html_data, "html.parser")
    try:
        data = soup.find("meta", property="og:description").attrs["content"]

        data = data.split("-")[0]
        data = data.split(",")

        followers_label.config(text="Followers: " + data[0].strip())
        following_label.config(text="Following: " + data[1].strip())
        posts_label.config(text="Posts: " + data[2].strip())
    except Exception as e:
        error_label.config(text="Error: " + str(e))

# Create Tkinter window
root = tk.Tk()
root.title("Instagram Data Fetcher")

# Username entry field
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Fetch data button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Result labels
followers_label = tk.Label(root, text="")
followers_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

following_label = tk.Label(root, text="")
following_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

posts_label = tk.Label(root, text="")
posts_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

error_label = tk.Label(root, text="")
error_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()