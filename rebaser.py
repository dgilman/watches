import os
from lxml import etree
import apt_pkg
import subprocess

apt_pkg.init()

class Version(object):
   def __init__(self, ver):
      self.ver = ver

   def __cmp__(self, other):
      return apt_pkg.version_compare(self.ver, other.ver)

   def __str__(self):
      return self.ver

local_watches = {}
for filename in os.listdir('sepwatch/watchfiles'):
   if not filename.endswith('.watch'):
      continue
   pkgname = filename[:-6]
   package, _, version = pkgname.partition('_')
   version = Version(version)
   if package in local_watches:
      if version > local_watches[package][0]:
         local_watches[package] = (version, filename)
   else:
      local_watches[package] = (version, filename)


t = etree.parse('http://lintian.debian.org/tags/debian-watch-file-is-missing.html')
TEST_XPATH = '//xhtml:h2[@class="tag" and not(xhtml:span)]/xhtml:a/text()'

os.chdir('sepwatch')
for missing_watches in t.xpath(TEST_XPATH, namespaces={'xhtml': 'http://www.w3.org/1999/xhtml'}):
   package_name, package_version = missing_watches.split()
   if package_name not in local_watches:
      continue
   if package_version[1] == ':': # strip epoch
      package_version = package_version[2:]
   debian_version = Version(package_version)
   if debian_version > local_watches[package_name][0]:
      subprocess.check_call(['git', 'mv', 'watchfiles/' + local_watches[package_name][1],
         'watchfiles/' + package_name + '_' + package_version + '.watch'])

