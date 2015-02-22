__author__ = 'ned'

class Domain(object):
  def __init__(self,fqdn,ipaddr,ts):
    self.fqdn = fqdn
    self.ipaddr = ipaddr
    self.ts = ts