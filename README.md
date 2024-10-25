# Spearman's Rank Correlation Coefficient Calculator

## Introduction

Spearman's Rank Correlation Coefficient is a non-parametric measure of correlation that assesses the strength and direction of the association between two ranked variables. Unlike Pearson’s Correlation, it does not assume a linear relationship and is suitable for data with non-normal distributions. Spearman's coefficient $ \rho$ ranges between -1 and 1, where:
- $\rho = 1$: Perfect positive correlation.
- $\rho = -1$: Perfect negative correlation.
- $\rho = 0$: No correlation.

## Formula

For data without repeated (tied) values:

$\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$

where:
- $d_i$ is the difference between the ranks of each pair of values,
- $n$ is the number of pairs.

For data with repeated (tied) values, we adjust the formula:

$\rho = 1 - \frac{6 \sum d_i^2 + \sum \left( \frac{t_j^3 - t_j}{12} \right)}{n(n^2 - 1)}$

where:
- $t_j$ represents the number of tied ranks in each group.

## Usage

### Beginner Installation

1. Install the requirements (only once):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the program:
   ```bash
   python spearman_rank.py
   ```

### Advanced Installation (Recommended for Future Runs)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On MacOS/Linux
   venv\Scripts\activate       # On Windows
   ```
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program as desired:
   ```bash
   python spearman_rank.py
   ```
   *Deactivate the environment* after use with `deactivate`.

### Sample Input and Output

There are two files available in this repository with different inputs for repeated and non-repeated values.
