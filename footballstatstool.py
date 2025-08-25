import base64
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ----------------------------
# 1️⃣ API Setup
# ----------------------------
API_KEY = "4b5be4ee607a717d6bc01281fb01d122"
BASE_URL = "https://v3.football.api-sports.io"
headers = {"x-apisports-key": API_KEY}

# ----------------------------
# 2️⃣ Fetch Top Scorers Safely
# ----------------------------
@st.cache_data
def fetch_top_scorers(league=39, season=2023):
    url = f"{BASE_URL}/players/topscorers"
    params = {"league": league, "season": season}
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()

    players = []
    for item in data.get("response", []):
        stats_list = item.get("statistics", [])
        stats = stats_list[0] if stats_list else {}

        players.append({
            "player": item.get("player", {}).get("name", "Unknown"),
            "team": stats.get("team", {}).get("name", "Unknown"),
            "goals": stats.get("goals", {}).get("total") or 0,
            "assists": stats.get("goals", {}).get("assists") or 0,
            "shots": stats.get("shots", {}).get("total") or 0,
            "shots_on_target": stats.get("shots", {}).get("on") or 0,
            "key_passes": stats.get("passes", {}).get("key") or 0,
            "dribbles": stats.get("dribbles", {}).get("attempts") or 0,
            "appearances": stats.get("games", {}).get("appearances") or 0,
            "tackles": stats.get("tackles", {}).get("tackles") or 0
        })

    df = pd.DataFrame(players)
    numeric_cols = ["goals", "assists", "shots", "shots_on_target", "key_passes", "dribbles", "appearances"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
    return df


# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

# ----------------------------
# Background Image
# ----------------------------
image_path = r"C:\Users\HarryHogg\PycharmProjects\Footballdatatool\football-background-vector.jpg"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

page_bg_img = f"""
<style>
.stApp {{
background-image: url("data:image/jpg;base64,{encoded_image}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# ----------------------------
# HOME PAGE
# ----------------------------
if page == "Home":
    st.title("⚽ Welcome to the Football Stats Dashboard")
    st.markdown("""
    This dashboard lets you explore Premier League player statistics.  

    ### Features:
    - 📊 Top 10 Goal Scorers
    - 🎯 Goals vs Assists Analysis
    - 🕸 Player Comparison (Radar Chart)
    - 🔑 Key Passes, Shots, Dribbles  

    👉 Use the **sidebar** to navigate to the Dashboard.
    """)


# ----------------------------
# DASHBOARD PAGE
# ----------------------------
elif page == "Dashboard":
    st.title("⚽ Premier League Top Scorers Dashboard")

    # Fetch data
    df = fetch_top_scorers()

    # Team filter
    teams = st.multiselect("Select Teams:", options=df["team"].unique(), default=df["team"].unique())
    filtered_df = df[df["team"].isin(teams)]

    # ----------------------------
    # 5️⃣ Top 10 Goal Scorers (Bar)
    # ----------------------------
    st.subheader("Top 10 Goal Scorers")
    top10 = filtered_df.sort_values(by="goals", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="goals", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Goals")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

    # ----------------------------
    # 5️⃣ Top 10 Assists (Bar)
    # ----------------------------
    st.subheader("Top 10 Assists")
    top10 = filtered_df.sort_values(by="assists", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="assists", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Assists")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

    # ----------------------------
    # 5️⃣ Top 10 Shots (Bar)
    # ----------------------------
    st.subheader("Top 10 Shots")
    top10 = filtered_df.sort_values(by="shots", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="shots", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Shots")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

    # ----------------------------
    # 5️⃣ Top 10 Shots on target (Bar)
    # ----------------------------
    st.subheader("Top 10 Shots on Target")
    top10 = filtered_df.sort_values(by="shots_on_target", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="shots_on_target", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Shots on Target")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

    # ----------------------------
    # 5️⃣ Top Key Passes (Bar)
    # ----------------------------
    st.subheader("Key Passes")
    top10 = filtered_df.sort_values(by="key_passes", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="key_passes", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Key Passes")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

    # ----------------------------
    # 5️⃣ Key Dribbles (Bar)
    # ----------------------------
    st.subheader("Dribbles")
    top10 = filtered_df.sort_values(by="dribbles", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10, x="dribbles", y="player", hue="team", dodge=False, ax=ax)
    ax.set_xlabel("Dribbles")
    ax.set_ylabel("Player")
    ax.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)


    # ----------------------------
    # 6️⃣ Goals & Assists (Scatter)
    # ----------------------------
    st.subheader("Goals & Assists")
    # Ensure numeric
    for col in ["goals", "assists", "appearances"]:
        filtered_df[col] = pd.to_numeric(filtered_df[col], errors='coerce').fillna(0)

    scatter_df = filtered_df[(filtered_df["goals"] > 0) | (filtered_df["assists"] > 0)]

    if scatter_df.empty:
        st.warning("No data available for Goals vs Assists plot.")
    else:
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.scatterplot(
            data=scatter_df,
            x="goals",
            y="assists",
            hue="team",
            size="appearances",
            sizes=(50, 300),
            alpha=0.7,
            ax=ax2
        )
        for i, row in scatter_df.iterrows():
            ax2.text(row["goals"] + 0.1, row["assists"] + 0.1, row["player"], fontsize=8)
        ax2.set_xlabel("Goals")
        ax2.set_ylabel("Assists")
        ax2.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig2)

    # ----------------------------
    # 7️⃣ Player Comparison Radar Chart
    # ----------------------------
    st.subheader("Player Comparison Radar Chart")
    players = filtered_df["player"].tolist()
    player1 = st.selectbox("Select Player 1", players)
    player2_options = [p for p in players if p != player1]
    player2 = st.selectbox("Select Player 2", player2_options)

    categories = ["goals", "assists", "shots", "shots_on_target", "key_passes", "dribbles"]


    def get_player_stats(player_name):
        row = filtered_df[filtered_df["player"] == player_name].iloc[0]
        return [row.get(stat, 0) for stat in categories]


    p1_stats = get_player_stats(player1)
    p2_stats = get_player_stats(player2)

    fig3, ax3 = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    p1_stats += p1_stats[:1]
    p2_stats += p2_stats[:1]
    angles += angles[:1]

    ax3.plot(angles, p1_stats, label=player1, linewidth=2)
    ax3.fill(angles, p1_stats, alpha=0.25)
    ax3.plot(angles, p2_stats, label=player2, linewidth=2)
    ax3.fill(angles, p2_stats, alpha=0.25)
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(categories)
    ax3.set_title(f"Radar Chart: {player1} vs {player2}")
    ax3.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    st.pyplot(fig3)