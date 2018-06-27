from __future__ import print_function
from flask import Flask, send_file, abort
import io

from apiclient.discovery import build
from apiclient.http import MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools
from gdrivefilesloader import GdriveFilesLoader
import logging

app = Flask(__name__)

'''
    Main api which serves the given file from Google Drive.
'''
@app.route("/dcm/<study>/<series>/<file_name>")
def get_file(study,series,file_name):
    print(file_name)
    files_loader = GdriveFilesLoader()
    file_handle = files_loader.get_file(file_name)
    if file_handle is None:
        print ("File handle is None")
        abort(404)
    return send_file(
        file_handle,
        mimetype='application/dicom')

if __name__ == "__main__":
    logging.getLogger('backoff').addHandler(logging.StreamHandler())
    logging.getLogger('backoff').setLevel(logging.INFO)
    app.run()
