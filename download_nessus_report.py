from tenable_io.client import TenableIOClient
from tenable_io.api.scans import ScanExportRequest
from tenable_io.api.models import Scan
import os, re

client = TenableIOClient(access_key='', secret_key='')
scans = {scan.name: scan.id for scan in client.scans_api.list().scans}
scan = client.scan_helper.scans(name_regex=r'.*Test.*')
#scanname.download(scanname,format=ScanExportRequest.FORMAT_NESSUS)
#scan.download(name_regex=r'.*Test/sScan/sAPI.*', format=ScanExportRequest.FORMAT_NESSUS)
scan.download('{Test Scan API}', format=ScanExportRequest.FORMAT_NESSUS)

