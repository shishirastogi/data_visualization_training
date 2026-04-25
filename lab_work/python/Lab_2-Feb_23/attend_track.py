def analyze_attendance(data, limit=75):
    report = {}
    for name, rec in data.items():
        pct = (sum(rec) / len(rec)) * 100
        flagged = [rec[0]] + [("Warning!" if rec[i] == 0 and rec[i-1] == 0 else rec[i]) for i in range(1, len(rec))]
        
        report[name] = {
            "Pct": f"{pct:.1f}%",
            "Status": "Low" if pct < limit else "Good",
            "Records": flagged
        }
    return report

data = {
    "Alice": [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    "Bob": [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    "Charlie": [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
}

print(analyze_attendance(data))