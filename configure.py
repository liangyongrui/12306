# 必填
# 用户名
USER_NAME = ''
# 密码
USER_PWD = ''
# 出发站
FROM_STATION = '北京西'
# 到达站
TO_STATION = '达州'
# 乘车日期（格式: YYYY-mm-dd）
TRAIN_DATE = '2019-02-02'
# 购票人身份证号
PASSENGERS_ID = ['513721199308106084']
# 票类型（单程:dc 往返:wc）
TOUR_FLAG = 'dc'
#订票策略,1表示必须全部一起预定，2表示可以部分提交
POLICY_BILL = 1

# 选填
# 车次 eg:['G6343','G6212']
TRAINS_NO = ['Z95','T9','K117','K589']
# 座位类别（商务座(9),特等座(P),一等座(M),二等座(O),高级软卧(6),软卧(4),硬卧(3),软座(2),硬座(1),无座(1)）
#SEAT_TYPE_CODE = ['M', 'O', '4', '3', '2', '1']
SEAT_TYPE_CODE = ['3','4']
# 购票人类别（成人票:1,儿童票:2,学生票:3,残军票:4）
PASSENGER_TYPE_CODE = '1'
# 座位选择 eg:['1A','2A'],有多少张票就填多少个,其中，A靠窗，B中间，C过道,D过道,F靠窗
CHOOSE_SEATS = []

# 刷票间隔(单位:s)
QUERY_TICKET_REFERSH_INTERVAL = 0.5

#是否自动识别验证码
IS_AUTO_CHECK_CAPTHCA = True

#是否更新ip池，默认为更新
IS_REFASH_IP_POOL = True
#执行检查任务的线程/进程池大小
THREAD_POOL_SIZE = 20
#采用多线程或多进程,默认多线程
THREAD_OR_PROCESS = True


mail_host = 'smtp.qq.com'
mail_user = '******@qq.com'
mail_pass = '******'
mailto_list = ['example@163.com']

#短信,使用说明：https://cuiqingcai.com/5696.html
ACCOUNT_SID = "DC4c32222717d4daa96bf8b611fd311f66"
# Your Auth Token from twilio.com/console
AUTO_TOKEN = "6b8087bf15572c210298375641f59e6a"
FROM_NUM = '(731) 201-9528'
TO_NUM = '+8617611719722'