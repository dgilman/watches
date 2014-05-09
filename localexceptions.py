DEBIAN_IS_UPSTREAM = 0
UNSCRIPTABLE_UPSTREAM_WEBPAGE = 1
NO_UPSTREAM_WEBPAGE = 2
CHILIPROJECT_UPSTREAM = 3 # see https://www.chiliproject.org/issues/1332 for resolution
SHA_FINGERPRINTING = 4
DEBIAN_TIME_WARP = 5 # debian is shipping sorce code that hasn't shipped yet
WATCHFILE_IS_MEANINGLESS = 6 # pointless to have a watchfile
GITWEB = 7 # if a generic gitweb scraper is written it can be used
BTS = 8 # a bug is opened in BTS to fix it

overrides = {
   "aptitude": DEBIAN_IS_UPSTREAM,
   "blas": SHA_FINGERPRINTING,
   "cwidget": GITWEB,
   "discover": NO_UPSTREAM_WEBPAGE,
   "dkg-handwriting": DEBIAN_IS_UPSTREAM,
   "libemu": DEBIAN_TIME_WARP,
   "liblockfile": NO_UPSTREAM_WEBPAGE,
   "linux-ntfs": NO_UPSTREAM_WEBPAGE,
   "lvm2": BTS, # 742305
   "mawk": NO_UPSTREAM_WEBPAGE,
   "mpclib": BTS, # 747468
   "netcat": NO_UPSTREAM_WEBPAGE, # actually, there is at http://techno-fandom.org/~hobbit/ but you'll never see a release from them
   "netkit-ftp": NO_UPSTREAM_WEBPAGE,
   "netkit-ntalk": NO_UPSTREAM_WEBPAGE,
   "netkit-rsh": NO_UPSTREAM_WEBPAGE,
   "netkit-rusers": NO_UPSTREAM_WEBPAGE,
   "netkit-rwall": NO_UPSTREAM_WEBPAGE,
   "netkit-rwho": NO_UPSTREAM_WEBPAGE,
   "netkit-telnet": NO_UPSTREAM_WEBPAGE,
   "netkit-tftp": NO_UPSTREAM_WEBPAGE,
   "ntfsdoc": NO_UPSTREAM_WEBPAGE,
   "picon-domains": SHA_FINGERPRINTING,
   "picon-misc": SHA_FINGERPRINTING,
   "picon-news": SHA_FINGERPRINTING,
   "picon-unknown": SHA_FINGERPRINTING,
   "picon-usenix": SHA_FINGERPRINTING,
   "picon-users": SHA_FINGERPRINTING,
   "picon-weather": SHA_FINGERPRINTING,
   "pyew": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "python-pam": NO_UPSTREAM_WEBPAGE,
   "redmine-recaptcha": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "sudo": BTS, # 747473
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
   "xcolors": NO_UPSTREAM_WEBPAGE,
   "xd": DEBIAN_TIME_WARP,
   "xdmf": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xdrawchem": DEBIAN_TIME_WARP,
   "xdvik-ja": NO_UPSTREAM_WEBPAGE,
   "xemacs21": BTS, #744089
   "xemacs21-packages": WATCHFILE_IS_MEANINGLESS,
   "xen": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xerces-c": BTS, #744092
   "xf86-input-multitouch": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xflip": NO_UPSTREAM_WEBPAGE,
   "xfonts-a12k12": NO_UPSTREAM_WEBPAGE,
   "xfonts-ayu": NO_UPSTREAM_WEBPAGE,
   "xfonts-biznet": NO_UPSTREAM_WEBPAGE,
   "xfonts-cronyx": NO_UPSTREAM_WEBPAGE,
   "xfonts-jisx0213": UNSCRIPTABLE_UPSTREAM_WEBPAGE,
   "xfonts-kaname": NO_UPSTREAM_WEBPAGE,
   "xfonts-kappa20": NO_UPSTREAM_WEBPAGE,
   "xfonts-naga10": NO_UPSTREAM_WEBPAGE,
   "xfonts-nexus": NO_UPSTREAM_WEBPAGE,
   "xfonts-scalable-nonfree": WATCHFILE_IS_MEANINGLESS, # there's a script in there to pull the latest versions from the xfree86 cvs repo
   "xgammon": NO_UPSTREAM_WEBPAGE,

}
