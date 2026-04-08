# ⚽ Premier League Stats Dashboard

An interactive football statistics dashboard built with Streamlit, powered by the API-Football live data API. Explore Premier League top scorers, compare players head-to-head, and analyse attacking stats through a range of charts.

---

## Features

- **Live data** fetched from the [API-Football](https://www.api-football.com/) API
- **Top 10 charts** for goals, assists, shots, shots on target, key passes, and dribbles
- **Goals vs Assists scatter plot** — bubble size reflects appearances
- **Radar chart** — compare any two players across 6 key stats side by side
- **Team filter** — multi-select to focus on specific clubs
- **Custom background** — styled with a football-themed background image
- **Two-page layout** — Home (overview) and Dashboard (full stats)

---

## Getting Started

### Prerequisites

- Python 3.8+
- An [API-Football](https://www.api-football.com/) API key (free tier available)

### Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

### Configuration

Before running, update the following in the script:

1. **API Key** — replace the `API_KEY` value with your own API-Football key:
    ```python
    API_KEY = "your_api_key_here"
    ```

2. **Background image** — update the `image_path` variable to point to your image file:
    ```python
    image_path = "path/to/your/background.jpg"
    ```

### Running the App

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

---

## Usage

Use the **sidebar** to navigate between pages:

- **Home** — overview of the dashboard's features
- **Dashboard** — full stats view with all charts and filters

On the Dashboard page, use the **team multi-select** to filter by club. Use the **player dropdowns** at the bottom to pick two players for the radar chart comparison.

---

## Stats Tracked

| Stat | Description |
|------|-------------|
| Goals | Total goals scored |
| Assists | Total assists |
| Shots | Total shots attempted |
| Shots on Target | Shots on target |
| Key Passes | Passes leading to a shot |
| Dribbles | Dribble attempts |
| Appearances | Games played (used for scatter bubble size) |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `requests` | API data fetching |
| `pandas` | Data manipulation |
| `matplotlib` | Bar, scatter, and radar charts |
| `seaborn` | Styled chart rendering |
| `numpy` | Radar chart angle calculations |

Install all dependencies:

```bash
pip install streamlit requests pandas matplotlib seaborn numpy
```

### requirements.txt

```
streamlit
requests
pandas
matplotlib
seaborn
numpy
```

---

## Project Structure

```
.
├── app.py                  # Main Streamlit app
├── background.jpg          # Background image (add your own)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Screenshots

> Add screenshots of the dashboard here once deployed.

---

## ⚠️ API Notes

- This app uses the **API-Football v3** free tier, which has a limit of 100 requests/day
- Data is cached with `@st.cache_data` to minimise API calls during a session
- Default league is the **Premier League (ID: 39)**, season **2023** — update these in `fetch_top_scorers()` to change

---

## Contributing

Pull requests are welcome! Possible additions — league selector, season picker, defensive stats, xG data, or Streamlit Cloud deployment — feel free to open an issue.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)
