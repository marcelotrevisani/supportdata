# -*- coding: utf-8 -*-


def download_file(url, md5hash, d):
    """ Download data file from web

        IMPROVE it to automatically extract gz files
    """
    download_block_size = 2 ** 16

    assert type(md5hash) is str

    if not os.path.exists(d):
        os.makedirs(d)

    hash = hashlib.md5()

    fname = os.path.join(d, os.path.basename(urlparse(url).path))
    if os.path.isfile(fname):
        h = hashlib.md5(open(fname, 'rb').read()).hexdigest()
        if h == md5hash:
            print("Was previously downloaded: %s" % fname)
            return
        else:
            assert False, "%s already exist but doesn't match the hash: %s" % \
                    (fname, md5hash)

    remote = urlopen(url)

    with NamedTemporaryFile(delete=False) as f:
        try:
            bytes_read = 0
            block = remote.read(download_block_size)
            while block:
                f.write(block)
                hash.update(block)
                bytes_read += len(block)
                block = remote.read(download_block_size)
        except:
            if os.path.exists(f.name):
                os.remove(f.name)
                raise

    h = hash.hexdigest()
    if h != md5hash:
        os.remove(f.name)
        print("Downloaded file doesn't match. %s" % h)
        assert False, "Downloaded file (%s) doesn't match with expected hash (%s)" % \
                (fname, md5hash)

    shutil.move(f.name, fname)
    print("Downloaded: %s" % fname)
