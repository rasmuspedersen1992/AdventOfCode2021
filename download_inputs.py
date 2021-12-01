import requests
# https://adventofcode.com/2021/day/1/input

session_id = '...'
curYear = 2021
curDay = 2
response = requests.get(f"https://adventofcode.com/{curYear}/day/{curDay}/input",
            cookies={'session': session_id})
print(response.status_code)

filename = f'inputs\\day{curDay}.txt'
with open(filename,'w') as f:
    f.write(response.text)