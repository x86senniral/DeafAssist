import streamlit as st
import json
import os
import time

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
        .menu-bar {
            background-color: #1e1e1e;
            padding: 10px 0;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(255,255,255,0.2);
            margin-bottom: 20px;
        }
        .menu-item {
            display: inline-block;
            margin: 0 15px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            text-decoration: none;
            transition: 0.3s;
        }
        .menu-item:hover {
            color: #ff9800;
        }
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #ff4b4b, #ff9800);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
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
        }
        .sidebar-item:hover {
            background-color: #ff9800;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <div class='menu-bar'>
        <a class='menu-item' href='#'>🏠 Home</a>
        <a class='menu-item' href='#'>📊 Dashboard</a>
        <a class='menu-item' href='#'>⚙️ Settings</a>
        <a class='menu-item' href='#'>🔓 Logout</a>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-container'>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-title'>🔔 Deaf Assistance Dashboard</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📡 Live Alerts</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📜 Event History</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🔧 Device Settings</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📞 Support</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='header-title'>Deaf Assistance Alert System</div>", unsafe_allow_html=True)

st.markdown("<div class='user-box'>", unsafe_allow_html=True)
st.markdown("<p>👤 Logged in as: <span>John</span></p>", unsafe_allow_html=True)
st.markdown("<p>📅 Last Login: <span>Today</span></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

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

if st.session_state.get("alert") == "fire":
    st.markdown("<div class='alert-box fire'>🔥 Fire Detected! 🔥</div>", unsafe_allow_html=True)
elif st.session_state.get("alert") == "knock":
    st.markdown("<div class='alert-box knock'>🚪 Door Knock Detected! 🚪</div>", unsafe_allow_html=True)
elif st.session_state.get("alert") == "default":
    st.markdown("<div class='alert-box no-alert'>✅ No Alerts</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='alert-box no-alert'>✅ No Alerts</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

time.sleep(2)
st.rerun()

st.markdown("<div class='footer'>Created for the **Deaf Assistance Project** 🛠️</div>", unsafe_allow_html=True)
