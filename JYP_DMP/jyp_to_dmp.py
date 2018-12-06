import pymssql
from JYP_DMP.to_db import *
from datetime import datetime, timedelta

engine_JYP = pymssql.connect(host="10.1.2.122", user="JYPRIME_READ", password="JYPRIME_READ", database="JYPRIME")
engine_DMP = pymssql.connect(host="10.1.8.148", user="dmp", password="ABcd1234", database="dataTrace")
engine_DMP_test = pymssql.connect(host="10.1.5.98", user="sa", password="ABcd1234", database="dataTrace_test")



class JYP:
    def __init__(self):
        # 测试库
        # self.conn = pymssql.connect(host='10.1.5.121', user='dmp', password='123456', database='JYPRIME')
        # 正式库
        self.conn = pymssql.connect(host='10.1.2.122', user='JYPRIME_READ', password='JYPRIME_READ', database='JYPRIME')
        # , charset="utf8"
        self.cur = self.conn.cursor()

    def get(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.conn.close()


class DMP:
    def __init__(self):
        # 测试库
        # self.conn = pymssql.connect(host='10.1.5.98', user='sa', password='ABcd1234', database='dataTrace_test')
        # 正式库
        self.conn = pymssql.connect(host='10.1.8.148', user='dmp', password='ABcd1234', database='dataTrace')
        # , charset="utf8"
        self.cur = self.conn.cursor()

    def exec(self, sql):
        self.cur.execute(sql)
        self.conn.commit()  # 修改数据后提交事务

    def get(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.conn.close()


def now_time(a=0):
    now = datetime.now()
    delta = timedelta(minutes=a)
    n_days = now + delta
    cc = n_days.strftime('%Y-%m-%d %H:%M:%S')
    return cc




def all_data_to_table(table):
    """
    table: 'FinanceFZB'/'FinanceXJB'/'FinanceLRB'
    全量插入需要把原来表内（FinanceFZB）数据清空再批量插入，
    判断是否存在再插入可能耗时更久

    """

    table_dict = {'FinanceFZB': 'usrMGCWZCFZB',
                  'FinanceXJB': 'usrMGCWXJLLB',
                  'FinanceLRB': 'usrMGCWLRFPB'}

    del_sql = "DELETE FROM [trace].[{}]".format(table)
    d = DMP()
    d.exec(del_sql)
    sql_all = "SELECT ID,IGSDM,GSXZ,CWKM,XMMC,XMZWMC,SSLB,XGSJ FROM dbo.{}".format(table_dict.get(table))
    df_all = pd.read_sql(sql_all, engine_JYP)
    df_all['XMZWMC'] = df_all['XMZWMC'].apply(lambda x: re.sub("’ |'|\\n|", "", x) if type(x) is str else x)
    df_all['XMMC'] = df_all['XMMC'].apply(lambda x: re.sub("’ |'", "", x) if type(x) is str else x)
    df_all['CWKM'] = df_all['CWKM'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    df_all['SSLB'] = df_all['SSLB'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    df_all['GSXZ'] = df_all['GSXZ'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    in_to_sql('dataTrace', 'trace', table,
              engine_DMP, df_all, chunksize=1000)



def logtime_data(table):
    """

    :param table: 'FinanceFZB'/'FinanceXJB'/'FinanceLRB'
    :return: 增量查询插入数据
    """
    table_dict = {'FinanceFZB': 'usrMGCWZCFZB',
                  'FinanceXJB': 'usrMGCWXJLLB',
                  'FinanceLRB': 'usrMGCWLRFPB'}
    # 获取时间从updateLog
    sql_time = "SELECT top 1 UPDATETIME from [trace].[updateLog] " \
               "where TABLENAME='FinanceFZB' order by UPDATETIME desc"
    time = pd.read_sql(sql_time, engine_DMP).iloc[0][0]

    sql_in = "SELECT ID,IGSDM,GSXZ,CWKM,XMMC,XMZWMC,SSLB,XGSJ FROM dbo.{table} where XGSJ > '{time}'" \
        .format(table=table_dict.get(table), time=time)
    df = pd.read_sql(sql_in, engine_JYP)
    df['XMMC'] = df['XMMC'].apply(lambda x: re.sub("’ |'|（|）|-|—|\n|\t|\r|/|:|;|.|？a|¡|¯|ª| |¤", "", x))
    df['XMZWMC'] = df['XMZWMC'].apply(lambda x: re.sub("’ |'", "", x) if type(x) is str else x)
    df['CWKM'] = df['CWKM'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    df['SSLB'] = df['SSLB'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    df['GSXZ'] = df['GSXZ'].apply(lambda x: str(int(x)) if type(x) is float and x >= 0 else x)
    up_to_sql('dataTrace', 'trace', table,
              engine_DMP, df, zhu=['ID'])

    # 在updatelog插入时间
    sql = "INSERT INTO [trace].[updateLog] " \
          "SELECT '{table}', CONVERT(varchar(100), GETDATE(), 20),'{count}'".format(table=table, count=len(df))

    d = DMP()
    d.exec(sql)


def main():
    # 全量写入， 需要时再启动操作会发生大量删除需要注意
    # all_data_to_table('FinanceFZB')
    # all_data_to_table('FinanceXJB')
    # all_data_to_table('FinanceLRB')

    # 增量
    logtime_data('FinanceFZB')
    logtime_data('FinanceXJB')
    logtime_data('FinanceLRB')


if __name__ == '__main__':
    main()




