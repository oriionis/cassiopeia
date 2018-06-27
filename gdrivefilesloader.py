from gdriveauthenticate import authenticate_gdrive
from apiclient.http import MediaIoBaseDownload
from httplib2 import Http
from googleapiclient.errors import HttpError
import io
from apiclient import errors
import backoff
'''
    Class which downloads (does not store the file locally) the file FROM
    google drive and serves.
'''
class GdriveFilesLoader(object):
    def __init__(self):
        self.service = authenticate_gdrive()
    '''
        Method to download file from Google drive
    '''
    @backoff.on_exception(backoff.expo, HttpError, max_tries=10)
    def download_file(self, file_id):
        try:
            request = self.service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print ("Download %d%%." % int(status.progress() * 100))
            fh.seek(0)
            return fh
        except HttpError as error:
            if error.resp.status in [403, 500, 503]:
                print 'Rate Error or 500/503 error occurred - Backing Off'
                raise
            return None

    '''
        Gets the File id from the given file name. If found then download the
        contents fo the file and return.
    '''
    @backoff.on_exception(backoff.expo, HttpError, max_tries=10)
    def get_file(self, file_name):
        query = 'name=\"' + file_name + '\"'
        print (query)
        try:
            results = self.service.files().list(q=query,
                fields="files(id, name)").execute()
        except HttpError as error:
            if error.resp.status in [403, 500, 503]:
                print 'Rate Error or 500/503 error occurred - Backing Off'
                raise
            print(str(error))
            return None
        print(results)
        items = results.get('files', [])
        if not items or len(items) <= 0:
            return None
        else:
            return self.download_file(items[0]['id'])
