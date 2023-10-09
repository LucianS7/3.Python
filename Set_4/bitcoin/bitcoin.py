import requests
import sys

def main():
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]) > 0:
                n = float(sys.argv[1])
            else:
                sys.exit("Missing command-line argument")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit ("Missing command-line argument")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = response.json()
        bitcoin_price =  float(r["bpi"]["USD"]["rate_float"])
        amount = n * bitcoin_price
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Request Exception")


if __name__ == "__main__":
    main()