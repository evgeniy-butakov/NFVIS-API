def get_urn_data(command, url, data):
    uri_data = {

        "get_routes": ["%s/api/config/system/routes%s" % (url, data), "data", "GET"],
        "get_settings": ["%s/api/config/system/settings?deep%s" % (url, data), "data", "GET"],
        "get_image_status": ["%s/api/operational/vm_lifecycle/opdata/images/image%s" % (url, data), "data", "GET"],
        "image_reg": ["%s/api/config/vm_lifecycle/images%s" % (url, data), "data", "POST"]
    }

    return uri_data[command][0], uri_data[command][2], uri_data[command][1]
