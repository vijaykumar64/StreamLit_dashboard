import streamlit as st
import pandas as pd

# -------------------------
# Load real allocation dataset
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("allotment_results.csv")  # final allocation dataset
    return df

df = load_data()

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="College Allotment Dashboard",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for better look
# Custom CSS for better look
# Custom CSS for better look
# Custom CSS for better look
st.markdown("""
    <style>
        /* Wrapper fix for Streamlit text input */
        div[data-baseweb="input"] {
            border: 2px solid #4CAF50 !important;
            border-radius: 10px !important;
            background-color: #1e1e1e !important;
            box-shadow: none !important;
        }

        /* Ensure green border stays even on focus */
        div[data-baseweb="input"]:focus-within {
            border: 2px solid #4CAF50 !important;
            box-shadow: 0 0 5px #4CAF50 !important; /* optional glow */
        }

        /* Input field inside */
        .stTextInput input {
            color: white !important;
            background-color: #1e1e1e !important;
            height: 42px !important;
            padding-left: 10px !important;
        }

        /* Button styling */
        div[data-testid="stButton"] > button {
            background: #4CAF50 !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-size: 18px !important;
            height: 40px !important;
            width: 120px !important;
            font-weight: bold !important;
        }
        div[data-testid="stButton"] > button:hover {
            background: #45a049 !important;
        }
        .stButton { text-align: center; }
    </style>
""", unsafe_allow_html=True)


# -------------------------
# Streamlit Dashboard
# -------------------------
st.title("🎓 Student College Allotment Dashboard")
st.markdown("Welcome! Enter your **Student ID** below to view your allotment details.")

# Input box for Student ID
student_id = st.text_input("🔑 Enter Student ID:",placeholder="eg: 5196578828")

# Search button below the input
search = st.button("Search")

if search and student_id:
    result = df[df["Student_ID"].astype(str) == str(student_id)]
    
    if not result.empty:
        st.success("✅ Student Found")
        
        # Show student details in nice format
        student = result.iloc[0]
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**🧑 Name:** {student['Name']}")
            st.markdown(f"**🏅 Rank:** {student['Rank']}")
            st.markdown(f"**🧾 Category:** {student['Caste']}")
        
        with col2:
            st.markdown(f"**🏫 Allotted College:** {student['Allotted College']}")
            st.markdown(f"**📌 Preference Order Used:** {student['Preference_Order_Used']}")
        
        st.markdown("---")
        st.subheader("📊 Full Record")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("❌ Student ID not found in records.")

# Option to show complete dataset
st.markdown("---")
if st.checkbox("📑 Show Full Allocation Data"):
    st.dataframe(df, use_container_width=True)
