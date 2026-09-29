# 🕷️ vlrscraper

![status](https://img.shields.io/badge/status-discontinued-lightgrey)
[![license](https://img.shields.io/github/license/canmenzo/vlrscraper)](LICENSE)
![python](https://img.shields.io/badge/python-3.6+-blue?logo=python&logoColor=white)

Scrapes the comments on a [VLR.gg](https://www.vlr.gg) match page, pulls out score predictions for the two teams, and prints the most common one.

> *This is a discontinued project. Comments within VLR.gg are not as valuable as you might think they are.*

### ✨ Features
- 🌐 Downloads every comment on a match page (`requests` + BeautifulSoup)
- 🔎 Keeps comments that mention either team with a score, like `LOUD 2-1 GenG` (team names are matched case-insensitively)
- 📊 Rewrites every prediction from the first team's side (`GenG 1-2 LOUD` counts as `LOUD 2-1 GenG`) and sorts them
- 🏆 Prints the most repeated prediction and how many times it appeared

### 🚀 Quick start
```bash
pip install -r requirements.txt
python3 all.py
```
Paste a VLR.gg match URL and the two team names when asked. Intermediate results are written to `output.txt` (raw comments), `scores.txt` (filtered) and `processed_scores.txt` (sorted).

### 📄 License
MIT
