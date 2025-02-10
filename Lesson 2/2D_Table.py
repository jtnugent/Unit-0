
def main():
    populations = [
        [106,111,133,221,767, 1766]
        [502,635,809,947,1402,3634,5268]
        [2,2,2,6,13,30,46]
        [163,203,276,408,547,729,628]
        [2,7,26,82,172,307,392]
        [16,24,38,74,167,511,809]
    ]
    continents = [
        "Africa",
        "Asia",
        "Australia",
        "Europe",
        "North America",
        "South America"
    ]

    headers = print(f"{"Year":<10}{"1750":<10}{"1800":<10}\
        {"1850":<10}{"1900":<10}{"1950":<10}\
        {"2050":<10}")
    for row in range(len(populations)):
        print(f"{continents[row]:<19}",end="")
        for column in range(len(populations[0])):
            print(f"{populations[row][column]:<10}",end="")
        print()



main()