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
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stTextInput input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
        }
        .stDataFrame {
            border: 2px solid #ddd;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Streamlit Dashboard
# -------------------------
st.title("🎓 Student College Allotment Dashboard")
st.markdown("Welcome! Enter your **Student ID** below to view your allotment details.")

# Input box for Student ID
student_id = st.text_input("🔑 Enter Student ID:")

if student_id:
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
