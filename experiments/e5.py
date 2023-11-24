ips = ['100.122.133.105', '100.122.133.111']

index = input("Enter the index of the IP you want: ")

match index:
    case '0':
        result = f"{'You chose '}{ips[0]}"
        print(result)
    case '1':
        result = f"{'You chose '}{ips[1]}"
        print(result)

