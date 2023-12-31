import hashlib
import time

class tfcg:
    def genCode(key):
        gmt = time.gmtime(time.time())
        strToFormat = f"___{key}__{gmt.tm_hour}_{str(gmt.tm_min)[0]}__{gmt.tm_mday}_{gmt.tm_mon}_{gmt.tm_year}___"
        md5Hash = hashlib.md5(strToFormat.encode()).hexdigest()
        return md5Hash[:6].upper()

    def valCode(code, key):
        gmt = time.gmtime(time.time())
        strToFormat = f"___{key}__{gmt.tm_hour}_{str(gmt.tm_min)[0]}__{gmt.tm_mday}_{gmt.tm_mon}_{gmt.tm_year}___"
        md5Hash = hashlib.md5(strToFormat.encode()).hexdigest()
        return code == md5Hash[:6].upper()
