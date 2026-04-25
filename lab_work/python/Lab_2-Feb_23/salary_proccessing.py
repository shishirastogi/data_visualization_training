def process_salaries(salaries, min_wage=30000):
    filtered = [s for s in salaries if s >= min_wage]
    updated = [round(s * 1.05, 2) if s > 50000 else s for s in filtered]
    sorted_salaries = sorted(updated, reverse=True)
    
    return sorted_salaries[:3]

salaries = [25000, 45000, 55000, 60000, 32000, 75000, 15000]
print(process_salaries(salaries))