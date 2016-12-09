from radiusauth.backends import RADIUSRealmBackend

RADIUS_SERVERS = {
    'client1.myproject.com': ('14.0.90.92', 1812, 'StarRadi0001'),
    'client2.myproject.com': ('radius.client2.com', 1812, 'p@55w0Rd'),
}

class MyRADIUSBackend(RADIUSRealmBackend):
    def get_server(self, realm):
        if realm in RADIUS_SERVERS:
            return RADIUS_SERVERS[realm]
        return None
