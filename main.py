import nfvis
import ipaddress
import getpass


def notvalidip(ip_addr, msg):
    try:
        ipaddress.ip_address(ip_addr)
        return False
    except:
        return True


def getcreds():
    # Gets NFVIS IP Address, Username, and Password
    nfvis_ip = input(" \n What is the IP address of the NFVIS system: ")
    while notvalidip(nfvis_ip, True):
        ## True value of second argument will trigger  an  Error message if entered ip address is invalid
        nfvis_ip = input("What is the IP address of the NFVIS system: ")

    url = "https://" + nfvis_ip
    # username = input("Username: ")
    username = "ebutakov"
    print(username, ", Enter your  password.")
    password = getpass.getpass()
    return url, username, password


def get_payload():
    return "this is payload from function get_payload()"


api = nfvis.API()
api.url, api.username, api.password = getcreds()
api.payload = get_payload()

try:
    status_code, response = api.query("get_routes")
    print(status_code)
    print(response)

except KeyError:
    print("No such command!")
except TypeError:
    print("Argument error")
except ConnectionError:
    print("ConnectionError")
except:
    print("Something went wrong")
