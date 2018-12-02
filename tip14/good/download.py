
class Check:

    @classmethod
    def check_network(cls):
        return True

    @classmethod
    def check_download_url(cls):
        return True

    @classmethod
    def check_access_allowed(cls):
        return True

    @classmethod
    def check_dns(cls):
        return False


class ConnectionError(Exception):
    pass


class DownloadURLError(Exception):
    pass


class PermissionError(Exception):
    pass


class DNSError(Exception):
    pass


def download_file():
    if not Check.check_network():
        raise ConnectionError("Cannot connect to network")
    if not Check.check_download_url():
        raise DownloadURLError("Invalid URL")
    if not Check.check_access_allowed():
        raise PermissionError("Cannot access resource (permission denied)")
    if not Check.check_dns():
        raise DNSError("No DNS")


    return ['c', 'o', 'o', 'l']

if __name__ == "__main__":

    try:
        print(download_file())
    except DNSError:
        # check configure DNS
        print('xxxx DNS error')
    except Exception as e:
        print('download error: {}'.format(e))
    print('xxxxxxx')
        