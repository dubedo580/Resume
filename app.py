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


# Experience / Qualifications
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
        - Thing 1
        - Thing 2
        - Thing 3
        - Trait 1
        - Trait 2
        - Trait 3        
        """
)

# Skills
st.write("\n")
st.subheader("Skills")
st.write(
    """
        - Skill 1
        - Skill 2
        - Skill 3
        - Skill 4
        - Skill 5
        - Skill 6
        """
)

# Work History
st.write("\n")
st.subheader("Work History")
st.write("---")

# Job 1
st.write("**Job Title | Company Name**")
st.write("Start Date - End Date")
st.write(
    """
        - Responsibility 1 with Description
        - Responsibility 2 with Description
        """
)

# Job 2
st.write("**Job Title | Company Name**")
st.write("Start Date - End Date")
st.write(
    """
        - Responsibility 1 with Description
        - Responsibility 2 with Description
        """
)

# Projects / Accomplisments
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}({link})]")
