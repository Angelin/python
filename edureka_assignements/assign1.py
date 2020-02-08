import sys
import re

ip = sys.stdin.readline()
compiled_pattern = re.compile('^[A-Za-z0-9]{6,12}$')
match_result = compiled_pattern.match(ip)
print(match_result)

d = {"john":40, "peter":45}
print(d.keys())
