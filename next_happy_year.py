years = int(input())

while True:
    years += 1
    str_years = str(years)
    set_years = set(str_years)
    len_years = len(str_years)
    if len(set_years) == len_years:

        break
print(years)
