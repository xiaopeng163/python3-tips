
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


def download_file():
    if not Check.check_network():
        print("Cannot connect to network")
        return
    if not Check.check_download_url():
        print("Invalid URL")
        return
    if not Check.check_access_allowed():
        print("Cannot access resource (permission denied)")
        return
    if not Check.check_dns():
        print("No DNS")
        return

    return ['c', 'o', 'o', 'l']

if __name__ == "__main__":

    try:
        print(download_file())
    except Exception as e:
        print(e)