

def player_address():
    address = str.upper(input("What's your address?"))
    return address
def province_check(address):
    provinces = {
        'A': 'Newfoundland',
        'B': 'Nova Scotia',
        'C': 'Prince Edward Island',
        'E': 'New Brunswick',
        'G': 'Quebec',
        'H': 'Quebec',
        'J': 'Quebec',
        'K': 'Ontario',
        'L': 'Ontario',
        'M': 'Ontario',
        'P': 'Ontario',
        'R': 'Manitoba',
        'S': 'Saskatchewan',
        'T': 'Alberta',
        'V': 'British Columbia',
        'X': 'Nunavut or Northwest Territories',
        'Y': 'Yukon'
    }
    user_province = provinces[address[0]]
    if address[1] == 0:
        region = "Rural"
    else:
        region = "Urban"
    return user_province, region


def main():
    while True:
        try:
            address = player_address()
            if len(address) != 6:
                break
            province, region = province_check(address)
            print(f"You are from the province {province}, and you're in a {region} area.")
            break
        except KeyError:
            print("Please Enter a Valid Address")
    
main()