import nfvis
import ipaddress
import getpass
import xml.etree.ElementTree as ET
import os

config = "configuration.xml"


def notvalidip(ip_addr, msg):
    try:
        ipaddress.ip_address(ip_addr)
        return False
    except:
        return True


def get_section(section):
    #print(config)
    # This function returns xml configuration block(s) and number of blocks based on configuration file and section name
    tree = ET.parse(config)
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
    # print(payload)
    return payload


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


api = nfvis.API()
api.url, api.username, api.password = getcreds()
# api.payload = get_seсtion()

try:

    # status_code, response = api.query("put_banner", None, get_section(config, "banners"))
    # status_code, response = api.query("get_settings")
    # status_code, response = api.query("image_reg", None, get_section(config, "image"))
    status_code, response = api.query("get_image_status", "128T-5.0.0", "","json")
    #status_code, response = api.query("delete_syslog", "163.185.18.27")
    #status_code, response = api.query("configure_syslog",None,get_section("syslog"))

    print(status_code,", ",response)


except KeyError:
    print("No such command!")
except TypeError:
    print("Argument error")
except ConnectionError:
    print("ConnectionError")
except:
    print("Something went wrong")
