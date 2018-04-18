import requests,time
from bs4 import BeautifulSoup
import p_mysql,json
class jxy_all():
    def xunhuan(self,gol_cookies):
        wrong = 0
        first_run = 0
        jishu = 0
        toufayu = False
        multiple = [1, 3, 7, 15, 31, 63, 127, 34, 55, 89, 144, 1, 1]
        maxwrong = 6
        global moni
        firstflag_vote = ''
        current_period = ''
        vote_retime = 0
        endf = 1
        wrongflag = False
        vote_list = []
        self.header = {"Accept": "text/html, application/xhtml+xml, */*",
                       "Accept-Encoding": "gzip, deflate",
                       "Accept-Language": "zh-CN",
                       "Connection": "Keep-Alive",
                       "Host": "www.juxiangyou.com",
                       "Referer": "http://www.juxiangyou.com/",
                       "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64;Trident/5.0)"}
        post_head = {"Accept": "application/json, text/javascript, */*; q=0.01",
                     "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-cn",
                     "Cache-Control": "no-cache",
                     "Connection": "Keep-Alive",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "Host": "www.juxiangyou.com",
                     "Referer": "http://www.juxiangyou.com/fun/play/crazy28/index",
                     "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                     "X-Requested-With": "XMLHttpRequest"}
        self.url = 'http://www.juxiangyou.com/fun/play/crazy28/index'
        yinshu = 1
        list_v = []
        czlst = []
        c_time = time.strftime('%m-%d %H:%M', time.localtime(time.time()))
        try:
            req = requests.get(self.url, cookies=gol_cookies, headers=self.header)
            soup = BeautifulSoup(req.text, 'lxml')
            # 查询当前投注信息
            vote_info = soup.find('p', attrs={'class': 'time-static1'})
            # 第一步 找到当前期 这里必然找出当前期，目的是为了投注。
            if vote_info != None:
                if (vote_info.text).find('正在开奖') > 0:
                    print('正在开奖，等待5秒')
                    time.sleep(5)
                else:
                    # 如果没有开奖，则查询当前投注期
                    try:
                        vote_current = vote_info.find_all('span')
                        # 结束标识，查询
                        end_flag = (vote_info.text).find('截止投注')
                        if end_flag > 0:
                            # 即使投注了，当前期也需要展示出来，为投注判断
                            print(vote_current[0].string + '期已经截止投注')
                            current_period = vote_current[0].string
                        else:
                            print('当前期' + vote_current[0].string + '剩余' + vote_current[1].string + '秒投注')
                            vote_retime = int(vote_current[1].string)
                            current_period = vote_current[0].string
                    except Exception as e:
                        print('搜索资料出错，列表错误')
                        print('traceback.format_exc():%s' % traceback.format_exc())
            if current_period != '':
                # 添加保存第一次金币部分
                try:
                    current_jinbi = (soup.find('span', attrs={'class': 'J_udou'}).string).replace(',', '')
                except Exception as e:
                    print(repr(e))
                if firstflag_vote == '':
                    firstflag_vote = current_period
                    firstflag_jinbi = current_jinbi
                    config = configparser.ConfigParser()
                    config.read("Config_jxyfk28.ini")
                    config_title = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    try:
                        config.add_section(config_title)
                        config.set(config_title, "starttime：", config_title)
                        config.set(config_title, "firstvote：", firstflag_vote)
                        config.set(config_title, "firstjinbi", firstflag_jinbi)
                        config.write(open("Config_jxyfk28.ini", "w"))
                        tempa = config.sections()
                        newa = []
                        findtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                        # print(findtime)
                        for x in tempa:
                            # print(x.find(findtime))
                            if x.find(findtime) >= 0:
                                newa.append(x)
                        todayfirstjinbi = int(config.get(newa[0], 'firstjinbi'))
                    except configparser.DuplicateSectionError:
                        print("Section already exists")
                # 循环采集部分
                mydb = p_mysql.MySQL()
                # 查询数据库最后一期，然后显示出来
                sql_text = "select period from jx_fk28 ORDER BY period DESC limit 1"
                sql_re = mydb.query(sql_text)
                if len(sql_re) <= 0:
                    endf = 44
                else:
                    endf = int((int(current_period) - int(sql_re[0][0])) / 25) + 1
                    if endf >= 44:
                        endf = 44
                self.up_dt_info.emit("需采集" + str(endf) + "页数")
                w = 1
                while w <= endf:
                    self.up_dt_info.emit("开始采集，第" + str(w) + "页---")
                    try:
                        base_time = int(time.time()) * 1000
                        x_sign = baseN(base_time, 36)
                        # 为header字典添加一个X-sign标识，毫秒级时间戳36进制
                        post_head['X-Sign'] = x_sign
                        # 服务器接受str格式，把字典格式json格式转化
                        a = json.dumps(
                            {"c": "quiz", "fun": "getEachList", "items": "crazy28", "pageSize": 23, "pageIndex": w})
                        b = json.dumps({"items": "crazy28"})
                        # 毫秒级时间戳，同时作为postdatspeed16a数据发现服务器
                        pst_data = {'jxy_parameter': a, 'timestamp': base_time, 'params': b,
                                    'xtpl': 'fun/private/jc-index-tbl'}
                        url = 'http://www.juxiangyou.com/fun/play/interaction'
                        # Post数据服务器，cookies使用登录页面与验证码 合并cookies提交
                        req_one = requests.post(url, data=pst_data, cookies=gol_cookies, headers=post_head,
                                                allow_redirects=False)
                        vote_data = json.loads(req_one.text)
                        if vote_data['code'] == 10000:
                            for x in vote_data['itemList']:
                                period = x['num']
                                vote_time = x['date']
                                jcjg = x['jcjg2']
                                state = x['state']
                                if state == 1:
                                    sql = "insert into jx_fk28 values ('" + period + "','" + vote_time + "','" + str(
                                        jcjg) + "')"
                                    mydb.query(sql)
                        w = w + 1
                    except Exception as e:
                        self.up_dt_info.emit("采集过程中，页面信息问题，重新采集该页")
                        print("错误:%s" % traceback.format_exc())
                        w = w - 1
                        if w <= 0:
                            w = 1
                self.up_dt_info.emit("采集完成")
                self.up_table_info.emit(req.text)
                # if moni == 1 and first_run == 0:
                #     wrong = firstwrong
                #     print('当我更新wrong时，我的值还是',firstwrong)
                if first_run == 0:
                    self.up_dt_info.emit('先搜索最近的一次错6')
                    remax = self.remaxwrong()
                    if int(current_period) - int(remax) <= 30:
                        moni = 0
                    first_run = 1
                    self.up_statusinfo.emit(
                        '第一次查询错六为: ' + str(remax) + " ,间隔期 : " + str(int(current_period) - int(remax)))
                    self.up_dt_info.emit('搜索结束')

                # 每一次，必须采集完成后，才开始从数据库中拿数据判断
                if vote_list:  # 如果不为空，说明上一次投注了，判断是否正确。
                    try:
                        vote_period = str(vote_list[-1]).strip()
                        sql = "select * from jx_fk28 where period='" + vote_period + "' limit 1"
                        redata = mydb.query(sql)
                        last_vote = redata[0][2]
                        # print('返回列表', vote_list, '查找返回投注期的结果', last_vote[0])
                        self.up_dt_info.emit('上期投注列表' + str(vote_list))
                        if int(last_vote) in vote_list:
                            print('投注正确,倍率清空')
                            self.up_lastinfo.emit((vote_period, '', '', last_vote, '正确', ''))
                            wrong = 0
                            if wrongflag == True and moni == 1:
                                wrongflag = False
                                toufayu = True
                                jishu = 0
                                moni = 0
                        else:
                            self.up_lastinfo.emit((vote_period, '', '', last_vote, '错误', ''))
                            if int(last_vote) > 0:
                                # print('投注错误,次数加 1 ,错误次数：', wrong)
                                wrong = wrong + 1
                                if wrong >= maxwrong:
                                    wrongflag = True
                                    moni = 1
                    except Exception as e:
                        self.up_dt_info.emit("查询已投注的结果错误:%s" % traceback.format_exc())
                        # ---------------------------------------------------
                s1 = int(current_period) - 1
                s2 = str(int(current_period) - 2)
                s3 = str(int(current_period) - 3)
                s4 = str(int(current_period) - 4)
                # sql = "select * from jx_fk28 where period='" + s1 + "' or period='" + s2 + "' or period='" + s3 + "' or period='" + s4 + "' order by period DESC"
                sql = "select * from jx_fk28 where period <= %s order by period DESC LIMIT 20" % (s1)
                # print(sql)
                redata_1 = mydb.query(sql)
                # print(redata_1)
                last_1 = redata_1[0][2]
                last_2 = redata_1[1][2]
                last_3 = redata_1[2][2]
                last_4 = redata_1[3][2]
                print(last_1, last_2, last_3, last_4)
                for x in redata_1:
                    czlst.append(int(x[2]))
                print(czlst)
                if vote_retime > 9:
                    if moni == 0:
                        if jishu >= 6 and wrong == 0:
                            toufayu = False
                        if toufayu == True:
                            yinshu = 20
                        jishu = jishu + 1
                        if jishu >= 250 and wrong <= 2:
                            moni = 1
                            jishu = 0
                    # print('lezhuan,最大错:', maxwrong, '当前错误', wrong, "金币：", '倍数', yinshu, '模拟', moni, '投注次数', jishu,
                    #       '错标', wrongflag, '偷发育', toufayu)
                    # list_v = daxiao_1(last_1, last_2, last_3, last_4, multiple[wrong], yinshu)
                    list_v = daxiao_2(last_1, last_2, last_3, last_4, multiple[wrong], yinshu, czlst)
                if list_v:
                    vote_list = vote_thing(current_period, list_v)
                    if int(vote_list[0]) < 10:
                        dd = '小'
                    else:
                        dd = '大'
                    self.up_curinfo.emit((current_period, multiple[wrong] * yinshu * 500, jishu, wrong,
                                          int(current_jinbi) - todayfirstjinbi, moni, dd))
                else:
                    vote_list = []
                    self.up_curinfo.emit((current_period, '', '', '', '', moni, ''))
                del mydb
                dealy_time = vote_retime + 28
                self.up_dt_info.emit('延时%s刷新' % dealy_time)
                for m in range(dealy_time, -1, -1):
                    self.up_lcd_num.emit(m)
                    time.sleep(1)
            else:
                self.up_dt_info.emit("当前期都没找到，继续延时30秒查找")
                time.sleep(5)
        except Exception as e:
            print('traceback.format_exc():%s' % traceback.format_exc())
            self.up_dt_info.emit("访问网站出错，等待10秒，重新访问" + repr(e))
            time.sleep(5)
