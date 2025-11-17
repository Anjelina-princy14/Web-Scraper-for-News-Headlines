📰 Web Scraper for News Headlines
📌 Project Overview

This project is part of the Python Developer Internship – Task 3.
The goal is to automate data collection from a public website by scraping the latest news headlines and saving them into a text file for further use or analysis.

The script fetches live news headlines from BBC News, extracts unique <h2> tags using BeautifulSoup, and stores them in headlines.txt — one headline per line, as required in the task.

🛠 Technologies Used

Python

requests – Fetch webpage HTML

BeautifulSoup (bs4) – Parse and extract headline tags

File handling – Write data to .txt file

📁 Files in This Project
File Name	Purpose
headline_scraper.py	Python script for scraping headlines
headlines.txt	Output file containing the headlines
README.md	Project documentation
▶️ How to Run
1️⃣ Install Required Packages

Open terminal and run:

pip install requests beautifulsoup4

2️⃣ Run the Script
python headline_scraper.py

3️⃣ Check Output

Once the script finishes, a file named headlines.txt will be generated containing:

Headline 1
Headline 2
Headline 3
...
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8a77dd71-ecc3-484d-b7ab-ffd92a226e44" />
