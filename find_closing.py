with open('admin.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="finance-view-history"' in line:
        print(f"finance-view-history at {i+1}")
    if 'id="view-epoint-reports"' in line:
        print(f"view-epoint-reports at {i+1}")
    if 'id="view-kupon"' in line:
        print(f"view-kupon at {i+1}")
