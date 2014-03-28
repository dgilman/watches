DEBIAN_IS_UPSTREAM = 0
UNSCRIPTABLE_UPSTREAM_WEBPAGE = 1
NO_UPSTREAM_WEBPAGE = 2
CHILIPROJECT_UPSTREAM = 3 # see https://www.chiliproject.org/issues/1332 for resolution
SHA_FINGERPRINTING = 4
DEBIAN_TIME_WARP = 5 # debian is shipping sorce code that hasn't shipped yet
WATCHFILE_IS_MEANINGLESS = 6 # pointless to have a watchfile
GITWEB = 7 # if a generic gitweb scraper is written it can be used

overrides = {
   "dkg-handwriting": DEBIAN_IS_UPSTREAM,
   "mawk": NO_UPSTREAM_WEBPAGE,
   "netkit-ftp": NO_UPSTREAM_WEBPAGE,
   "netkit-ntalk": NO_UPSTREAM_WEBPAGE,
   "netkit-rsh": NO_UPSTREAM_WEBPAGE,
   "netkit-rusers": NO_UPSTREAM_WEBPAGE,
   "netkit-rwall": NO_UPSTREAM_WEBPAGE,
   "netkit-rwho": NO_UPSTREAM_WEBPAGE,
   "netkit-telnet": NO_UPSTREAM_WEBPAGE,
   "netkit-tftp": NO_UPSTREAM_WEBPAGE,
   "python-pam": NO_UPSTREAM_WEBPAGE,
   "woff-tools": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "woof": SHA_FINGERPRINTING,
   "wordplay": NO_UPSTREAM_WEBPAGE,
   "worklog": NO_UPSTREAM_WEBPAGE,
   "w3-recs": WATCHFILE_IS_MEANINGLESS,
   "wacomtablet": CHILIPROJECT_UPSTREAM,
   "wdg-html-validator": SHA_FINGERPRINTING,
   "webkit-image": NO_UPSTREAM_WEBPAGE,
   "webkitkde": CHILIPROJECT_UPSTREAM,
   "wfrog": DEBIAN_TIME_WARP,
   "whatweb": DEBIAN_TIME_WARP,
   "whiteboard": DEBIAN_IS_UPSTREAM,
   "wikidiff2": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "wims-extra": WATCHFILE_IS_MEANINGLESS,
   "wims-help": WATCHFILE_IS_MEANINGLESS,
   "wims-modules-es": WATCHFILE_IS_MEANINGLESS,
   "wims-moodle": NO_UPSTREAM_WEBPAGE,
   "windows-el": NO_UPSTREAM_WEBPAGE,
   "withsqlite": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "wmail": NO_UPSTREAM_WEBPAGE,
   "wmcalclock": NO_UPSTREAM_WEBPAGE,
   "wmcdplay": NO_UPSTREAM_WEBPAGE,
   "wmii": DEBIAN_TIME_WARP,
   "wmii-doc": NO_UPSTREAM_WEBPAGE,
   "wmlongrun": NO_UPSTREAM_WEBPAGE,
   "wmpinboard": NO_UPSTREAM_WEBPAGE,
   "wmppp.app": NO_UPSTREAM_WEBPAGE,
   "wmressel": NO_UPSTREAM_WEBPAGE,
   "wmtv": NO_UPSTREAM_WEBPAGE,
   "wnn6-sdk": SHA_FINGERPRINTING,
   "wraplinux": GITWEB, # http://git.etherboot.org/wraplinux.git/
   "writer2latex": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "wsdl2c": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "wsil4j": UNSCRIPTABLE_UPSTREAM_WEBPAGE, # http://svn.apache.org/viewvc/webservices/archive/wsil4j/
   "wsjt": DEBIAN_TIME_WARP,
   "wsjtx": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "wwl": NO_UPSTREAM_WEBPAGE,
   "x-pgp-sig-el": NO_UPSTREAM_WEBPAGE,
   "x2": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xapers": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xball": NO_UPSTREAM_WEBPAGE,
   "xbattbar": GITWEB,
   "xbindkeys-config": NO_UPSTREAM_WEBPAGE,
   "xcal": NO_UPSTREAM_WEBPAGE,
   "xcite": SHA_FINGERPRINTING,
   "xcolmix": NO_UPSTREAM_WEBPAGE,



}
