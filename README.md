# 🔍 SEO Keyword Research AI Agent

This project is an AI-powered keyword research tool built using Python and Streamlit. It helps users discover **50 high-opportunity keywords** based on a **single seed keyword**, ranked by **high search volume** and **low competition**, enabling better visibility on the first page of Google search results.


## 🚀 Features

- 🔡 **Seed Keyword Input** – Start with a single keyword like “Global Internship”
- 🔁 **Keyword Expansion** – Generates 200+ long-tail keyword variations using smart modifiers
- 📊 **Synthetic Metrics** – Assigns simulated search volume and competition scores (can be upgraded to real-time data via Google Ads API)
- 🧠 **Keyword Scoring** – Ranks keywords using:  
  `Score = Search Volume / (Competition + 1)`
- 🏆 **Top 50 Keywords Output** – Optimized keyword list downloadable as CSV



## 🖼️ Demo

<img width="1732" height="883" alt="Screenshot 2025-07-13 161241" src="https://github.com/user-attachments/assets/4818a33c-5deb-4690-aeee-b32fbc05354c" />



## 📂 File Structure

├── agent.py # Expands the seed keyword with relevant modifiers
├── app.py # Streamlit UI for user interaction
├── googleadds.py # Simulates keyword metrics (volume, competition)
├── utils.py # Ranks keywords based on scoring logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## ⚙️ How It Works

1. User enters a seed keyword (e.g., `global internship`)
2. The tool expands the keyword into 200+ combinations using modifiers (e.g., `global internship remote 2024`)
3. Each keyword is assigned synthetic search volume and competition values
4. Keywords are scored and sorted to identify those with high volume and low competition
5. Top 50 keywords are displayed in a table and can be downloaded


## 📥 Installation

# Clone the repository
git clone https://github.com/mahithachopra/seo-keyword-ai-agent.git
cd seo-keyword-ai-agent

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
🔮 Future Improvements
✅ Integrate real-time Google Ads Keyword Planner API

✅ NLP-based keyword clustering

✅ Keyword trend graphs and score visualizations

✅ Multilingual keyword support

✅ Export to JSON or Excel formats



🙌 Acknowledgments
Created with ❤️ using Python, Streamlit, and creativity for digital marketers and SEO enthusiasts.

📬 Contact
If you have any suggestions, questions, or want to collaborate, feel free to connect:

Lankapalli Mahitha Chopra
📧 mahithachopra.lankapalli@gmail.com
🌐 LinkedIn : www.linkedin.com/in/mahitha-chopra-lankapalli



