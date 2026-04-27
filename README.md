## Project Structure
- `.github/workflows/`: Contains the CI pipeline (`ci.yml`) for environment verification.
- `.vscode/`: Editor settings for consistent development environment.
- `data/`: Local storage for raw and processed climate datasets (excluded from Git via `.gitignore`).
- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA).
- `scripts/`: Python utility scripts for data processing.
- `src/`: Main source code for the Climate Challenge.
- `tests/`: Unit tests to ensure code quality and reliability.
=======
# Climate Challenge - Week 0

## How to Reproduce the Environment
1. **Clone the repository**: 
   `git clone https://github.com/bethelhemf/climate-challenge-week0.git`
2. **Create a virtual environment**: 
   `python -m venv venv`
3. **Activate the environment**: 
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. **Install dependencies**: 
   `pip install -r requirements.txt`
>>>>>>> main
