import streamlit as st

# Set Page Configurations
st.set_page_config(
    page_title="Prasad Chowdary's Portfolio",
    page_icon=":briefcase:",
    layout="centered",
)

# Main Header
st.title("👨‍💻 Prasad Chowdary's Portfolio")
st.subheader("Frontend Developer | Penetration Tester")

# Contact Section
st.write("---")
st.header("📬 Contact Information")
st.write("- **Email:** pchowdary205@gmail.com")
st.write("- **Full Name:** Chowdary Durga Vara Prasad")
st.write("- **Phone:** +91 8309957874")
st.write("- **DOB:** 02 Nov, 2003")

# Add Resume Download Option
st.write("---")
st.header("📄 Resume")
st.write("Click the button below to download my latest resume:")
with open("PRASAD CHOWDARY__CV2.pdf", "rb") as file:  # Ensure the resume file is in the same directory
    st.download_button(
        label=" 📥 Download Resume",
        data=file,
        file_name="PRASAD CHOWDARY__CV2.pdf",
        mime="application/pdf",
    )

# Languages Known
st.write("---")
st.header("🌐 Languages Known")
st.write("- English")
st.write("- Telugu")

# Technical Skills
st.write("---")
st.header("💻 Technical Skills")
st.write("**Programming Languages**")
st.write("- Advance: Python")
st.write("- Intermediate: C")
st.write("- Novice: JavaScript, Bash")
st.write("**Tools & Technologies**")
st.write("- GIT • Linux • Windows")
st.write("- Django • HTML • CSS • SQL • REACT")

# Education
st.write("---")
st.header("🎓 Education")
st.write("**Kakinada Institute of Engineering & Technology**")
st.write("B. Tech, CSE (2021-25) | Kakinada | CGPA: 7.1")
st.write("**Narayana Junior College**")
st.write("Intermediate, MPC (2019-21) | Rajamundry | Percentage: 88%")
st.write("**Montessori E.M School**")
st.write("SSE (2018-19) | Tallapudi | Percentage: 85.5%")

# Work Experience
st.write("---")
st.header("💼 Work Experience")
st.subheader("Cyber Security Intern - Shadow Fox (Oct 2024 - Nov 2024)")
st.write("- Penetration Test | Wireshark | Brute Force")
st.subheader("Linux Intern - Cyberdosti (Dec 2023 - Jan 2024)")
st.write("- Mastered Linux commands, developed tools like password viewer, phishing link detector.")
st.write("- Used Wireshark, Brute Force, and Maltego for cybersecurity tasks.")
st.subheader("Web Development Intern - Bharat Intern (Oct 2023 - Nov 2023)")
st.write("- Created and cloned Netflix landing page.")
st.write("- Designed a Temperature Converter landing page.")
st.write("- Developed a simple Port Scanner.")

# Projects
st.write("---")
st.header("📂 Projects")
st.subheader("Simple Port Scanner")
st.write("**Problem:** Network administrators struggle with visibility of open ports.")
st.write("**Technology:** Python, Socket")
st.subheader("Real-Time Sentiment Analysis Web App")
st.write("**Utilized:** TF-IDF vectorization and logistic regression for text classification.")
st.write("**Framework:** Streamlit for an interactive interface.")

# Certifications
st.write("---")
st.header("🎓 Certifications")
st.write("- **Cybersecurity Fundamentals** by CISCO")
st.write("- **SQL Basic** by Hackerrank")
st.write("- **Ethical Hacking Essentials** by EC-Council")
st.write("- **Introduction to CyberSecurity** by Great Learning")

# Links
st.write("---")
st.header("🔗 Links")
st.write("[GitHub](https://github.com/prasadchowdary5)")
st.write("[TryHackMe](https://tryhackme.com/pchowdary205)")
st.write("[LinkedIn](https://linkedin.com/in/prasad-chowdary)")
st.write("[Hackerrank](https://hackerrank.com/pchowdary205)")
st.write("[LeetCode](https://leetcode.com/prasadchowdary143)")

# Footer
st.write("---")
st.write("👀 **Explore, Innovate, and Create!** This portfolio reflects my journey and aspirations in tech. Reach out for collaborations or opportunities!")
