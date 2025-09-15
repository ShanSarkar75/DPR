# DPR

v0.0 - Date Sep 15 2025

A Benchmark Study of Classical and Dual Polynomial Regression (DPR)-Based Probability Density Estimation Techniques

This is a research-oriented repository for **probability distribution function (PDF) estimation, benchmarking, and validation**. It provides synthetic and real-world datasets, comparison metrics, and modular Python implementations of distribution estimation algorithms, including kernel density estimation (KDE), histogram-based methods, and polynomial-based PDF estimation.  

**Includes:**

TensorFlow function for Histogram Density Estimation (tHDE)
TensorFlow function for Kernel Density Estimation (tKDE)
TensorFlow function for Dual Polynomial Regression - Based Probability Density Estimation (DPR)

---

## Directory Structure  

```
ProbFunc
│
├── Data/                               # Input datasets
│   ├── Gaussian-Symmetric.npy          # Generated synthetic data
│   ├── Gaussian-Right-skewed.npy       # Generated synthetic data
│   ├── Gaussian-Left-skewed.npy        # Generated synthetic data
│   ├── Asymmetric-M-Wright-I.npy       # Generated synthetic data
│   ├── Asymmetric-M-Wright-II.npy      # Generated synthetic data
│   ├── Asymmetric-Laplace.npy          # Generated synthetic data
│   └── Systolic_Diastolic_Data.xlsx    # Real patient systolic & diastolic data (2022–2024, anonymized)
│
├── Metrics/                            # Performance comparison metrics
│   ├── SyntheticDataMetrics.csv        # Metrics on synthetic datasets
│   ├── SystolicMetrics.csv             # Metrics for systolic data
│   └── DiastolicMetrics.csv            # Metrics for diastolic data
│
├── Code/                               # Main evaluation code
│   ├── ProbDistFuncAlgorithm_v0_0.ipynb  # Jupyter notebook for evaluation
│   └── Lib/  
│       ├── FontDict.py  
│       ├── DensityEstimate.py  
│       ├── ProbabilityDensityFunction.py  
│       └── DualPolyRegPDF.py  
```

---

## Features  

- Synthetic dataset generation for symmetric and asymmetric distributions  
- Real patient systolic and diastolic dataset (de-identified)  
- Multiple PDF estimation methods:
  - Python SciPy KDE  
  - TensorFlow based Histogram-Density Estimation (tHDE) 
  - TensorFlow based Kernel Density Estimation (tKDE)  : x30 faster than SciPy KDE
  - Dual Polynomial Regression (DPR) Function using tKDE/tHDE as backend for training: >99% less Inference time compared to SciPy KDE   
- Benchmarking and metrics for synthetic and real-world data  

---

## Requirements  

- Python 3.8+  
- NumPy, TensorFlow, SciPy, Pandas, Matplotlib, scikit-learn (for KDE, metrics, and visualization)  
- NumPy version: 1.22.3+
- TensorFlow version: 2.11.0+
- SciPy version: 1.10.0+
Install dependencies with:  
```bash
pip install -r requirements.txt
```

---

## Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ShanSarkar75/DPR.git
   cd ProbFunc
   ```  

2. Open the Jupyter Notebook for evaluation:  
   ```bash
   jupyter notebook Code/ProbDistFuncAlgorithm_v0_0.ipynb
   ```  

3. Modify dataset paths or methods in `Lib/` modules if needed.  

---

## Metrics  

- **SyntheticDataMetrics.csv**: Quantitative comparison of estimation methods on generated datasets  
- **SystolicMetrics.csv** and **DiastolicMetrics.csv**: Performance evaluation on real patient data  

---

## License  

This repository is released under the MIT License.  

## Citation

If you use this code or the data in your research, please cite our preprint:

Shantanu Sarkar, Mousumi Sinha, and Dexter Cahoy.
A Benchmark Study of Classical and Dual Polynomial Regression (DPR)-Based Probability Density Estimation Techniques.
Preprint, Electronic Journal of Statistics.

For any use of the real patient systolic and diastolic data, please also cite Epic Systems Corporation:

Epic Systems Corporation.
Epic Electronic Health Record System.
https://www.epic.com
