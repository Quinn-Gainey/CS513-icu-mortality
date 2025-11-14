ICU Mortality Prediction (PhysioNet 2012)
Master’s project replicating—and extending—the PhysioNet/CinC 2012 task: predict in-hospital mortality using only the first 48 hours of ICU data. We parse per-patient TXT files (Time, Variable, Value), aggregate windowed features, and evaluate classic models from class.

Data: PhysioNet Challenge 2012 (Sets A/B + Outcomes-*.txt). Each file = one patient; we build one row per patient.

Problem: Early risk prediction from 6/12/24/48h windows (no leakage beyond the window).

Features: For vitals/labs (HR, MAP, RR, Temp, SpO₂, Urine, WBC, Hgb, Platelets, Glucose, Na, K, Cr, BUN) compute mean/min/max/std/last/count + missingness flags.

Models: Logistic (baseline), CART, C4.5, KNN (L1/L2), Naive Bayes (Gaussian & quantile-binned).

Evaluation: PR-AUC (primary), ROC-AUC, Recall at Precision ≈ 0.80, (optionally) Brier & calibration plots.

Extensions: Early-window ablation, NB discretization, KNN distance/k grid, CART vs C4.5, cost-aware thresholding, missingness as signal, light soft-vote ensemble, subgroup slices (age/ICU type), top-10 “feature-economy” model.



DATA ORGANIZATION 


Per-patient file format
Time,Variable,Value
0,HR,82
0,SysABP,120
0,MAP,85
0.5,HR,86
1,SysABP,118
...


Time: hours since ICU admission (floating point). The dataset is already clipped to the first 48 hours.

Variable: short code for a vital sign, lab, or derived measurement (e.g., HR, SysABP, MAP, RespRate, Temp, SpO2, WBC, Hgb, Glucose, Sodium, Creatinine, etc.).

Value: numeric value as text. Some rows may be non-numeric (rare) or blank; handle robustly.
