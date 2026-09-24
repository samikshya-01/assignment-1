# Assignment 1: Git, NumPy and Pandas

Assignment 1 for the Leading2AI Data Science with AI/ML course by Samikshya Giri.
It covers Git theory (Part A), NumPy tasks on a weather grid (Part B), and
pandas cleaning and analysis of a messy student scores CSV (Part C).

## Project structure

```
assignment-1/
├── answers/
│   ├── 01_git_theory.md      Part A: written Git answers
│   ├── 02_numpy.ipynb        Part B: NumPy tasks B1-B10
│   └── 03_pandas.ipynb       Part C: pandas tasks C1-C12
├── data/
│   ├── make_data.py          generates the dataset
│   └── scores_raw.csv        raw messy dataset
├── outputs/
│   └── summary.csv           Part C summary table (C12a)
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
```
   git clone https://github.com/samikshya-01/assignment-1.git
   cd assignment-1
```
2. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
```
3. Install dependencies:
```
   pip install -r requirements.txt
```

## Generate the data

```
cd data
python make_data.py
cd ..
```

This writes `data/scores_raw.csv` (126 rows, 7 columns). The seed is fixed, so the file is identical every time.

## Run each part

- **Part A:** open `answers/01_git_theory.md`.
- **Part B:** open `answers/02_numpy.ipynb` in Jupyter or VS Code and click Run All.
- **Part C:** open `answers/03_pandas.ipynb` and click Run All. It also writes `outputs/summary.csv`.

To run a notebook from the terminal:
```
jupyter nbconvert --execute --to notebook --inplace answers/03_pandas.ipynb
```