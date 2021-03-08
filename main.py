import nfvis
import ipaddress
import getpass
import xml.etree.ElementTree as ET
import os


def notvalidip(ip_addr, msg):
    try:
        ipaddress.ip_address(ip_addr)
        return False
    except:
        return True


def get_section(file, section):
    print(file)
    # This function returns xml configuration block(s) and number of blocks based on configuration file and section name
    tree = ET.parse(file)
    root = tree.getroot()
    sections_list = []
    output_list = []
    payload = ""
    ### Building configuration sections list
    for i in root:
        item = i.tag
        sections_list.append(item)
    # Getting index of requested configuration section
    index = sections_list.index(section)

    for config_items in root[index]:
        result = ""
        result = "\n\t" + str(ET.tostring(config_items), 'utf-8')
        output_list.append(result)

    for i in output_list:
        payload += i

    return len(payload), payload

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


#def get_payload():
#    return "this is payload from function get_payload()"

print(get_section("configuration.xml", "banners"))
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
