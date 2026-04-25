def process_exams(scores):
    if len(scores) < 2: return []
    
    clean_scores = sorted(scores)[2:]
    adjusted = [s + 5 if 30 <= s <= 35 else s for s in clean_scores]
    pass_count = sum(1 for s in adjusted if s >= 40)
    
    return {"Scores": adjusted, "Pass_Count": pass_count}

data = [25, 32, 45, 15, 88, 34, 41]
print(process_exams(data))