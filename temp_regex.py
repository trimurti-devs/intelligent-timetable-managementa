import re

avail_str = 'Mon,Wed,Fri 10:00-17:00'

pattern_days = r'([a-zA-Z,-]+)\s+(\d{1,2}[\.,]?\d{2})\s*[-to]+\s*(\d{1,2}[\.,]?\d{2})'

match = re.search(pattern_days, avail_str)

print(f"match: {match}")

if match:

    print(f"groups: {match.groups()}")
