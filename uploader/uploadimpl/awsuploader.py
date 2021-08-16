import logging
import os
import threading

import boto3

from uploader.uploadimpl.uploaderbase import UploaderBase


class AwsUploader(UploaderBase):

    def __init__(self):
        self.client = boto3.client('s3',
                                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                                   aws_secret_access_key=os.getenv('AWS_SECRET_KEY'))
        self.bucket = os.getenv('AWS_BUCKET')

    def upload(self, file_path: str, file_key: str) -> bool:
        print(f'thread: {threading.currentThread().getName()} started upload for file {file_key}')
        stat = os.stat(file_path)
        file_permissions = stat.st_mode
        file_last_modified = stat.st_mtime
        try:
            self.client.upload_file(file_path,
                                    self.bucket,
                                    file_key,
                                    extra_args={'Metadata': {'last_modified': file_last_modified,
                                                             'permissions': file_permissions}
                                    })
        except Exception as e:
            logging.error(e)
            return False

        return True

