import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def get(username, password, uri, header):
    response = requests.get(
        uri,
        verify=False,
        auth=HTTPBasicAuth(username, password),
        headers=header,
        timeout=10,
    )
    if response.status_code != 204:
        code = response.status_code
        content = response.content
        return code, content
    else:
        code = response.status_code
        content = "No content"
        return code, content


def put(username, password, uri, header, payload):
    response = requests.put(
        uri,
        verify=False,
        auth=HTTPBasicAuth(username, password),
        headers=header,
        data=payload,
        timeout=10,
    )
    return response.status_code, response


def delete(username, password, uri, header):
    """gets the specified uri and returns: response code, response. """
    response = requests.delete(
        uri,
        verify=False,
        auth=HTTPBasicAuth(username, password),
        headers=header,
        timeout=10,
    )
    return response.status_code, "No Content"


class API(object):

    def __init__(self, url=None, command=None, data="", form=None, username=None, password=None, uri=None, payload=""):
        self.command = command
        self.data = data
        self.url = url
        self.format = form
        self.username = username
        self.password = password
        self.uri = uri
        self.payload = payload

    def query(self, command, form, argument="", payload=""):
        self.command = command
        self.format = form
        self.payload = payload
        if argument:
            self.data = "/" + argument

        uri_data = {

            "get_routes": ["%s/api/config/system/routes%s" % (self.url, self.data), "data", "GET"],
            "get_settings": ["%s/api/config/system/settings?deep%s" % (self.url, self.data), "collection", "GET"],
            "get_image_status": ["%s/api/operational/vm_lifecycle/opdata/images/image/%s" % (self.url, self.data),
                                 "data", "GET"]

        }

        accept = "application/vnd.yang." + uri_data[self.command][1] + "+" + self.format
        content_type = "application/vnd.yang.collection+" + self.format
        header_data = {"Content-type": content_type, "Accept": accept}
        method = uri_data[self.command][2]
        uri = uri_data[self.command][0]

        if method == "GET":
            return get(self.username, self.password, uri, header_data)
        elif method == "PUT":
            return put(self.username, self.password, uri, header_data, self.payload)
        elif method == "DELETE":
            return delete(self.username, self.password, uri, header_data)
        else:
            raise ValueError

        # Returning method , urn and header for the provided command
        # return uri_data[self.command][2], uri_data[self.command][0], header_data
