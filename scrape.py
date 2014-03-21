import sqlite3
from lxml import etree
import os
import urllib
import subprocess

import localexceptions

LINTIAN_WATCH_FILE_IS_MISSING = 0
WATCH_FILE_IN_SEPWATCH = 1
WATCH_FILE_USCAN_ERRORS = 2
LOCAL_WATCHFILE = 3
LINTIAN_WATCH_FILE_IS_MISSING_OVERRIDDEN = 4
LOCAL_OVERRIDE = 5
LINTIAN_WATCH_CONTAINS_DH_MAKE = 6
LINTIAN_WATCH_CONTAINS_DH_MAKE_OVERRIDDEN = 7
LINTIAN_WATCH_MISSING_VERSION = 8
LINTIAN_WATCH_MISSING_VERSION_OVERRIDDEN = 9
LINTIAN_WATCH_PUBKEY_MISSING = 10
LINTIAN_WATCH_PUBKEY_MISSING_OVERRIDDEN = 11
LINTIAN_WATCH_SHOULD_DVERSIONMANGLE = 12
LINTIAN_WATCH_SHOULD_DVERSIONMANGLE_OVERRIDDEN = 13
LINTIAN_WATCH_SHOULD_MANGLE = 14
LINTIAN_WATCH_SHOULD_MANGLE_OVERRIDDEN = 15
LINTIAN_WATCH_SHOULD_USE_SF = 16
LINTIAN_WATCH_SHOULD_USE_SF_OVERRIDDEN = 17
LINTIAN_WATCH_SHOULD_UVERSIONMANGLE = 18
LINTIAN_WATCH_SHOULD_UVERSIONMANGLE_OVERRIDDEN = 19
LINTIAN_WATCH_DEPRECATED_SF = 20
LINTIAN_WATCH_DEPRECATED_SF_OVERRIDDEN = 21
# too pedantic, nobody cares
#LINTIAN_WATCH_MAY_CHECK_GPG = 22
#LINTIAN_WATCH_MAY_CHECK_GPG_OVERRIDDEN = 23
LINTIAN_WATCH_PUBKEY_IS_MISSING = 24
LINTIAN_WATCH_PUBKEY_IS_MISSING_OVERRIDDEN = 25


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def upsert(package, status):
   c.execute('SELECT id FROM packages WHERE name = ?', (package,))
   package_id = c.fetchall()
   if not package_id:
      c.execute('INSERT INTO packages (id, name, status) VALUES (NULL, ?, ?)', (package, status))
      package_id = c.lastrowid
   else:
      package_id = package_id[0][0]
   c.execute('UPDATE packages SET status = ? WHERE id = ?', (status, package_id))
   if package_id == None:
      import pdb; pdb.set_trace()
   return package_id


lintian_results = (('http://lintian.debian.org/tags/debian-watch-contains-dh_make-template.html',
                     LINTIAN_WATCH_CONTAINS_DH_MAKE,
                     LINTIAN_WATCH_CONTAINS_DH_MAKE_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-missing-version.html',
                     LINTIAN_WATCH_MISSING_VERSION,
                     LINTIAN_WATCH_MISSING_VERSION_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-pubkey-file-is-missing.html',
                     LINTIAN_WATCH_PUBKEY_IS_MISSING,
                     LINTIAN_WATCH_PUBKEY_IS_MISSING_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-should-dversionmangle-not-uversionmangle.html',
                     LINTIAN_WATCH_SHOULD_DVERSIONMANGLE,
                     LINTIAN_WATCH_SHOULD_DVERSIONMANGLE_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-should-mangle-version.html',
                     LINTIAN_WATCH_SHOULD_MANGLE,
                     LINTIAN_WATCH_SHOULD_MANGLE_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-should-use-sf-redirector.html',
                     LINTIAN_WATCH_SHOULD_USE_SF,
                     LINTIAN_WATCH_SHOULD_USE_SF_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-should-uversionmangle-not-dversionmangle.html',
                     LINTIAN_WATCH_SHOULD_UVERSIONMANGLE,
                     LINTIAN_WATCH_SHOULD_UVERSIONMANGLE_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-uses-deprecated-sf-redirector-method.html',
                     LINTIAN_WATCH_DEPRECATED_SF,
                     LINTIAN_WATCH_DEPRECATED_SF_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-pubkey-file-is-missing.html',
                     LINTIAN_WATCH_PUBKEY_IS_MISSING,
                     LINTIAN_WATCH_PUBKEY_IS_MISSING_OVERRIDDEN),
                   ('http://lintian.debian.org/tags/debian-watch-file-is-missing.html',
                     LINTIAN_WATCH_FILE_IS_MISSING,
                     LINTIAN_WATCH_FILE_IS_MISSING_OVERRIDDEN))


TEST_XPATH = '//xhtml:h2[@class="tag" and not(xhtml:span)]/xhtml:a/text()'
OVERRIDDEN_XPATH = '//xhtml:h2[@class="tag" and xhtml:span]/xhtml:a/text()'

print 'fetching lintian pages'
for url, test, overridden_test in lintian_results:
   t = etree.parse(url)
   for status_code, xpath in ((test, TEST_XPATH), (overridden_test, OVERRIDDEN_XPATH)):
      hits = t.xpath(xpath, namespaces={'xhtml': 'http://www.w3.org/1999/xhtml'})
      for hit in hits:
         package = hit.split(' ')[0]
         upsert(package, status_code)

print 'updating local watchfiles'
for watch in (x for x in os.listdir('sepwatch/watchfiles') if x.endswith('.watch')):
   package = watch.split('_')[0]
   upsert(package, WATCH_FILE_IN_SEPWATCH)

print 'adding uscan errors'
for watch in urllib.urlopen('http://qa.debian.org/watch/uscan-errors.txt'):
   package = watch.split(' ')[0]
   upsert(package, WATCH_FILE_USCAN_ERRORS)

print 'adding local patches'
os.chdir('sepwatch/watchfiles')
mods = subprocess.check_output(['git', 'log', '--name-only', '--pretty=format:', 'git-svn..'])
for line in mods.splitlines():
   if not line:
      continue
   _, package = line.split('/')
   package = package.split('_')[0]
   upsert(package, LOCAL_WATCHFILE)

print 'adding local exceptions'
for override in localexceptions.overrides:
   upsert(override, LOCAL_OVERRIDE)

print 'updating popcon'
for package_info in urllib.urlopen('http://popcon.debian.org/sourcemax/by_inst'):
   if package_info[0] == '#':
      continue
   package_info = package_info.split()
   try:
      package = package_info[1]
      count = int(package_info[2])
   except:
      continue
   c.execute('SELECT id FROM packages WHERE name = ?', (package,))
   package_id = c.fetchall()
   if not package_id:
      continue
   c.execute('UPDATE packages SET popcon_inst = ? WHERE id = ?', (count, package_id[0][0]))

conn.commit()
conn.close()
