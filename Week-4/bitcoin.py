import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    arguement = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=365afa7db9ae6b67b2f6568317a3ec825a1b835ace4919411f0f6796e1232216")
    response = arguement.json()
    bit_price = response["data"]["priceUsd"]
    total_amount = float(bit_price) * value
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("")
    sys.exit(1)
