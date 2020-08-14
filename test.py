import os
import time
VedioDate = time.ctime(os.path.getctime("F:\\mytraffic_cv\\detect_result\\cache\\result.txt"))
print(VedioDate.replace(' ', "_").replace(':', '_').replace('__', '_'))
