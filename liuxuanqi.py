'''我的主页'''
import streamlit as st
from PIL import Image

zyjs = ':blue[主页介绍]'
wdxqtj = ':red[我的兴趣推荐]:coffee:'
wdtpclgj = ':orange[我的图片处理工具]'
wdzncd = ':blue[我的智能词典]'
wdxxxdjl = ':blue[我的学习心得交流]:sparkling_heart:'
zsdt = ':orange[知识答题]:100:'
bxdtz = ':red[憋笑大挑战]:smile:'
xxgk = ':red[感谢欣赏]:kissing_heart:'
wdlyq = ':orange[我的留言区]:balloon:'

page = st.sidebar.radio('我的首页', [zyjs, wdxqtj, wdtpclgj, wdzncd, wdxxxdjl, 
                                    zsdt, bxdtz, xxgk, wdlyq])

wzjs = ':blue[网站介绍]'
qy = ':red[前言]'
jj = '''


        大家好！欢迎来到乐趣社！我是制作人六无双（匿名），请多多支持，多多指教。
        \n本网站分为七大区：
        \n我的兴趣推荐、我的图片处理工具、我的智能词典、我的学习心得交流、我的留言区、憋笑大挑战、知识答题。
        \n下面请你们点击其他表格，让我们一起去了解其他区的故事吧！:smile:
        '''
bxwp_1 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

wdxqtj_tm= ':red[我的兴趣推荐]'
wdxqtj_story = '''


                    你们好！我的名字叫兴趣推荐！我在这里排行老大，因为我会的最多。
                    \n我会的不仅有音乐、游戏、电影还有书籍和习题集等。
                    \n所以在这里我称第一，没人敢称第二，哈哈哈哈哈。
                    \n还有谁！！！！！
                    '''
bxwp_2 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

wdtpclgj_tm = ':orange[我的图片处理工具]'
wdtpclgj_story = '''


                        大家好！我的名字叫图片处理工具！我在这里排行第五。
                        \n如你们所见，我会处理图片，把图片改成其他的颜色。
                        \n很高兴见到你们，以后请多多指教！
                        '''
bxwp_3 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

wdzncd_tm = ':blue[我的智能词典]'
wdzncd_story = '''


                    大家好！我的名字叫智能词典，我在这里排行第三。
                    \n我的英语特别好，大家有什么不会的单词都可以问我哦。
                    \n希望能和大家和谐相处，共同进步！
                    '''
bxwp_4 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

wdxxxdjl_tm = ':blue[我的学习心得交流]'
wdxxxdjl_story = '''


                        你们好！我的名字叫学习心得，我在这里排行第四。
                        \n我的成绩可好了，而且我有很多的学习方法可以分享给大家。
                        \n希望大家也能学习进步！
                        '''
bxwp_5 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

wdlyq_tm = ':orange[我的留言区]'
wdlyq_story = '''


                    大家好！我的名字叫留言，我在这里排行第六。
                    \n我擅长记录别人说的评价，而且记忆力超群。
                    \n我希望可以和大家和谐相处！
                    '''
bxwp_6 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

bxdtz_tm = ':red[憋笑大挑战]:smile:'
bxdtz_story = '''


                    大家好！全体目光看向我，我叫憋笑大挑战！我在这里可是排行第二哦！
                    \n我会讲很多笑话，时常惹得大家发笑。
                    \n我希望可以用这些笑话让大家都开心起来。
                    \n所以在此我也祝大家能开心快乐每一天！
                    '''

bxwp_7 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

zsdt_tm = ':orange[知识答题]'
zsdt_story = '''


                    大家好！我的名字叫知识答题，在这里我排行第七！
                    \n我有一个爱好是考别人问题，而且还会给出评价。
                    \n希望你们能通过我的考验！
                    '''

bxwp_23 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

def page_1():
    '''主页介绍'''
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(["网站介绍", "我的兴趣推荐", "我的图片处理工具", 
                                                  "我的智能词典", "我的学习心得交流", "我的留言区",
                                                  "憋笑大挑战", "知识答题"])
    with tab1:
        st.title(wzjs)
        st.header(qy)
        st.subheader(jj)
        st.caption(bxwp_1)
        st.snow()
    with tab2:
        st.title(wdxqtj_tm)
        st.subheader(wdxqtj_story)
        st.caption(bxwp_2)
        st.balloons()
    with tab3:
        st.title(wdtpclgj_tm)
        st.subheader(wdtpclgj_story)
        st.caption(bxwp_3)
        st.snow()
    with tab4:
        st.title(wdzncd_tm)
        st.subheader(wdzncd_story)
        st.caption(bxwp_4)
        st.balloons()
    with tab5:
        st.title(wdxxxdjl_tm)
        st.subheader(wdxxxdjl_story)
        st.caption(bxwp_5)
        st.snow()
    with tab6:
        st.title(wdlyq_tm)
        st.subheader(wdlyq_story)
        st.caption(bxwp_6)
        st.balloons()
    with tab7:
        st.title(bxdtz_tm)
        st.subheader(bxdtz_story)
        st.caption(bxwp_7)
        st.snow()
    with tab8:
        st.title(zsdt_tm)
        st.subheader(zsdt_story)
        st.caption(bxwp_23)
        st.balloons()

# 电影推荐
mag_movie = ':blue[电影推荐]'
movie_1 = ':red[《哈利波特》]'
zynr_1 = ':orange[主要内容]'
movie_hl = '''


                《哈利·波特》系列电影，是由美国华纳兄弟娱乐公司将JK罗琳所著的同名系列小说改拍成的八部电影，由
            丹尼尔·雷德克里夫、鲁伯特·格林特、艾玛·沃特森等主演的剧情片 。
                \n讲述的是年轻的巫师学生哈利·波特在霍格沃茨魔法学校前后六年的学习生活和冒险故事;第七部讲述的
            是哈利·波特在第二次巫界大战中被迫逃亡在外寻找魂器并消灭伏地魔的故事。
            '''
movie_2 = ':red[《长安三万里》]'
zynr_2 = ':orange[主要内容]'
movie_caswl = '''


                《长安三万里》以盛唐为背景，讲述安史之乱后，整个长安因战争而陷入混乱，身处局势之中的高适回忆
            起自己与李白的过往。剧情简介安史之乱后数年，吐蕃大军入侵西南，大唐节度使高适交战不利。长安岌岌可
            危。困守孤城的高适向监军太监回忆起自己与李白的一生往事。
                《长安三万里》塑造了大唐诗人的群像，在李白、高适、杜甫之外，还有贺知章、王维、王昌龄、郭子仪、
            岑参、张旭、哥舒翰......诗人们的集体登场，宛如历史天空中的群星闪耀在观众眼前。
            '''
bxwp_8 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 游戏推荐
mag_game = ':blue[游戏推荐]'
game_1 = ':red[我的世界]'
game_2 = ':red[王者荣耀]'
jdtc = ':orange[经典台词]'
game_wzry = '''


                一个人可以被毁灭，但绝不会被打败 ——————凯
                \n人生就是不停地比拼，你赢了别人就输了，别人赢了你就输了。——————狄仁杰
                \n决定了内心的正道，便毫无动摇。——————关羽
                \n天地与我并生,万物与我为宜。——————庄周
                \n雄鹰不及暴风者也，狼群不应长夜畏惧。——————成吉思汗
                '''
game_3 = ':red[和平精英]'
bxwp_9 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 书籍推荐
mag_book = ':blue[书籍推荐]'
book_1 = ':red[《钢铁是怎样炼成的》]'
zynr_3 = ':orange[主要内容]'
book_gtszylcd = '''


                    《钢铁是怎样炼成的》是苏联作家尼古拉·奥斯特洛夫斯基于1934年创作的一部现实主义小说，被誉
                为是社会主义文学的代表作之一。该小说主要讲述了主人公保尔·柯察金的成长历程，以及他如何在革命的
                熔炉中，逐步锻炼成为一位坚强的无产阶级战士。
                    \n小说的主旨是探讨人类社会发展与科技进步之间的关系。作者通过描写柯察金的成长经历，表现了革
                命斗争的艰辛与意义，强调了人的精神力量和意志力的伟大。同时，小说中也详细阐述了科技在社会发展中
                的重要作用，并对科技的发展进行了深入的思考和分析。
                '''
book_2 = ':red[《明朝那些事儿》]'
zynr_4 = ':orange[主要内容]'
book_mcnxs = '''


                历史小说《明朝那些事儿》主要讲述的是从1344年到1644年这三百年间关于明朝的一些故事。以史料为基
            础，以年代和具体人物为主线，并加入了小说的笔法，语言幽默风趣。对明朝十七帝和其他王公权贵和小人物的
            命运进行全景展示，尤其对官场政治、战争、帝王心术着墨最多，并加入对当时政治经济制度、人伦道德的演
            义。
            '''
book_3 = ':red[《上下五千年》]'
zynr_5 = ':orange[主要内容]'
book_sxwqn = '''


                主要内容:以时间为经，以事件和人物为纬，穿针引线，纵横交纵，从盘古开天辟地的传说开始，将中华
            上下五千年历史文化的精髓，展现，为读者提供了了解历史的捷径。清晰地勾勒出历史事件的来龙去脉和历史
            人物的真伪辩恶。
            '''
bxwp_10 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 习题集推荐
mag_exersice = ':blue[习题集推荐]'
exersice = ':red[《三年中考五年模拟》]'
bxwp_11 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 音乐推荐
mag_music = ':blue[音乐推荐]'
bxwp_12 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
xz_1 = ':green[喜欢可以下载哦!]:sunglasses:'

# 图片推荐
mag_picture = ':blue[图片推荐]'
bxwp_13 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
xz_2 = ':green[喜欢可以下载哦!]:sunglasses:'

def page_2():
    '''我的兴趣推荐'''
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["电影推荐", "游戏推荐", "书籍推荐",
                                                  "习题集推荐", "音乐推荐", "图片推荐"])
    with tab1:
        st.title(mag_movie)
        st.header(movie_1)
        st.subheader(zynr_1)
        st.write(movie_hl)
        st.image('hl.jpg')
        st.image('fdm.jpg')
        st.header(movie_2)
        st.subheader(zynr_2)
        st.write(movie_caswl)
        st.image('caswlone.jpg')
        st.image('caswltwo.jpg')
        st.caption(bxwp_8)
        st.snow()
    with tab2:
        st.title(mag_game)
        st.header(game_1)
        st.image('wdsj.jpg')
        st.header(game_2)
        st.write(jdtc)
        st.write(game_wzry)
        st.header(game_3)
        st.image('hpjyone.jpg')
        st.image('hpjytwo.jpg')
        st.caption(bxwp_9)
        st.balloons()
    with tab3:
        st.title(mag_book)
        st.header(book_1)
        st.subheader(zynr_3)
        st.write(book_gtszylcd)
        st.header(book_2)
        st.subheader(zynr_4)
        st.write(book_mcnxs)
        st.image('mcnxs.jpg')
        st.header(book_3)
        st.subheader(zynr_5)
        st.write(book_sxwqn)
        st.caption(bxwp_10)
        st.snow()
    with tab4:
        st.title(mag_exersice)
        st.header(exersice)
        st.image('wnzlsnmn.jpg')
        st.caption(bxwp_11)
        st.balloons()
    with tab5:
        st.title(mag_music)
        with open('编程猫的梦想.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
            st.download_button(label="下载音频", data = mymp3, file_name="编程猫的梦想.mp3")
        with open('Beijing_Bass.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
            st.download_button(label="下载音频", data = mymp3, file_name="Beijing_Bass.mp3")
        with open('Last_Stop.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
            st.download_button(label="下载音频", data = mymp3, file_name="Last_Stop.mp3")
            st.write(xz_1)
        st.caption(bxwp_12)
        st.snow()
    with tab6:
        st.title(mag_picture)
        st.image('dog.jpg')
        with open("dog.jpg", "rb") as f:
            a = f.read()
        st.download_button(label="下载图片", data = a, file_name="dog.jpg")
        st.image('dragon.jpg')
        with open("dog.jpg", "rb") as f:
            a = f.read()
        st.download_button(label="下载图片", data = a, file_name="dragon.jpg")
        st.image('hx.jpg')
        with open("dog.jpg", "rb") as f:
            a = f.read()
        st.download_button(label="下载图片", data = a, file_name="hx.jpg")
        st.image('kr.jpg')
        with open("dog.jpg", "rb") as f:
            a = f.read()
        st.download_button(label="下载图片", data = a, file_name="kr.jpg")
        st.image('xk.jpg')
        with open("dog.jpg", "rb") as f:
            a = f.read()
        st.download_button(label="下载图片", data = a, file_name="xk.jpg")
        st.write(xz_2)
        st.caption(bxwp_13)
        st.balloons()

tpclgj = ':blue[图片处理小程序]:sunglasses:'
        
def page_3():
    '''我的图片处理工具'''
    st.snow()
    st.subheader(tpclgj)
    uploaded_file = st.file_uploader("图片分享", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1,tab2,tab3,tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
            st.snow()
        with tab2:
            st.image(img_change(img, 0, 2, 1))
            st.balloons()
        with tab3:
            st.image(img_change(img, 1, 2, 0))
            st.snow()
        with tab4:
            st.image(img_change(img, 1, 0, 2))
            st.balloons()

zncd = ':blue[智能词典]'
        
def page_4():
    '''我的智能词典'''
    st.subheader(zncd)
    # 从本地文件中词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容在进行分割， 分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典， 方便查询，格式为“编号、单词、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询词书读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 经列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    st.balloons()
    
def page_5():
    '''我的学习心得交流'''
    # 素材
    sc_1 = '''    
    
                古书有云:“学如逆水行舟，不进则退。”我也深有体会，它自然成为我的个人格言。学习如天上
            的云，一不小心就会然自己的知识被大地吸干，努力的成绩可都被别人来去了，自己却成为一无所有。
                \n“书中自有黄金屋，书中自有彦如玉。”在我的生活中，书是我的好朋友，床边、书桌、椅子，都
            有它的存在。在有空的时候看一看书，然紧张的大脑放松一下。在书的海洋遨游，然你受益匪浅。我
            平时爱在中午看一些散文，晚上看含有深刻道理的，体会、分析、感受、领悟其深刻的道理。
                \n“人的天才只是火花，要想使它成熊熊火焰，那就只有学习!学习。”它是我的助跑线，它让我知道:
            只有学习才能让人的天才成熊熊火焰，就算人没有天才，但有了学习就是有成功之路。
                \n讲到学习方法，我想用六个字来概括:“严格、严肃、严密。”这种科学的学习方法，除了向别人学
            习之外，更重要的是靠自己有意识的刻苦锻炼。如果你只会向别人学习，自己却不意识的刻苦锻炼，就
            如一颗没发芽的种子，只想快快长大，自己不主动在生活中锻炼，只会长得矮小。
                \n“复习是学习之母。”复习也是我的学习生活中最重要的一部分，也是我的学习方法之一。“学习后
            复习，让知识更巩固。”是我课后的名言，也是我的课后行动，因常言道“温故知新”。
                \n让我们赶快行动起来，找到自己的学习方法，感受学习的快乐，体验学习的幸福，领悟学习的道
            理吧!'''
    bxwp_14 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'

    sc_2 = '''

    
                对于学习，我们应该去适应它，而不是让它来适应我们。那我们应该怎样去适应学习呢?我觉得我们应
            该做到以下三点:
            \n
            一、学得平衡
                \n学习，首先要做到的就是平衡。不能说你喜欢这一学科，就一味地学习这一学科，而放弃其它学科。
            但也不能因为你这一学科较弱而总学习这一学科，自己较强的学科却不去学习。这些都是不平衡的现象，到
            最后只会是两手空空。我们应该做到科科必学，科科平衡。当然，如果自己的弱势学科实在是补不上，可以
            采取“扬长避短”的学习方法，让自己的优收起势字科学得更好，以弥补自己的不足。
            \n
            二、学得透彻 
                \n学习，就是要有敢问敢钻研的精神。我是一个提倡“不懂就问”的学习方法的人。要想学得透彻，不光
            上课要认真听，课后还要找出不懂的地方问老师，与同学探讨，力求把每一个不懂的地方都弄懂，每一个知
            识点都学懂。不能将不懂的知识都藏起来，要记住把不懂的知识变成为自己的知识，是一件有利于自己的事。
            \n
            三、学得有趣 
                \n当你把所有的知识都学懂之后，你会发现，原来那一道道如拦路虎般的练习题都变成了笑脸在向你招
            手。学得有趣就是要在学得透彻的基础上更进一步。把做练习题变得像做游戏一样有趣，那你的学习之旅就
            会变得既轻松又愉快了。
                \n学习是一件困难而又轻松的事，只要你掌握一定的学习方法与态度，就能化难为易，轻松学习。
            '''
    bxwp_15 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'
    
    sc_3 = '''
    
    
                成功没有捷径，只有靠自己的努力和付出才能取得胜利。在学习的路程上，有着许多困难和挫折，有人没
            有勇气度过，从而浑浑噩噩度过一生，有人则披荆斩棘，尝到了胜利的果实。
                \n爱因斯坦说过:“我认为，对一切来说，只有热爱才是最好的教师，它远远超过责任感。”只有对学习产
            生兴趣，才能更认真的学习。比如某些同学，根据自己的喜好来学习，弱科放在一旁不管，结果偏科很严重。
            要想办法对自己薄弱的科目产生兴趣，并学习它。老师经常对我们说“科要多练，文科要多读”。我们应该多读
            写，“知之为知之，不知为不知，是知也”，遇到不会的题目，千万不要不懂装懂。
                \n“预则立，不预则废”每次课前都要先预习下，下节课学习的内容，不但能使我们的自主学习能力有很大
            的提高，还能排除对老师的依赖。如果不课前预习，就会比别人慢一拍，造成课堂学习上“手忙脚乱”的窘相。
                \n“温故而知新”当老师讲完课之后，我们应该做到即时复习，巩固学过的知识，记忆得更牢固。我们也可
            以试试为自己制定一个学习计划，但不要天马行空，纸上谈兵，否则到头来还是竹篮打水一-一场空。
                \n学习方法因人而异，各不相同，愿同学们找到适合自己的学习方法，在学习生涯中绘上精彩的一笔!
            '''
    bxwp_16 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'

    tab1,tab2,tab3 = st.tabs(["学习心得1", "学习心得2", "学习心得3"])
    with tab1:
        st.write(sc_1)
        st.caption(bxwp_14)
        st.snow()
    with tab2:
        st.write(sc_2)
        st.caption(bxwp_15)
        st.balloons()
    with tab3:
        st.write(sc_3)
        st.caption(bxwp_16)
        st.snow()
    
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

# 答题介绍
dtjs = ':blue[答题介绍]'
dtjs_1 = '''


            大家好！欢迎来到知识答题！
            \n本版块分为语文答题、数学答题和英语答题。
            \n希望大家都能取得好成绩！
            \n加油！挑战者！:rocket:
            '''

# 评级
pj = ':orange[评级]'
pj_1 = '''


            答对三道及以下的答题者：没文化，真可怕！:joy:
            \n答对四道到六道的答题者：合格喽！:smile:
            \n答对七道到九道的答题者：很不错！:satisfied:
            \n全部答对者：人才啊！:heart_eyes:
            '''

bxwp_18 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
bxwp_19 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
bxwp_20 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
bxwp_21 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'
bxwp_22 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

def page_6():
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["介绍", "语文答题", "数学答题", "英语答题", "热梗答题"])
    with tab1:
        st.title(zsdt)
        st.header(dtjs)
        st.write(dtjs_1)
        st.subheader(pj)
        st.write(pj_1)
        st.caption(bxwp_18)
        st.balloons()
    with tab2:
        i = 0
        st.write("单选题")
        choice = st.radio(
        '1、下列词语中加点字的注音完全正确的一项是()',
        ['A. 亘古(gèn) 枯槁(gǎo) 坍塌(tān) 忍俊不禁(jīn)', 
         'B. 惬意(xiá) 倔强(jué) 痴想(chi)潜龙勿用(qián)', 
         'C. 狩猎(shǒu) 归省(xǐng)逞能(chěng) 略胜一筹(chóu)', 
         'D. 滑稽(jī) 静谧(mi) 蓦然(mò) 惊慌无措(chù)'])
        if choice == 'A. 亘古(gèn) 枯槁(gǎo) 坍塌(tān) 忍俊不禁(jīn)':
            i += 1

        choice = st.radio(
        '2、下列句子中没有语病的一项是()',
        ['A. 经过表决、推举和讨论等程序，学生会的人选顺利产生。', 
         'B. 凭借着“山重水复疑无路，柳暗花明又一村”的坚强意志，他终于跨越了眼前这道人生沟坎。', 
         'C. 一个人是否拥有健康的体魄，关键在于持之以恒地参加体育锻炼。', 
         'D. “七河八岛”被誉为扬州的“翡翠项链”，它与古运河扬州段是构成扬城“血脉”的重要组成部分。'])
        if choice == 'D. “七河八岛”被誉为扬州的“翡翠项链”，它与古运河扬州段是构成扬城“血脉”的重要组成部分。':
            i += 1

        choice = st.radio(
        '3、下列各句中，加点词语使用不恰当的一项是()',
        ['A. 对这个一窍不通的少年，母亲只能为他四处请教学习方法。', 
         'B. 一本书的梗概或简介，通常包括作者情况、书名由来、内容梗概和作品评价等方面内容。', 
         'C.《忆读书》一文中，冰心奶奶不仅将读《三国演义》时的真实感受写得酣畅淋漓，义薄云天。', 
         'D.《济南的冬天》和《小石潭记》这两篇散文，表现手法的差异可谓泾渭分明。'])
        if choice == 'C.《忆读书》一文中，冰心奶奶不仅将读《三国演义》时的真实感受写得酣畅淋漓，义薄云天。':
            i += 1

        choice = st.radio(
        '''4、下列句子组成语段顺序排列正确的一项是()
            ①人工智能的发展必将引发新的科技革命，产生重大而深远的影响。
            ②当今世界，信息技术创新日新月异。
            ③随着各种人工智能技术的涌现和应用，人们对未来充满期待和憧憬。
            ④新一代人工智能技术正在引领新一轮科技革命和产业变革方向的发展。
            ⑤尤其是人工智能技术，已经成为国际竞争的新焦点和经济发展的新引擎。''',
        ['A. ②⑤①④③', 'B. ②①④⑤③', 'C. ④①②⑤③', 'D. ②④①⑤③'])
        if choice == 'D. ②④①⑤③':
            i += 1

        choice = st.radio(
        '5、下列各句中加点的词语古今意义相同的一项是()',
        ['A. 是鸟也，海运则将徙于南冥', 'B. 若夫乘天地之正，而御六气之辩', 
         'C. 三餐而反，腹犹果然', 'D. 虽然，犹有未树也'])
        if choice == 'D. 虽然，犹有未树也':
            i += 1

        choice = st.radio(
        '6、下列句子没有语病的一项是()',
        ['A. 我们通过阅读提升阅读鉴赏能力，掌握运用语言文字的规律，进而涵养好品德。', 
         'B. “三独”比赛的举办权不仅赋予了南宁市还赋予了桂林市，我市将于今年11月如期举行比赛。', 
         'C.《中华人民共和国民法典(草案)》明确住宅建设用地使用权70年到期自动续期。民法典这一规定消除了大家的后顾之忧。', 
         'D. 通过垃圾分类处理，能节约资源、减少环境污染，已经引起了各级政府的高度重视。'])
        if choice == 'C.《中华人民共和国民法典(草案)》明确住宅建设用地使用权70年到期自动续期。民法典这一规定消除了大家的后顾之忧。':
            i += 1
            
        choice = st.radio(
        '7、下列句子中没有通假字的一项是()',
        ['A. 不亦说乎', 'B. 由，诲女知之乎', 'C. 学而不思则罔', 'D. 是故学然后知不足'])
        if choice == 'D. 是故学然后知不足':
            i += 1

        choice = st.radio(
        '8、下列句子中加点词的解释错误的一项是()',
        ['A. 微斯人，吾谁与归(如果没有)', 'B. 盖简桃核修狭者为之(挑选)', 
         'C. 无案牍之劳形(使.....劳累)', 'D. 同舍生皆被绮绣(通“披”，穿)'])
        if choice == 'A. 微斯人，吾谁与归(如果没有)':
            i += 1
            
        st.write("多选题")
        st.write('9、下列文学常识中，哪些是正确的？')
        col1, col2, col5= st.columns([2, 2, 1])
        with col1:
            cb1 = st.checkbox('A. 李白，字太白，号青莲居士，被人誉为‘诗仙’。')
        with col2:
            cb2 = st.checkbox('B. 鲁迅，原名周树人，浙江绍兴人，代表作有散文集《野草》，短篇小说《彷徨》等。')
        col3, col4, col6= st.columns([2, 2, 1])
        with col3:
            cb3 = st.checkbox('C. 萧红，原名张迺莹，黑龙江呼兰人，代表小说有《呼兰河传》《生死场》等。')
        with col4:
            cb4 = st.checkbox('D. 冰心，原名谢婉莹，中国现代诗人、作家、思想家。')
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            i += 1

        st.write('10、下列对课文内容理解正确的一项是 ')
        col1, col2, col5= st.columns([2, 2, 1])
        with col1:
            cb1 = st.checkbox('A.《春》一文的作者用诗的笔调，描绘了大地回春、万物复苏、生机勃勃的景象,抒发了作者热爱春天、赞美春天、珍惜春天的美好感情。')
        with col2:
            cb2 = st.checkbox('B.《济南的冬天》描绘了如下几幅图画:阳光下济南全景，冬日山景，清亮的水色。')
        col3, col4, col6= st.columns([2, 2, 1])
        with col3:
            cb3 = st.checkbox('C.《雨的四季》是一篇托物言志的散文，对雨的描写生动形象，语言古朴典雅。')
        with col4:
            cb4 = st.checkbox('D.《次北固山下》作者借潮平岸阔之景抒发了思乡之情。')
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            i += 1

        tj_1 = st.button('提交答题1')
        if tj_1:
            if i <= 3:
                st.write("没文化，真可怕！")
            elif i >= 4 and i <= 6:
                st.write("合格喽！")
            elif i >= 7 and i <= 9:
                st.write("很不错哦！")
            else:
                st.write("天才啊！")
        st.caption(bxwp_19)
        st.snow()
    with tab3:
        i = 0
        st.write("单选题")
        choice = st.radio(
        '1、下列说法正确的是()',
        ['A. 射线AB与射线BA是同一条射线。', 'B. 两条射线组成的图形叫做角。', 
         'C. 各边都相等的多边形是正多边形。', 'D. 连接两点的线段的长度叫做两点间的距离。'])
        if choice == 'D. 连接两点的线段的长度叫做两点间的距离。':
            i += 1

        choice = st.radio(
        '2、在数轴上与原点的距离小于8的点对应的数为x，则x的取值范围是()',
        ['A. x>0', 'B. x<0', 'C. x<8' 'D. 0<x<8'])
        if choice == 'C. x<8':
            i += 1

        choice = st.radio(
        '3、当x、y满足关系___时，|x-y|表示x与y差的绝对值',
        ['A. x-y≤0', 'B. y-x≤0', 'C. x-y≥0', 'D. x-y≤0'])
        if choice == 'C. x-y≥0':
            i += 1

        choice = st.radio(
        '4、已知二次二项式（n -1）a ⁴ +aⁿ +a²，那么n的值为()',
        ['A. 3', 'B. 4', 'C. 2', 'D. 5'])
        if choice == 'C. 2':
            i += 1

        choice = st.radio(
        '5、在平面直角坐标系中，点A的坐标为(-1,2)，将线段OA绕点0逆时针旋转90°得到OA，则点A的坐标是()',
        ['A. (2,-1)', 'B. (-1,-2)', 'C. (-2,1)', 'D. (1,-2)'])
        if choice == 'D. (1,-2)':
            i += 1

        choice = st.radio(
        '6、下列说法中正确的是()',
        ['A. -5不是负数', 'B. 有理数中包括正数和负数', 'C. 0不是自然数', 'D. 正整数包括零和自然数'])
        if choice == 'A. -5不是负数':
            i += 1

        choice = st.radio(
        '7、已知∠a=36°42/，则∠a的补角为___',
        ['A. 53°18', 'B. 233°18', 'C. 126°42', 'D. 143°18'])
        if choice == 'D. 143°18':
            i += 1

        choice = st.radio(
        '8、下列说法中正确的是()',
        ['A. 射线AB与射线BA是同一条射线。', 'B. 有且只有一条直线垂直于已知直线。', 
         'C. 从同一点引出的两条射线组成的图形叫做角。', 'D. 有公共端点的两条线段组成的图形叫做角。'])
        if choice == 'C. 从同一点引出的两条射线组成的图形叫做角。':
            i += 1

        st.write("多选题")
        st.write('9、下列说法中，正确的是')
        col1, col2, col5= st.columns([2, 2, 1])
        with col1:
            cb1 = st.checkbox('A. 射线AB和射线BA是同一条射线。')
        with col2:
            cb2 = st.checkbox('B. 延长射线MN到C。')
        col3, col4, col6= st.columns([2, 2, 1])
        with col3:
            cb3 = st.checkbox('C. 延长线段MN到A，使NA=2MN。')
        with col4:
            cb4 = st.checkbox('D. 连接两点的线段的长度叫做两点间的距离。')
        if cb1 == False and cb2 == False and cb3 == True and cb4 == True:
            i += 1

        st.write('10、当整数m为何值时,关于x的方程1/2mx - 5/3 = 1/2(x - 4/3)的解是正整数?')
        col1, col2, col5= st.columns([2, 2, 1])
        with col1:
            cb1 = st.checkbox('A. 7')
        with col2:
            cb2 = st.checkbox('B. 3')
        col3, col4, col6= st.columns([2, 2, 1])
        with col3:
            cb3 = st.checkbox('C. 4')
        with col4:
            cb4 = st.checkbox('D. 2')
        if cb1 == False and cb2 == True and cb3 == False and cb4 == True:
            i += 1

        tj_2 = st.button('提交答题2')
        if tj_2:
            if i <= 3:
                st.write("没文化，真可怕！")
            elif i >= 4 and i <= 6:
                st.write("合格喽！")
            elif i >= 7 and i <= 9:
                st.write("很不错哦！")
            else:
                st.write("天才啊！")
        st.caption(bxwp_20)
        st.balloons()
    with tab4:
        i = 0
        st.write("单选题")
        choice = st.radio(
        '1、-What is this? \n-lt is ______ orange.',
        ['A. a', 'B. an', 'C. the', 'D. /'])
        if choice == 'B. an':
            i += 1

        choice = st.radio(
        '2、-______ is your favorite subject? \n-It is math.',
        ['A. What', 'B. Who', 'C. Why', 'D. When'])
        if choice == 'A. What':
            i += 1

        choice = st.radio(
        '3、-I have ______ uncle. -__works in a hos pital.',
        ['A. a; He', 'B. an; His', 'C.the;He', 'D.an; His'])
        if choice == 'B. an; His':
            i += 1

        choice = st.radio(
        '4、-_____is it from your home to school? -About 10 kilometers.',
        ['A. How many', 'B. How far', 'C. How much', 'D. How long'])
        if choice == 'B. How far':
            i += 1

        choice = st.radio(
        '5、-______ do you go to the movies? -Once a month.',
        ['A. How often', 'B. How long', 'C. How far', 'D. How much'])
        if choice == 'A. How often':
            i += 1

        choice = st.radio(
        '6、当别人问你是哪国人时，你应说:',
        ['A. I am China.', 'B. I live in china.', 'C. I live in China.', 'D. T am living China.'])
        if choice == 'C. I live in China':
            i += 1

        choice = st.radio(
        '7、The CD is in my backpack，and my back pack _____ on the floor now.',
        ['A. is', 'B. are', 'C. was', 'D. will be'])
        if choice == 'A. is':
            i += 1

        choice = st.radio(
        '8、-____ do you usually have P.E.? -On Monday and Thursday.',
        ['A. What time', 'B. When', 'C. How many', 'D. What day'])
        if choice == 'B. When':
            i += 1
            
        choice = st.radio(
        '9、My teacher always gets the class ____ a question ___“What is the meaning of life?"',
        ['A. to answer; like', 'B. to answer; as', 'C. /; as', 'D. /; like'])
        if choice == 'D. /; like':
            i += 1

        choice = st.radio(
        '10、-____everyone here today? -Yes, we are all here.',
        ['A. Are', 'B. Is', 'C. Am', 'D. /'])
        if choice == 'B. Is':
            i += 1

        tj_3 = st.button('提交答题3')
        if tj_3:
            if i <= 3:
                st.write("没文化，真可怕！")
            elif i >= 4 and i <= 6:
                st.write("合格喽！")
            elif i >= 7 and i <= 9:
                st.write("很不错哦！")
            else:
                st.write("天才啊！")
        st.caption(bxwp_21)
        st.snow()
    with tab5:
        i = 0
        st.write("单选题")
        choice = st.radio(
        '1、网红奶茶店的"XXX"是何种含义?',
        ['A.对茶的尊重。', 'B.对某个领域的独占和掌控。', 
         'C.对幸福和美满生活的期待。', 'D.一种特殊的茶艺技巧。'])
        if choice == 'B.对某个领域的独占和掌控。':
            i += 1

        choice = st.radio(
        '2、网络流行词"绝绝子"的真正含义是什么?',
        ['A.非常优秀，非常好', 'B.非常差劲，很糟糕', 'C.绝对不可能', 'D.绝对正确'])
        if choice == 'A.非常优秀，非常好':
            i += 1

        choice = st.radio(
        '3、"躺平"这一网络热词的真实含义是什么?',
        ['A.指放弃追求高薪高压力的生活，选择过一种轻松自在的生活态度。', 
         'B.指放弃追求一切目标，完全放弃思考和行动。', 
         'C.指放弃追求高品质生活，选择过一种简朴的生活方式。',
         'D.指放弃追求个人理想，随波逐流。'])
        if choice == 'B.指放弃追求一切目标，完全放弃思考和行动。':
            i += 1

        choice = st.radio(
        '4、"内卷"这一网络热词的真实含义是什么?',
        ['A.指在某个领域内不断努力，不断进步。', 
         'B.指在某个领域内竞争激烈，人们不得不不断加大投入才能保持竞争力。', 
         'C.指在某个领域内出现了倒退和衰退的现象。',
         'D.指在某个领域内缺乏创新和变革。'])
        if choice == 'B.指在某个领域内竞争激烈，人们不得不不断加大投入才能保持竞争力。':
            i += 1

        choice = st.radio(
        '5、请问"梗"是什么意思?',
        ['A.指一个具体的物品。', 'B.指代一个人或事物。', 
         'C.指的是一种网络文化现象。', ' D.指的是一种语言现象。'])
        if choice == 'C.指的是一种网络文化现象。':
            i += 1

        choice = st.radio(
        '6、"网红"一词的含义是什么?',
        ['A.指在社交媒体上具有一定影响力的个人或团体。', 
         'B.指在某个领域内具有特殊技能或专业知识的人。', 
         'C.指在某个地方有一定知名度的个人或团体。', 
         'D.指在某个公司或机构内具有一定职位或地位的人。'])
        if choice == 'A.指在社交媒体上具有一定影响力的个人或团体。':
            i += 1

        choice = st.radio(
        '7、"破防"这一网络热词的真实含义是什么?',
        ['A.指在游戏中击败对手，使其失去防御能力。', 
         'B.指在现实生活中遇到困难或挫折时，内心崩溃，失去抵抗能力。', 
         'C.指在争论或冲突中失败，无言以对。', 
         'D.指突破某种限制或障碍，取得成功。'])
        if choice == 'B.指在现实生活中遇到困难或挫折时，内心崩溃，失去抵抗能力。':
            i += 1

        choice = st.radio(
        '8、“狗头保命"这个梗的来源是什么?',
        ['A.某部电影中的台词。', 'B.某社交平台上的用户创意。', 
         'C.某游戏中的角色设定。', 'D.某广告中的宣传语。'])
        if choice == 'B.某社交平台上的用户创意。':
            i += 1
            
        choice = st.radio(
        '9、"抖音神曲"通常指的是?',
        ['A.在抖音上流行的音乐。', 'B.在抖音上创作的音乐。', 
         'C.在抖音上传播的音乐。', 'D.在抖音上下载的音乐。'])
        if choice == 'A.在抖音上流行的音乐。':
            i += 1

        choice = st.radio(
        '10、"沙雕"在网络语境中是什么意思?',
        ['A.表示某个人的行为很粗鲁。', 'B.表示某个人的性格很古怪。', 
         'C.表示某个人的智商很高。', 'D.表示某个人的思想很独特。'])
        if choice == 'B.表示某个人的性格很古怪。':
            i += 1

        tj_4 = st.button('提交答题4')
        if tj_4:
            if i <= 3:
                st.write("没文化，真可怕！")
            elif i >= 4 and i <= 6:
                st.write("合格喽！")
            elif i >= 7 and i <= 9:
                st.write("很不错哦！")
            else:
                st.write("天才啊！")
        st.caption(bxwp_22)
        st.balloons()
        
# 憋笑大挑战
mag_tz = ':blue[憋笑大挑战]'
bxwp_17 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 规则
js = '''


        大家好！欢迎来到憋笑大挑战！:smile:
        \n下面是三个搞笑视频，分别是初级挑战、中级挑战和高级挑战
        \n规则如下：
        \n1、初级挑战未过：虚:joy:
        \n2、中级挑战未过：合格:smile:
        \n3、高级挑战未过：强:satisfied:
        \n4、高级挑战过了：牛:heart_eyes:
        \n加油！挑战者!:rocket:
        '''

# 评分
cjwg = ':blue[如果初级未过，那么你是一个爱笑的人，加油！]:smile:'
cj = ':green[恭喜你！合格喽！继续加油！]:satisfied:'
zj = ':orange[马上到终点了！再接再厉！]:blush:'
qg = ':red[憋笑之王强无敌！憋笑之王强无敌！]:heart_eyes:'

# 结尾
jw = ':green[恭喜你完成挑战！]:kissing_heart:'

def page_7():
    '''憋笑大挑战'''
    st.title(mag_tz)
    st.write(js)
    st.write(cjwg)
    st.header('初级')
    st.video('gxspa.mp4')
    st.write(cj)
    st.header('中级')
    st.video('gxspb.mp4')
    st.write(zj)
    st.header('高级')
    st.video('gxspc.mp4')
    st.write(qg)
    st.write(jw)
    st.caption(bxwp_17)
    st.balloons()
    st.snow()

def page_8():
    col1, col2, col3= st.columns([1, 1.5, 1])
    with col2:
        st.title(xxgk)
    st.balloons()

lyq = ':blue[我的留言区]'
jjfy = ':red[请大家积极发言哦！]'

def page_9():
    '''我的留言区'''
    st.title(lyq)
    st.subheader(jjfy)
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf=8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌕'):
                st.write(i[1],':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🎃'):
                st.write(i[1],':', i[2])
    name = st.selectbox('我是……', ['帅哥', '美女'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
if page == zyjs:
    page_1()
elif page == wdxqtj:
    page_2()
elif page == wdtpclgj:
    page_3()
elif page == wdzncd:
    page_4()
elif page == wdxxxdjl:
    page_5()
elif page == zsdt:
    page_6()
elif page == bxdtz:
    page_7()
elif page == xxgk:
    page_8()
elif page == wdlyq:
    page_9()



