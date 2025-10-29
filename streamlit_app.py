import streamlit as st

# style 
st.set_page_config(
    page_title="Markdown Editor",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700&display=swap');

    .header-title {
        font-family: 'Nunito', sans-serif;
        color: 
    }
    .stDownloadButton > button {
        background-color: 
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='header-title'>Markdown Editor</h1>", unsafe_allow_html=True)
st.markdown("Write your Markdown, preview it live, and download it as a `.md` file.")

st.sidebar.header("Settings")

# license template 
license_options = [
    "None", 
    "MIT License",
    "Apache License 2.0",
    "GNU GPL v3",
    "GNU LGPL v3",
    "Mozilla Public License 2.0",
    "Creative Commons CC0 (Public Domain)",
    "Creative Commons CC BY 4.0"
]
selected_license = st.sidebar.selectbox("Choose a license:", license_options)

file_name = st.sidebar.text_input("Output file name:", "README.md")

template_choice = st.sidebar.selectbox(
    "Insert a boilerplate template?",
    ["None", "Basic README", "Project README", "Blog Post"]
)

TEMPLATES = {
    "Basic README": "# Project Title\n\n## Description\n\n## Installation\n\n## Usage\n\n## License\n",
    "Project README": "# Project Name\n\n### What it does\n\n### Why it matters\n\n### How to use it\n\n### Screenshots\n\n### License\n",
    "Blog Post": "# Blog Post Title\n\n## Intro\n\n## Main Content\n\n## Conclusion\n\n---\n*Published on …*"
}

LICENSE_BADGES = {
    "MIT License": "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
    "Apache License 2.0": "[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)",
    "GNU GPL v3": "[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)",
    "GNU LGPL v3": "[![License: LGPL v3](https://img.shields.io/badge/License-LGPLv3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)",
    "Mozilla Public License 2.0": "[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)",
    "Creative Commons CC0 (Public Domain)": "[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)",
    "Creative Commons CC BY 4.0": "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)",
    "None": ""
}

LICENSE_TEXT = {
    "MIT License": "This project is licensed under the MIT License.",
    "Apache License 2.0": "Licensed under the Apache License, Version 2.0.",
    "GNU GPL v3": "This project is licensed under the GNU General Public License v3.0 (GPL).",
    "GNU LGPL v3": "This project is licensed under the GNU Lesser General Public License v3.0 (LGPL).",
    "Mozilla Public License 2.0": "This project is licensed under the Mozilla Public License 2.0 (MPL 2.0).",
    "Creative Commons CC0 (Public Domain)": "The content of this project is dedicated to the public domain under Creative Commons CC0 1.0 Universal.",
    "Creative Commons CC BY 4.0": "The content of this project is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).",
    "None": ""
}

if template_choice != "None":
    default_text = TEMPLATES.get(template_choice, "")
else:
    default_text = ""

markdown_text = st.text_area(
    "Write your Markdown here:",
    value=default_text,
    height=350,
    placeholder="# Your Title\n\nYour content here..."
)

final_md = markdown_text

if selected_license != "None":
    badge = LICENSE_BADGES.get(selected_license, "")
    license_info = LICENSE_TEXT.get(selected_license, "")

    final_md = badge + "\n\n" + final_md

    final_md += f"\n\n---\n **License:** {license_info}"

if markdown_text.strip():
    st.markdown("### Live Preview")

    st.markdown(final_md, unsafe_allow_html=True)

    st.download_button(
        label=f"Download {file_name}",
        data=final_md,
        file_name=file_name if file_name.endswith(".md") else f"{file_name}.md",
        mime="text/markdown"
    )
    st.success("Your file is ready for download!")
else:
    st.info("Start typing Markdown above to see the preview and download button.")