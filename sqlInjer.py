import config
from lib.core.attrDict import var
from lib.test import test

var.METHOD = config.method
var.URL = config.url
var.PAYLOAD = config.payload
var.PARAM = config.param
var.INJERP = config.injerp
var.RIGHTF = config.rightf

t = test()
# res = t.CurDB()
# res = t.DBs()
# res = t.TBs('security')
# res = t.CBs('security','users')
res = t.Ds('security','users','id')
print(res)
