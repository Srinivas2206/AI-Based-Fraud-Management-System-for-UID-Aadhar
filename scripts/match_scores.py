import pandas as pd
from matching_logic import name_match, address_match, uid_match

# Paths
EXCEL_PATH = "results/comparison_reports/matching_scores.xlsx"
GROUND_TRUTH_PATH = "data/ground_truth.xlsx"
EXTRACTED_RESULTS_PATH = "results/extracted_text"

# Load data
ground_truth_df = pd.read_excel(GROUND_TRUTH_PATH)

# Match scores
def match_scores():
    results = []
    for idx, row in ground_truth_df.iterrows():
        input_name, input_address, input_uid = row["Name"], row["Address"], row["Aadhaar Number"]
        extracted_name, extracted_address, extracted_uid = row["Extracted Name"], row["Extracted Address"], row["Extracted UID"]
        
        # Calculate scores
        name_score = name_match(input_name, extracted_name)
        address_score = address_match(input_address, extracted_address)
        uid_score = uid_match(input_uid, extracted_uid)
        
        results.append({
            "Name": input_name,
            "Extracted Name": extracted_name,
            "Name Match Score": name_score,
            "Address Match Score": address_score,
            "UID Match Score": uid_score
        })
    
    # Save results to Excel
    results_df = pd.DataFrame(results)
    results_df.to_excel(EXCEL_PATH, index=False)

if __name__ == "__main__":
    match_scores()
