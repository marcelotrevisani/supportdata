#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

from supportdata.supportdata import download_file


def test_download_file_nooutput():
    """ download_file requires a valid outputdir
    """
    try:
        download_file('non/existent/path', url=None, filename=None)
    except:
        return
    assert False, "download_file should file if invalid output path"


def test_download_file():
    download_file(
            tempfile.gettempdir(),
            "https://raw.githubusercontent.com/castelao/supportdata/master/LICENSE",
            "LICENSE")
    filename = os.path.join(tempfile.gettempdir(), "LICENSE")
    assert os.path.exists(filename)
    os.remove(filename)


def download_file_md5():
    url = "https://raw.githubusercontent.com/castelao/supportdata/master/LICENSE"
    md5hash = "68153c4036be9d8b8abd02011b5271ff"

    download_file(tempfile.gettempdir(), url, 'LICENSE', md5hash)
    output = os.path.join(tempfile.gettempdir(), 'LICENSE')
    assert os.path.exists(output)
    os.remove(output)

    try:
        download_file(tempfile.gettempdir(), url, 'LICENSE', 'bad hash')
    except:
        return

    assert False, "download_file didn't fail with a bad hash"