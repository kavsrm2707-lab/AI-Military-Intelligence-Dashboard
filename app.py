import streamlit as st # pyright: ignore[reportMissingImports]

st.set_page_config(
    page_title="AI Military Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Define pages
pages = {
    "Dashboard": [
        st.Page("1_🏠Home.py", title="Home", icon="🏠"),
        st.Page("2_🌎Global_Threat_Map.py", title="Global Threat Map", icon="🌎"),
        st.Page("3_🌎Country_Analysis.py", title="Country Analysis", icon="🌎"),
    ],

    "Analysis": [
        st.Page("4_🎯Attack_Prediction.py", title="Attack Prediction", icon="🎯"),
        st.Page("5_🚨Threat_Level_Prediction.py", title="Threat Level Prediction", icon="🚨"),
        st.Page("6_📈Forecasting.py", title="Forecasting", icon="📈"),
        st.Page("7_🧠AI_Intelligence_Report.py", title="AI Intelligence Report", icon="🧠"),
        st.Page("8_📊Data_Explorer.py", title="Data Explorer", icon="📊"),
    ],

    "System": [
        st.Page("9_⚙️Settings.py", title="Settings", icon="⚙️"),
    ]
}

# Create navigation
pg = st.navigation(pages)

# Run selected page
pg.run()