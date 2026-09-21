import pandas as pd
import numpy as np

def run_clinical_qc(file_path):
    df = pd.read_csv(file_path)
    issues = []

    # 1. Check for Missing Values in Required Fields
    missing_consent = df[df['consent_signed'].isna() | (df['consent_signed'] == False)]
    for pid in missing_consent['patient_id']:
        issues.append({"patient_id": pid, "issue_type": "Compliance", "details": "Missing or unsigned consent form"})

    # 2. Identify Out-of-Range Clinical Values
    invalid_age = df[(df['age'] < 0) | (df['age'] > 110)]
    for pid in invalid_age['patient_id']:
        issues.append({"patient_id": pid, "issue_type": "Data Anomaly", "details": "Age value out of realistic clinical bounds (0-110)"})

    # 3. Detect Missing Vital Signs
    missing_vitals = df[df['systolic_bp'].isna() | df['diastolic_bp'].isna()]
    for pid in missing_vitals['patient_id']:
        issues.append({"patient_id": pid, "issue_type": "Missing Data", "details": "Incomplete blood pressure readings"})

    # Export Audit Log
    audit_df = pd.DataFrame(issues)
    audit_df.to_csv("qc_audit_report.csv", index=False)
    print(f"QC Complete. Identified {len(issues)} data quality anomalies. Report generated.")
    return audit_df

if __name__ == "__main__":
    run_clinical_qc("raw_clinical_trials.csv")