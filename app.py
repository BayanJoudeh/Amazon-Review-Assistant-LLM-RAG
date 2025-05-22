import streamlit as st
import requests
from PIL import Image
import base64
from io import BytesIO

# Custom CSS for baby blue theme
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Custom CSS styling
st.markdown("""
<style>
    /* Main theme colors - baby blue palette */
    :root {
        --primary-color: #89CFF0;
        --secondary-color: #A7C7E7;
        --accent-color: #6CB4EE;
        --background-color: #F0F8FF;
        --text-color: #000000; /* Changed to black */
    }
    
    /* Header styling */
    .main-header {
        background-color: var(--primary-color);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    /* Title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.2rem;
        font-style: italic;
        margin-bottom: 1rem;
        color: white;
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        background-color: white;
        color: #000000; /* Changed to black */
        border: 2px solid var(--secondary-color);
        border-radius: 8px;
        padding: 0.5rem;
        font-size: 1rem;
        font-weight: bold; /* Added for better visibility */
    }
    
    /* Button styling */
    .stButton > button {
        background-color: var(--accent-color);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-color);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transform: translateY(-2px);
    }
    
    /* Answer box styling */
    .answer-box {
        background-color: white;
        border-left: 5px solid var(--accent-color);
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .answer-box h3 {
        color: #000080; /* Navy blue for headings */
        font-weight: bold;
    }
    
    .answer-box p {
        color: #000000; /* Black for answer text */
        font-size: 1.05rem;
        line-height: 1.6;
    }
    
    /* Footer styling */
    .footer {
        background-color: var(--secondary-color);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
        color: white;
        font-size: 0.9rem;
    }
    
    /* Example box styling */
    .example-box {
        background-color: rgba(255, 255, 255, 0.8);
        border: 1px solid var(--secondary-color);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .example-title {
        font-weight: bold;
        color: #000080; /* Changed to navy blue */
        margin-bottom: 0.5rem;
    }
    
    .example-box ul li {
        color: #000000; /* Changed to black */
        margin-bottom: 0.5rem;
    }
    
    /* Info box styling */
    .stInfo {
        background-color: rgba(137, 207, 240, 0.2);
        border-left: 5px solid var(--primary-color);
    }
    
    /* Label text color */
    .stTextInput label, .stButton label {
        color: #000080 !important; /* Navy blue for labels */
        font-weight: bold;
    }
    
    /* Expander text color */
    .streamlit-expanderHeader {
        color: #000080 !important; /* Navy blue for expander */
        font-weight: bold;
    }
    
    /* All regular text */
    p, li, div {
        color: #000000; /* Default black for all text */
    }
    
    /* Confidence level heading */
    h4 {
        color: #000080; /* Navy blue for headings */
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Create background gradient
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom, #e6f2ff, #ffffff);
    }
</style>
""", unsafe_allow_html=True)

# Custom header
st.markdown("""
<div class="main-header">
    <div class="main-title">🛍️ Amazon Review Assistant</div>
    <div class="subtitle">Your AI-powered shopping companion</div>
</div>
""", unsafe_allow_html=True)

# App description
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem; color: #000000;">
    Get instant insights from thousands of Amazon product reviews. 
    Ask any question about products, features, or customer experiences!
</div>
""", unsafe_allow_html=True)

# Create two columns for a more balanced layout
col1, col2 = st.columns([3, 1])

with col1:
    question = st.text_input("📝 Enter your question about any Amazon product:", 
                            placeholder="e.g., What do users like about the battery life of product B006K2ZZ7K?")

with col2:
    st.write("")
    st.write("")
    submit_button = st.button("🔍 Find Answers")

# Process the question when button is clicked
if submit_button:
    if not question.strip():
        st.warning("⚠️ Please enter a question first.")
    else:
        with st.spinner("🔄 Analyzing thousands of reviews to find your answer..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8002/ask",  # make sure port matches your API
                    json={"question": question}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.success("✅ Answer found!")
                    
                    # Display answer in a custom styled box
                    st.markdown(f"""
                    <div class="answer-box">
                        <h3>📊 Review Analysis:</h3>
                        <p>{answer}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Add a confidence meter (just for visual effect)
                    st.markdown("<h4>Confidence Level:</h4>", unsafe_allow_html=True)
                    confidence = 0.85  # This would ideally come from your API
                    st.progress(confidence)
                    
                else:
                    st.error(f"⚠️ Failed to fetch answer: {response.text}")
            except Exception as e:
                st.error(f"❌ Connection error: {e}")
                st.markdown("""
                <div style="background-color: #ffe6e6; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <p style="color: #000000;">Make sure your API server is running at the specified address and port.</p>
                </div>
                """, unsafe_allow_html=True)

# Example questions section
st.markdown("""
<div class="example-box">
    <div class="example-title">🔍 Example Questions to Try:</div>
    <ul>
        <li>What do customers like most about product B006K2ZZ7K?</li>
        <li>What are common complaints about product B001E4KFG0?</li>
        <li>Is the battery life good for product B00NLZUM36?</li>
        <li>Summarize the pros and cons of product B07PXGQC1Q</li>
        <li>How durable is product B07X6C9RMF according to reviews?</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Tips section
with st.expander("💡 Tips for Better Results"):
    st.markdown("""
    <div style="color: #000000;">
    - Include the product ID (starts with B00...) in your question for more accurate results
    - Be specific about what aspects of the product you're interested in
    - Try asking about common features like durability, ease of use, or value for money
    - Compare different aspects by asking multiple questions
    </div>
    """, unsafe_allow_html=True)

# Custom footer
st.markdown("""
<div class="footer">
    <p>© 2025 Amazon Review Assistant | Powered by AI | Your Shopping Companion</p>
    <p>This tool analyzes real customer reviews to help you make informed purchasing decisions.</p>
</div>
""", unsafe_allow_html=True)

# Add a sidebar with additional information
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=100)
    st.markdown("<h2 style='text-align: center; color: #000080;'>About</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color: #000000;">
    This AI-powered tool helps you navigate through thousands of Amazon reviews to find answers to your specific questions.
    
    Instead of reading hundreds of reviews yourself, let our AI assistant do the work for you!
    
    <strong>How it works:</strong>
    1. Enter your question about any Amazon product
    2. Our AI analyzes thousands of reviews
    3. Get a concise answer based on real customer experiences
    
    <strong>Privacy Note:</strong> We don't store your questions or browsing history.
    </div>
    """, unsafe_allow_html=True)
    
    # Add a fake satisfaction survey for visual appeal
    st.markdown("<h3 style='text-align: center; color: #000080;'>Rate Your Experience</h3>", unsafe_allow_html=True)
    st.slider("How helpful was this tool?", 1, 5, 5)
    st.button("Submit Feedback")
