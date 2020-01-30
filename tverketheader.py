from lxml import etree


class CommonTemplate(object):

    headers = {"content-type": "text/xml"}
    body = {}

    def __init__(self):
        self.start = etree.Element("REQUEST")
        self.login = etree.SubElement(self.start, "LOGIN")
        self.login.attrib["authenticationkey"] = "760fe1c6be3643dcb51d1762bea44db2"
        self.query = etree.SubElement(self.start, "QUERY")

    def compose_header(self):
        return self.headers

    def compose_body(self):
        self.body = etree.tostring(self.start, pretty_print=False)
        return self.body


class TrafficFlowCompose(CommonTemplate):

    def __init__(self, regionid, county, site, limit=10):
        super().__init__()
        self.query.attrib["objecttype"] = "TrafficFlow"
        self.query.attrib["limit"] = str(limit)
        self.filters = etree.SubElement(self.query, "FILTER")
        self.region = etree.SubElement(self.filters, "EQ")
        self.region.attrib["name"] = "Regionid"  # Stockholm region
        self.region.attrib["value"] = str(regionid)
        self.region.attrib["name"] = "CountyNo"  # Stockholm
        self.region.attrib["value"] = str(county)
        self.region.attrib["name"] = "SiteId"  # Random Site
        self.region.attrib["value"] = str(site)

    def compose_body(self):
        return super(TrafficFlowCompose, self).compose_body()

    def compose_header(self):
        return super(TrafficFlowCompose, self).compose_header()
