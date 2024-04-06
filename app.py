from pathlib import Path
import streamlit as st
from PIL import Image

# https://www.namecheap.com/support/knowledgebase/article.aspx/9737/2208/pointing-a-domain-to-the-heroku-app/

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "The_Resume.pdf"
profile_pic = current_dir / "assets" / "Profilepicture.png"

# General Settings
PAGE_TITLE = "DIGITAL Resume | Jonathan Taylor"
PAGE_ICON = ":wave:"
NAME = "Jonathan Taylor"
DESCRIPTION = "Just Looking For A Job."
EMAIL = "JTayl190@Emich.edu"
LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/jopataylor/",
    "Github": "https://github.com/dubedo580"
}
PROJECTS = {
    # NO PROJECTS FOR NOW
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF, Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section (?)
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/ocet-stream",
    )
    st.write(EMAIL)

# Social Links
st.write("\n")
cols = st.columns(len(LINKS))
for index, (platform, link) in enumerate(LINKS.items()):
    cols[index].write(f"[{platform}]({link})")

# Skills
st.write("\n")
st.subheader("Skills")
st.write(
    """
        - Effective communicator
        - Organized
        - Driven to learn
        - Creative
        - Detail oriented
        - Excel at collaborative relationships
        """
)

# Experience / Qualifications
st.write("\n")
st.subheader("Experience & Qualifications")
st.markdown(
    """
        - **Languages:**&nbsp;&nbsp;&nbsp;&nbsp;Java, Python, Kotlin, PHP, HTML
         
        - **Development**:&nbsp;&nbsp;&nbsp;&nbsp; IntelliJ, Eclipse, Android Studio, Visual Studio Code, Cloud9
        
        - **Database**:&nbsp;&nbsp;&nbsp;&nbsp; MySQL, Firebase, Dynamo, Cassandra
        
        - **General**:&nbsp;&nbsp;&nbsp;&nbsp; Version Control, Agile / Scrum, Microsoft & Google Suites

        - **Course-Work**:&nbsp;&nbsp;&nbsp;&nbsp; Discrete Mathematics, Software Engineering Solutions,  
                                                    Data Structures and Algorithms,  Big Data 1 & 2
        """,
    unsafe_allow_html=True
)

# Projects / Accomplisments
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}({link})]")

# Work History
st.write("\n")
st.subheader("Work History")
st.write("---")

# Job 1
st.write("**Manager | Conor O'Neills**")
st.write("April 2012 - Current")
st.markdown(
    """
        - Manage schedule for over 50 front of house positions, including full and part time staff
        
        - Ensure staff are attentive to customers’ needs and wants while managing the floor
        
        - Manage customer experience, including difficult clientele, to make the customer experience successful
        
        - Responsible for weekly drink inventory, work closely with regional drink representatives
        
        - Ensure correct food storage, handling, and preparation after being trained in food safety
        
    """,
    unsafe_allow_html=True
)

st.write("\n")
st.write("\n")

# Job 2
st.write("**Manager | Northside Grill**")
st.write("August 2017 - May 2023")
st.write(
    """
        - Ensured orders were correct and the customer experience was exemplary 
        
        - Balanced books/transactions at end of service day
        
        - Opened and closed restaurant for the day
        
        - Developed and maintained close relationships with kitchen staff
        
    """
)

