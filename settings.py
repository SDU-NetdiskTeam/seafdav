from wsgidav.addons.seafile.domain_controller import SeafileDomainController
domaincontroller = SeafileDomainController()

acceptbasic = True
acceptdigest = False
defaultdigest = False

provider_mapping = {}

from wsgidav.addons.seafile.seafile_dav_provider import SeafileProvider
provider_mapping["/dav"] = SeafileProvider()