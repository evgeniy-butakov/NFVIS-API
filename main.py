import nfvis
import ipaddress
import getpass


def notvalidip(ip_addr, msg):
    try:
        ip = ipaddress.ip_address(ip_addr)
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
    print (password)
    return url, username, password


def get_payload():
    return ("this is paylad from function get_payload()")


api = nfvis.API()
api.url, api.username, api.password = getcreds()
api.payload = "payload sample"

try:
    status_code,response = api.query("get_image_status", "xml", "128T-5.0.0", "")
    print (status_code)
    print(str(response,'utf8'))
except KeyError:
    print("No such command!")
except TypeError:
    print("Argument error")
except ConnectionError:
    print("ConnectionError")
except:
    print("Something went wrong")
