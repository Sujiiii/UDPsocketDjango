class UdpClient(object):
    pass


def getdata():
    host = "192.168.*.*"  # IP of the server or host.
    port = 13000

    client = UdpClient(host=host, port=port, exit_code="stop")