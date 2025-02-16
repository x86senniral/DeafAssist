import streamlit as st
import json
import os
import time
import pandas as pd

st.set_page_config(
    page_title="Deaf Assistance Dashboard",
    page_icon="🔔",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        body { background-color: #121212; color: #ffffff; font-family: 'Arial', sans-serif; }
        .stApp { background-color: #121212; }
        .main-container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            text-align: center;
        }
        .alert-box {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            padding: 25px;
            border-radius: 12px;
            margin-top: 30px;
            box-shadow: 0px 4px 20px rgba(255,255,255,0.3);
            transition: all 0.3s ease-in-out;
        }
        .fire { background-color: #ff4b4b; color: white; border: 3px solid #ff2222; }
        .knock { background-color: #ff9800; color: black; border: 3px solid #ff7700; }
        .no-alert { background-color: #1e1e1e; color: #aaaaaa; border: 3px solid #333333; }
        .header-title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            margin-bottom: 25px;
            background: linear-gradient(90deg, #ff9800, #ff4b4b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 16px;
            color: #aaa;
        }
        .user-box {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            text-align: left;
            width: 300px;
            margin: auto;
            margin-bottom: 20px;
            box-shadow: 0px 4px 15px rgba(255,255,255,0.2);
        }
        .user-box p { margin: 5px 0; font-size: 18px; color: #ffffff; }
        .user-box span { font-weight: bold; color: #ff9800; }
        .sidebar-container {
            padding: 15px;
            background-color: #1e1e1e;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(255,255,255,0.2);
        }
        .sidebar-item {
            padding: 10px;
            font-size: 18px;
            color: #ffffff;
            margin: 5px 0;
            border-radius: 5px;
            transition: 0.3s;
            cursor: pointer;
        }
        .sidebar-item:hover {
            background-color: #ff9800;
            color: black;
        }
        .event-history-btn {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""<div class='menu-bar'>
    <a class='menu-item' href='#'>🏠 Home</a>
    <a class='menu-item' href='#'>📊 Dashboard</a>
    <a class='menu-item' href='#'>⚙️ Settings</a>
    <a class='menu-item' href='#'>🔓 Logout</a>
</div>""", unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-container'>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-title'>🔔 Deaf Assistance Dashboard</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📡 Live Alerts</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🔧 Device Settings</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📞 Support</div>", unsafe_allow_html=True)

# Ensure toggle works properly
if "show_history" not in st.session_state:
    st.session_state["show_history"] = False

st.sidebar.markdown("<div class='event-history-btn'>", unsafe_allow_html=True)
if st.sidebar.button("📜 Event History", use_container_width=True):
    st.session_state["show_history"] = not st.session_state["show_history"]
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='header-title'>Deaf Assistance Alert System</div>", unsafe_allow_html=True)

st.markdown("<div class='user-box'>", unsafe_allow_html=True)
st.markdown("<p>👤 Logged in as: <span>John</span></p>", unsafe_allow_html=True)
st.markdown("<p>📅 Last Login: <span>Today</span></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Read the alert from alert.json
def read_alert():
    if os.path.exists("alert.json"):
        with open("alert.json", "r") as f:
            try:
                data = json.load(f)
                return data.get("event", None)
            except json.JSONDecodeError:
                return None
    return None

if "alert" not in st.session_state:
    st.session_state["alert"] = None

latest_event = read_alert()
if latest_event in ["fire", "knock", "default"]:
    st.session_state["alert"] = latest_event

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Display the current alert
if st.session_state.get("alert") == "fire":
    st.markdown("<div class='alert-box fire'>🔥 Fire Detected! 🔥</div>", unsafe_allow_html=True)
elif st.session_state.get("alert") == "knock":
    st.markdown("<div class='alert-box knock'>🚪 Door Knock Detected! 🚪</div>", unsafe_allow_html=True)
elif st.session_state.get("alert") == "default":
    st.markdown("<div class='alert-box no-alert'>✅ No Alerts</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='alert-box no-alert'>✅ No Alerts</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 🔥 Event History with Metrics and Chart
if st.session_state["show_history"]:
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            try:
                history_data = json.load(f)
                df = pd.DataFrame(history_data)

                event_counts = df["event"].value_counts().to_dict()
                fire_count = event_counts.get("fire", 0)
                knock_count = event_counts.get("knock", 0)
                default_count = event_counts.get("default", 0)

                st.markdown("<h2 style='color:#ff9800;'>📊 Event Statistics</h2>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns(3)
                col1.metric("🔥 Fire Events", fire_count, delta=fire_count)
                col2.metric("🚪 Knock Events", knock_count, delta=knock_count)
                col3.metric("✅ Default Events", default_count, delta=default_count)

                st.markdown("<h3 style='color:#ffffff;'>📈 Event Trend</h3>", unsafe_allow_html=True)
                st.bar_chart(df["event"].value_counts())

                st.markdown("<h3 style='color:#ffffff;'>📜 Event Log</h3>", unsafe_allow_html=True)
                st.dataframe(df, use_container_width=True)

            except json.JSONDecodeError:
                st.warning("Error reading history.json")
    else:
        st.warning("No history found.")

time.sleep(2)
st.rerun()

st.markdown("<div class='footer'>Created for the **Deaf Assistance Project** 🛠️</div>", unsafe_allow_html=True)
