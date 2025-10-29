# Markdown Editor

A modern, web-based Markdown editor built with Streamlit that allows you to write, preview, and download Markdown files with ease. Perfect for creating README files, documentation, and blog posts!

![Markdown Editor](https://img.shields.io/badge/Streamlit-Markdown_Editor-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)

## ✨ Features

- **📝 Live Preview**: See your Markdown rendered in real-time as you type
- **📋 Templates**: Pre-built templates for READMEs, projects, and blog posts
- **⚖️ License Integration**: Automatically add license badges and information
- **💾 Custom Downloads**: Download files with custom names
- **🎨 Clean Interface**: Modern, responsive design with Google Fonts

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/markdown-editor.git
cd markdown-editor
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install streamlit
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501` to see the application running.

## 🎯 How to Use

### Basic Usage

1. **Start Writing**: Type your Markdown content in the main text area
2. **Live Preview**: Watch the right panel update in real-time
3. **Download**: Click the download button to save your file

### Using Templates

1. In the sidebar, select a template:
   - **Basic README**: Simple project documentation
   - **Project README**: Comprehensive project overview
   - **Blog Post**: Structured blog content

2. The template will automatically populate the editor

### Adding Licenses

1. Select a license from the sidebar dropdown
2. The editor will automatically:
   - Add a license badge at the top
   - Append license information at the bottom
   - Format everything correctly

### Customizing File Names

1. In the sidebar, enter your desired filename
2. The download button will use this name
3. File extension (.md) is automatically added if missing

## 📁 Project Structure

```
markdown-editor/
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## 🛠️ Customization

### Adding New Templates

Edit the `TEMPLATES` dictionary in `app.py`:

```python
TEMPLATES = {
    "Basic README": "# Project Title\n\n## Description\n\n## Installation\n\n## Usage\n\n## License\n",
    "Project README": "# Project Name\n\n### What it does\n\n### Why it matters\n\n### How to use it\n\n### Screenshots\n\n### License\n",
    "Blog Post": "# Blog Post Title\n\n## Intro\n\n## Main Content\n\n## Conclusion\n\n---\n*Published on …*",
    "Your New Template": "# Your Template Content\n\nAdd your content here..."
}
```

### Adding New Licenses

Extend the `LICENSE_BADGES` and `LICENSE_TEXT` dictionaries:

```python
LICENSE_BADGES = {
    # ... existing licenses
    "Your License": "[![Your License Badge](https://img.shields.io/badge/Your-License-green.svg)](your-link)"
}

LICENSE_TEXT = {
    # ... existing licenses
    "Your License": "This project uses Your License."
}
```

