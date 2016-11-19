# -*- coding: utf-8 -*-

import os
import sys
import shutil
from tempfile import NamedTemporaryFile
if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from urllib.parse import urlparse
else:
    from urllib2 import urlopen
    from urlparse import urlparse


def download_file(outputdir, url, filename, md5hash=None):
    """ Download data file from a URL

        IMPROVE it to automatically extract gz files
    """
    assert os.path.exists(outputdir)

    download_block_size = 2 ** 16

    #assert type(md5hash) is str

    #hash = hashlib.md5()

    src = os.path.join(url, filename)
    fname = os.path.join(outputdir, filename)

    #fname = os.path.join(outputdir, os.path.basename(urlparse(url).path))
    #if os.path.isfile(fname):
    #    h = hashlib.md5(open(fname, 'rb').read()).hexdigest()
    #    if h == md5hash:
    #        print("Was previously downloaded: %s" % fname)
    #        return
    #    else:
    #        assert False, "%s already exist but doesn't match the hash: %s" % \
    #                (fname, md5hash)

    remote = urlopen(src)

    with NamedTemporaryFile(delete=False) as f:
        try:
            bytes_read = 0
            block = remote.read(download_block_size)
            while block:
                f.write(block)
                #hash.update(block)
                bytes_read += len(block)
                block = remote.read(download_block_size)
        except:
            if os.path.exists(f.name):
                os.remove(f.name)
                raise

    #h = hash.hexdigest()
    #if h != md5hash:
    #    os.remove(f.name)
    #    print("Downloaded file doesn't match. %s" % h)
    #    assert False, "Downloaded file (%s) doesn't match with expected hash (%s)" % \
    #            (fname, md5hash)

    shutil.move(f.name, fname)
    print("Downloaded: %s" % fname)
