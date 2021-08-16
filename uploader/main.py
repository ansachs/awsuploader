import concurrent.futures
import os
import resource

from dotenv import load_dotenv

from uploader.filehandler import list_files
from uploader.uploadimpl.awsuploader import AwsUploader


def limit_memory(memory_fraction: float):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    soft_max = memory_fraction * soft
    resource.setrlimit(resource.RLIMIT_AS, (int(soft_max), hard))


if __name__ == '__main__':
    load_dotenv()
    limit_memory(float(os.getenv('MAX_MEMORY_USE')))
    uploader = AwsUploader()
    files = list_files(os.getenv('FILE_DIRECTORY'))

    with concurrent.futures.ThreadPoolExecutor(max_workers=int(os.getenv('MAX_WORKERS'))) as executor:
        for file in files:
            executor.submit(uploader.upload, file_path=file.path, file_key=file.filename)

