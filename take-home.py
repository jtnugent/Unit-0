

def player_address():
    address = str(input("What's your address?"))
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
    print(user_province)



def main():
    address = player_address()
    province,region = province_check(address)