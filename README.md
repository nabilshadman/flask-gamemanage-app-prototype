# GameManage

## Overview
GameManage is a full-stack web application that serves as your centralized gaming hub, allowing you to manage your game collection, discover new titles, and connect with fellow gamers. Experience the live prototype [here](https://pacific-destiny-391109.ue.r.appspot.com/).

## Technology Stack
- Backend: Python/Flask
- Frontend: HTML, Bootstrap
- Development: GitLab, GitHub
- Deployment: Google Cloud Platform (formerly Heroku)
- Design: Lucidchart, Figma

## Documentation
Comprehensive documentation covering requirements, design, planning, implementation, testing, and review is available in our [project wiki](https://github.com/nabilshadman/flask-gamemanage-app-prototype/wiki). Note that the repository and wiki have been migrated from GitLab to GitHub, and deployment has transitioned to Google Cloud Platform.

## Local Development Setup

### Prerequisites
- Python 3.9 or higher ([Download](https://www.python.org/downloads/))

#### Platform-Specific Installation Guides
- [Linux Installation Guide](https://docs.python-guide.org/starting/install3/linux/)
- [macOS Installation Guide](https://python.tutorials24x7.com/blog/how-to-install-python-3-9-on-mac)
- [Windows Installation Guide](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

### Getting Started

1. Clone the Repository
```bash
# SSH
git clone git@github.com:nabilshadman/flask-gamemanage-app-prototype.git

# or HTTPS
git clone https://github.com/nabilshadman/flask-gamemanage-app-prototype.git

# Navigate to project directory
cd gamemanage-app-prototype
```

2. Set Up Virtual Environment
```bash
# Create virtual environment
# Linux/macOS
python3 -m venv venv

# Windows
py -3 -m venv venv

# Activate virtual environment
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Install Dependencies
```bash
# Install Flask
pip install Flask

# Install project dependencies
pip install -r requirements.txt
```

4. Launch Application
```bash
# Linux/macOS
export FLASK_APP=app
flask run

# Windows PowerShell
$env:FLASK_APP = "app"
flask run
```

For detailed Flask configuration and running options, consult the [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/).

### Contributing
When adding new dependencies, please update the requirements file:
```bash
pip freeze > requirements.txt
```

## Additional Resources
- [Flask Installation Guide](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [Flask Quickstart Guide](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

## License  
This project is licensed under the MIT License. See the [LICENSE](./LICENSE.txt) file for details.  

## Citation  
If you use this work in your research, please cite:  

```bibtex  
@misc{gamemanage-app,
  author = {Shadman, Nabil and Chan, Tom},
  title = {GameManage: Centralized Gaming Hub},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/nabilshadman/flask-gamemanage-app-prototype}
}
