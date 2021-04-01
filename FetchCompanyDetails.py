import requests
import argparse

# function is looking for MAC address by the user
def Arguments_by_user():
    # It provides a command line interface to the user
    parser = argparse.ArgumentParser()

    #MAC address is required as an input
    parser.add_argument("-m", "--macaddress",
                        dest="mac_address",
                        help="MAC Address of the device. "
                        )
    options = parser.parse_args()

    #Below condition is checking is the address is given
    if options.mac_address:
        return options.mac_address
    else:
        parser.error("[!] Please write command correctly"
                     "Use --help for more details.")


def Req_details(mac_address):
    # Provide url and apikey to fetch commpany details
    url = "https://api.macaddress.io/v1?apiKey=at_SoUgERBdjgXBpyWK25dw8Ix0tKBwL&output=json&search="

    # Request company details using apikey
    response = requests.get(url + mac_address)

    if response.status_code != 200:
        raise Exception("MAC Addressis not valid!")
    return response.content.decode()


if __name__ == "__main__":
    mac_address = Arguments_by_user()
    print("[+] Checking Details...")

    try:
        details = Req_details(mac_address)
        print("[+] Device vendor is " + details)
    except:
        #if something goes wrong it will throw an exception
        print("An error appeared! Please check if there are no spaces in the mac address")
