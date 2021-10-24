import random
import numpy as np
import re
a = "not 404 found 張三 99 深圳"
res=re.findall('\d+|[]A-Za-z]+',a)
print(res)