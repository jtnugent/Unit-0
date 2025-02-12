def find_average_price(price1,price2):
    return(price1+price2)/2

def cube_volume(side_length):
    volume = side_length**3
    return volume

def main():
    price1 = float(input("What is the price?"))
    price2 = float(input("What is the next price?"))
    avg_price = find_average_price(price1,price2)
    print(f"The average price of {price1} and {price2} is {avg_price:.2f}.")
    print(f"Side Length 4, volume {cube_volume(4)}")

if __name__ == '__main__':
    main()