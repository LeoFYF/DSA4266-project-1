# Installation

**Step 0.** Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html)

**Step 1.** Create a conda environment and activate it

```
conda create --name dsa4266 python=3.10 -y
conda activate dsa4266
```

**Step 2.** Install the required packages

```
pip install tensorflow pandas numpy scikit-learn gdown
```

**Step 3.** Clone the directory

```
git clone https://github.com/LeoFYF/DSA4266-project-1
cd DSA4266-project-1
```

**Step 4.** Download data

```
python setup.py
```
