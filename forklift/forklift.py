# -*- coding: utf-8 -*-

import os
import sys
from sys import stdout
import shutil
import hashlib
from tempfile import NamedTemporaryFile
from six.moves.urllib.request import urlopen


def download_file(outputdir, url, filename=None, md5hash=None, progress=True):
    """ Download data file from a URL

        IMPROVE it to automatically extract gz files
    """
    block_size = 65536

    assert os.path.exists(outputdir)

    if filename == None:
        filename = os.path.basename(url)
    src = os.path.join(url, filename)
    fname = os.path.join(outputdir, filename)

    md5 = hashlib.md5()
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

    file_size = int(remote.headers["Content-Length"])
    print("Downloading: %s (%d bytes)" % (filename, file_size))

    with NamedTemporaryFile(delete=True) as f:
        bytes_read = 0
        for block in iter(lambda: remote.read(block_size), ''):
            f.write(block)
            md5.update(block)
            bytes_read += len(block)

            if progress:
                status = "\r%10d [%6.2f%%]" % (
                        bytes_read, bytes_read*100.0/file_size)
                stdout.write(status)
                stdout.flush()
        if progress:
            print('')

        if md5hash is not None:
            assert md5hash == md5.hexdigest(), \
                    "Downloaded file (%s) doesn't match expected hash (%s)" % \
                    (filename, md5hash)

        if url[-3:] == '.gz':
            fname = fname.replace('.gz','')
            with open(fname, 'wb') as fout:
                fgz = gzip.open(f.name, 'rb')
                for block in iter(lambda: fgz.read(block_size), ''):
                    fout.write(block)
        else:
            shutil.copy(f.name, fname)
        print("Downloaded: %s" % fname)

    #h = hash.hexdigest()
    #if h != md5hash:
    #    os.remove(f.name)
    #    print("Downloaded file doesn't match. %s" % h)
    #    assert False, "Downloaded file (%s) doesn't match with expected hash (%s)" % \
    #            (fname, md5hash)

