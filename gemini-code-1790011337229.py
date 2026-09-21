import pandas as pd
import numpy as np

# Generate mock patient records with deliberate schema/data quality issues
data = {
    "patient_id": [101, 102, 103, 104, 105, 106, 107],
    "age": [45, -5, 62, np.nan, 29, 150, 34], # Inconsistent & impossible ages
    "systolic_bp": [120, 140, np.nan, 115, 130, 210, 125],
    "diastolic_bp": [80, 90, 85, np.nan, 85, 120, 80],
    "consent_signed": [True, True, False, True, True, True, np.nan],
    "visit_date": ["2026-01-10", "2026-01-11", "invalid_date", "2026-01-12", "2026-01-13", "2026-01-14", "2026-01-15"]
}

df = pd.DataFrame(data)
df.to_csv("raw_clinical_trials.csv", index=False)
print("Synthetic raw clinical dataset generated.")