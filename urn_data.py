uri_data = {

            "get_routes": ["%s/api/config/system/routes%s" % (self.url, self.data), "data", "GET"],
            "get_settings": ["%s/api/config/system/settings?deep%s" % (self.url, self.data), "collection", "GET"],
            "get_image_status": ["%s/api/operational/vm_lifecycle/opdata/images/image/%s" % (self.url, self.data),
                                 "data", "GET"]