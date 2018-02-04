import os
import errno
import logging

"""
Common code (global variables, functions) that will be used by multiple modules of this program
for configuration or functionality
"""

# GDC API base URL
BASE_URL = 'https://api.gdc.cancer.gov/'

# basic HTTP request header
HEADERS = {
    'Content-Type': 'application/json'
}

# total RNA, miRNA files to request
TOTAL_RNA, TOTAL_MIRNA = 12000, 12000

# max file manifests per json list
FILES_PER_LIST = 500

# directory where JSON query parameter for file manifest requests are saved
FILE_LIST_REQ_DIR = os.path.join('json','file-list_req')

# manifest request query JSON file name template
FILE_LIST_REQ_NAME = '%s-seq.json'

# manifest-list JSON files directory
# should be in .gitignore
FILE_LIST_DIR = os.path.join('json','file-list')

# manifest-list file name template
FILE_LIST_NAME = '%s-seq_%s.json'

# absolute directory path to download files to (recommended if project files are stored in
# a space-sensitive location such as a cloud drive directory (Dropbox, OneDrive, etc...)
ABS_DL_DIR = os.path.abspath(os.path.join(os.path.expanduser('~'), 'Downloads', 'GDC_Downloads'))

# relative directory path to download files to
# should be in .gitignore
REL_DL_DIR = 'GDC_Downloads'

# chosen downloads directory
DL_DIR = ABS_DL_DIR

# log file directory
LOG_DIR = 'logs'

# logging level
LOG_LEVEL = logging.DEBUG

# logging message format
LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s:%(message)s'

# logging time format
LOG_TIME_FORMAT = '%H:%M:%S'

# log file name template
LOG_FILE_NAME = 'logfile_%s.log'

# log file name date/time format
LOG_FILE_NAME_TIME = '%m%d-%H%M%S'


def make_dir(directory):
    """
    Recursively create directories so that the directory path provided is created

    :param directory: String directory path to create
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
