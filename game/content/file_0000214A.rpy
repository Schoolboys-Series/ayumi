# LM2RENPY Converter ©2017 GILESFVK ËKITES
#
# From LiveMaker Scene: 0000214A (Soundtrack)

init python:
    class SoundtrackPlayer(Action):
        def __init__(self, target_album, target_index, sound_list, playing_info_name):
            self.target_album = target_album
            self.target_index = target_index
            self.sound_list = sound_list
            self.playing_info_name = playing_info_name
        def __call__(self):
            if not (self.get_sensitive() and self.playing_info_name in globals()):
                return
            if self.get_selected():
                return
            renpy.music.stop('soundtrack', 0.2)
            renpy.music.play(self.sound_list[self.target_album]["item"][self.target_index]["path"], 'soundtrack', True)
            globals()[self.playing_info_name] = (self.target_album, self.target_index, renpy.music.get_duration('music'))
            renpy.restart_interaction()
        def get_sensitive(self):
            return self.target_album != None and self.target_index != None
        def get_selected(self):
            if not self.playing_info_name in globals():
                return False
            return self.target_album == globals()[self.playing_info_name][0] and self.target_index == globals()[self.playing_info_name][1]

label soundtrack_prepare:
    show black zorder -100
    with Dissolve(0.5)

    jump block_0000214B

    return

label block_0000214B:
    # Node: 0000214B ()
    $ soundtract_current_album = 4
    $ soundtrack_current_index = 0
    $ soundtrack_playing = (4, 0, 196.04898)
    $ set_place_title(False)

    jump block_0000214C

    return

label block_0000214C:
    # Node: 0000214C (Prepare)
    hide tag_BB4B85DBBFBF44DC9B3CC3B2F43AF6E3
    hide tag_747C986A971D4B81833D573429A46067
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    window hide

    stop music fadeout 2
    $ sys_music_current_file = ""

    $ zorder_tag_747C986A971D4B81833D573429A46067 = 0
    show rs_image_6AA1AE8F26894397B7B7A489DEA85104 as tag_747C986A971D4B81833D573429A46067 at center_bottom zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_07581C4E297D4018B7AB1E434A9EECA0

    hide tag_ECFB5B509A334A868686B3435242BF90
    with rs_effect_9271C226DF3F4D9F98AA8530D3BDF25B

    pause 0.5

    show rs_image_F64E3FF4BF7646D49B8E5DDD6B6B6E38 as tag_747C986A971D4B81833D573429A46067 zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_CDE613D22E9248719DB7B0AA90B2723F

    pause 1

    show rs_image_2F188FD479C04C6B8D3D474C29A22CA4 as tag_747C986A971D4B81833D573429A46067 zorder zorder_tag_747C986A971D4B81833D573429A46067 onlayer master
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    play soundtrack "sound/Piano/sti_gymno_01_pi.ogg" loop

    jump block_00003CA1

    return

label block_00003CA1:
    # Node: 00003CA1 (GenerateList)
    $ sound_list = [{
        "name": _("背景曲"), "intro": "",
        "item": [
            { "name": _("日常 1"), "intro": _("这首曲子第一次出现是在序章中，但不仅仅在这里，\n而是出现在整个游戏的各个地方，恐怕是大家印象最深刻的曲子。\n旋律和第一章步模式的背景音乐有点相似，都是为了表现夏天的\n日常时光。"), "path": "sound/BGM/Daily 1.ogg" },
            { "name": _("日常 2"), "intro": _("与“日常 1”不同，本曲旋律相对低缓了一些，气势也不再那么\n高昂。如果説“日常 1”表现的是初中少年们朝气蓬勃的一面，\n“日常 2”便是他们度过的由一个个奇迹连接而成的平凡日常。"), "path": "sound/BGM/Daily 2.ogg" },
            { "name": _("手足无措 1"), "intro": _("真正的手足无措，以略带混乱四处跳跃的旋律演奏，完全不知道\n该从哪里听起的曲子。"), "path": "sound/BGM/Flurry 1.ogg" },
            { "name": _("手足无措 2"), "intro": _("与其说“手足无措”，这首曲子更像是被逼的手足无措。从一开\n始不断重复的奇妙的上升旋律将整体代入了一个快节奏空间。不\n过背景音乐一直非常溷乱，结果还是不知道该从哪里听起。"), "path": "sound/BGM/Flurry 2.ogg" },
            { "name": _("平和 1"), "intro": _("这是一首吉他为主钢琴为辅的曲子。平缓的曲调讲述的不是故事，\n而是每天我们司空见惯的一切。"), "path": "sound/BGM/Guitar 1.ogg" },
            { "name": _("平和 2"), "intro": _("这是“平和 1”的后续，仍旧是那些乐器，仍旧是那个旋律，流\n逝而出的仍旧是如同空气一般理所应当的日常。"), "path": "sound/BGM/Guitar 2.ogg" },
            { "name": _("奇怪的酒店 1"), "intro": _("中世纪舞曲，此处被用来表现大家入住的酒店的奇妙和脱离日常。\n略带宗教风格的乐曲更是加重了这一感受。"), "path": "sound/BGM/Hotel 1.ogg" },
            { "name": _("奇怪的酒店 2"), "intro": _("相比刚入住时的激动和好奇，现在更多的则是冷静和对现状的把\n握。就算会发生什麽也不离奇的地方……"), "path": "sound/BGM/Hotel 2.ogg" },
            { "name": _("奇怪的酒店 3"), "intro": _("周围越来越奇怪，时间的流逝似乎出现了问题，这并不是梦，这\n是现实。既然是现实，就必须给出解决方法。可是，一筹莫展的\n现在，自己真的还正常吗……"), "path": "sound/BGM/Hotel 3.ogg" },
            { "name": _("见鬼了 1"), "intro": _("西洋宗教风，准确来说是基督教风格乐曲中用来描述恶魔场景的\n部分。鼓点和长号等低音乐器共同构筑了一幅尊贵的恶魔出场的\n画面。"), "path": "sound/BGM/Monster 1.ogg" },
            { "name": _("见鬼了 2"), "intro": _("主旋律使用了大量不稳定音，背景则充斥着腐朽的门窗等似乎是\n闹鬼老宅才会有的声音。就像真的要闹鬼一样。"), "path": "sound/BGM/Monster 2.ogg" },
            { "name": _("朔的洞窟"), "intro": _("和旋的音程非常不稳，不过主旋律却非常单纯。整体上来讲，和\n东方乐曲风格完全不同，确实很适合朔的身份。"), "path": "sound/BGM/Nori cave.ogg" },
            { "name": _("悠长的时间"), "intro": _("以提琴（小提琴和中提琴）为主的音乐。它所描述的时间，并不\n一定是现在，也可能只是回忆中的某一段。"), "path": "sound/BGM/Slowly time.ogg" },
            { "name": _("无语的想法"), "intro": _("比起“无语的想法”，这首曲子更适合被叫做“我无话可说”。\n总之就是对对方的言论不做评价，不予置评。"), "path": "sound/BGM/Strange idea.ogg" },
            { "name": _("友的房间"), "intro": _("这是一个放松而又安心的地方，是只属于自己的领地，是最重要\n的避风港，是自己最重要的朋友每天都会来的地方。"), "path": "sound/BGM/Tomo's room.ogg" }
        ]
    }, {
        "name": _("主题曲"), "intro": "",
        "item": [
            { "name": _("Don't be afraid!!"), "intro": _("本作的片头曲。"), "path": "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!!.ogg" },
            { "name": _("Don't be afraid!! （伴奏）"), "intro": _("本作片头曲的伴奏音轨。"), "path": "sound/BGM/Theme/Schoolboys Theme - Dont be afraid!! (Instrument).ogg" },
            { "name": _("愛を賭けて"), "intro": _("本作的片尾曲。"), "path": "sound/BGM/Theme/Schoolboys Theme - Bet of Love.ogg" },
            { "name": _("第一章节"), "intro": _("第一章步模式的背景音乐，有十足夏日气息的曲子。"), "path": "sound/BGM/Chapter 1.ogg" },
            { "name": _("第二章节"), "intro": _("第二章步模式的背景音乐，由于天气转凉旋律也变得悠长了。"), "path": "sound/BGM/Chapter 2.ogg" },
            { "name": _("第三章节"), "intro": _("第三章步模式的背景音乐。面对快要结束的学期，以及冬天的到\n来，心情也渐渐变得有些惆怅了。"), "path": "sound/BGM/Chapter 3.ogg" },
            { "name": _("学园活动"), "intro": _("体育祭和音乐祭的背景音乐。不是很清楚为什么要放这种史诗风\n格的音乐。"), "path": "sound/BGM/Celemony.ogg" },
            { "name": _("赤峰兄弟的训练"), "intro": _("和其他赤峰兄弟的曲子一样都是传统音乐风格。不过，因为这次\n涉及到训练的主题，曲调变得有些听起来很累（(⊙o⊙)…）"), "path": "sound/BGM/Series - Akamine brothers.ogg" },
            { "name": _("起点"), "intro": _("本作主菜单的音乐。"), "path": "sound/BGM/Start scene.ogg" },
            { "name": _("充满朝气的夕阳下"), "intro": _("描述了事件曲中“平和的午后”之后的时间。放学后，夕阳仍未\n西下，社团活动中，或是和朋友打闹中，不管怎样，一天都是充\n实的，都是无悔的，都是生命中珍贵的回忆。"), "path": "sound/BGM/Lively twilight.ogg" },
            { "name": _("英雄登场"), "intro": _("标准的热血漫画和特摄片的节奏。如果真正的英雄降临人世，或\n许就是这样的感觉也説不定呢。"), "path": "sound/BGM/Stage of HERO.ogg" },
            { "name": _("英雄末路"), "intro": _("何为正义？何为邪恶？\n正义和邪恶真的是两个水火不容的词语吗？\n如果说这是神规定的，是否有一天我们会向扔给我们谜题的神举\n起武器呢？"), "path": "sound/BGM/Drama.ogg" },
            { "name": _("御咲花车祭！"), "intro": _("传统日本祭典的鼓点声。花车祭也是一个拥有一定历史的活动，\n以后也绝对会一直举办下去的！"), "path": "sound/BGM/Drum.ogg" },
            { "name": _("漫才开始"), "intro": _("没有什么“大阪风”之类的説法。硬要说的话就是流行感。作为\n具有十足幽默感和流行性的城市，这样上世纪末风格的音乐正是\n在描述大阪文化圈最为辉煌的时期，也是杉本和陆田的出身地。"), "path": "sound/BGM/Manzai.ogg" },
            { "name": _("天使与恶魔"), "intro": _("基督教宗教风格音乐，不过并不传统，这是以现代乐器演奏的类\n似风格的音乐。单是听这首曲子的话，总觉得恶魔沾了上风。加\n油，恶魔！拿下友君！"), "path": "sound/BGM/Angel and Demon.ogg" },
            { "name": _("Ailurus fulgens"), "intro": _("小熊猫，拉丁语学名Ailurus fulgens。据说是一种毛茸茸、彭松松、\n无比可爱、令人无法自拔的动物。本游戏作者两人非常喜欢。"), "path": "sound/BGM/Ailurus fulgens.ogg" },
            { "name": _("寂静之夜"), "intro": _("全曲只有两种乐器，且都为敲击乐器，几乎没有任何和弦配合，\n所谓宁静的夜晚就是这样的。"), "path": "sound/BGM/Night.ogg" },
            { "name": _("宝物~卒業の春~"), "intro": _("和朋友分别，踏上各自闪光的道路。然后，以自己的姿态绽放。\n希望能永远在你身边欢笑，希望能叫出你的名字。\n就算分开，我们也在同一片蓝天下。我绝对不会忘记你。\n真的，只有一瞬……我们毕业了。"), "path": "sound/BGM/Treasure-Spring-of-Graduate.ogg" }
        ]
    }, {
        "name": _("事件曲"), "intro": "",
        "item": [
            { "name": _("平和的午后"), "intro": _("午后的时间是短暂的，却也难以忍耐，因为马上就要是放学时间。\n即便如此，放松心情慢慢等待也是值得的。"), "path": "sound/BGM/Afternoon.ogg" },
            { "name": _("敌人来袭"), "intro": _("乐曲中频繁出现早期电子游戏中常见的背景音乐的音符，彷佛就\n是遇敌的前兆。上昂的曲调则宣扬着战斗的意志。"), "path": "sound/BGM/Battle.ogg" },
            { "name": _("最终决战"), "intro": _("和上一首一样，仍是以怀旧感十足的早起电子乐为背景，不同的\n是鼓点动感十足。从中期开始旋律逐渐变得悠长，彷佛战斗的号\n角。末期的钢琴部分则诉说着战斗的间歇。"), "path": "sound/BGM/Final battle.ogg" },
            { "name": _("重重疑点"), "intro": _("整曲充斥着不稳定音反复构成的旋律，主旋律也显得无比诡异。\n背景中几乎没有其他乐器参与，试图塑造一个安静空间。却因为\n无处不在的不稳定音变得越发诡异。事情的真相愈加扑朔迷离。"), "path": "sound/BGM/Solve the case.ogg" },
            { "name": _("意料之外的展开"), "intro": _("比起对意料之外的事件的惊讶，这首曲子主要表现的是发生后无\n所适从的情景。不过事情已经发生，除了觉得比较奇怪外也无话\n可说了。"), "path": "sound/BGM/Something comical 1.ogg" },
            { "name": _("微妙的气氛"), "intro": _("犹如变魔术一般无法理解的气氛。即便从中期开始似乎有了那么\n一点头绪，最后还是没能搞明白现状。"), "path": "sound/BGM/Something strange 1.ogg" },
            { "name": _("暴风骤雨之前"), "intro": _("通过弹拨乐器的简短挑拨发出的促音构成了乐曲的主旋律，比起\n一般来说的有力的感觉更偏向莫名其妙的感觉一些。叫做“暴风\n骤雨之前”是因为这在本作中等于搞事用的BGM。"), "path": "sound/BGM/Something will happen.ogg" },
            { "name": _("感动的始末"), "intro": _("这是温暖人心的曲调。平和缓慢的旋律构成了乐曲的基础，带来\n温暖的感觉。不过，这首曲子也用在了“寻求刺激·解”里……"), "path": "sound/BGM/The end of touch.ogg" },
            { "name": _("追逐希望"), "intro": _("轻快的步伐，灵动的音符，这是这首曲子带给我们的感觉。对未\n来和希望的憧憬与信心，正是它独一无二的旋律。"), "path": "sound/BGM/The hope.ogg" },
            { "name": _("面向未来"), "intro": _("每四拍一次的突然停顿让这首乐曲有了一步一步递进的感觉，背\n景乐器则诉説着平澹而又欢乐的日常。这就是通向未来的道路。"), "path": "sound/BGM/To the future.ogg" },
            { "name": _("过去的宝物"), "intro": _("宝物不一定都是美好的。即便是那些痛苦的回忆，也是我们一起\n度过的时光。或许正是因为那些才会有现在的我们。或许……\n或许这会是一生中难忘的回忆……\n谢谢……对不起……"), "path": "sound/BGM/My precious time - piano.ogg" },
            { "name": _("过去的宝物……"), "intro": _("这是友和忍的所有相关曲目中唯一一首电子乐，也是他们初次分\n道扬镳之时的背景音乐。与印象曲中的不同，旋律内充满了紧张\n感。这既是友的孤注一掷，也是忍第一次感受到背叛的滋味。"), "path": "sound/BGM/My precious time.ogg" },
            { "name": _("珍重的时光"), "intro": _("本曲的主旋律可以分为前半段与后半段。前半段主要以钢琴为主，\n后半段则是电子乐器模拟的声音和钢琴混杂在一起。如果説一个\n是开心的时候，一个是难过的时候，那他们都是弥足珍贵的经历。"), "path": "sound/BGM/My precious time - slowly.ogg" },
            { "name": _("久远回忆"), "intro": _("那是很久很久之前了。\n那时候的我们，还什么都不知道，还什么都不懂。\n我所记忆犹新的经历。\n自从那一天开始……"), "path": "sound/BGM/The past precious.ogg" },
            { "name": _("面向未来之前"), "intro": _("从今以后，我们会向着各自不同的道路前行。\n道路终点的方向不尽相同，如果因此分离，也是无可奈何。\n慢慢习惯，渐渐适应，泯然日常……然后我们将会成为大人。\n正因如此，今后一起度过的而时光才会弥足珍贵，才更需要珍惜。"), "path": "sound/BGM/My precious time of now.ogg" },
            { "name": _("无比珍贵的现在"), "intro": _("“只有经过努力才能看到彩虹”有人这麽説，但努力是有尽头的。\n筋疲力竭之时，愿意拉你一把的，才是真正的朋友，才是真正的\n宝物。"), "path": "sound/BGM/My precious time of now - piano.ogg" }
        ]
    }, {
        "name": _("印象曲"), "intro": "",
        "item": [
            { "name": _("赤峰兄弟 1"), "intro": _("这首曲子更加侧重赤峰月，传统日本乐器、高昂的音调和悠扬的\n旋律共同塑造出了坚强开朗的少年这一形象。不过，背景里的其\n他乐器也是必不可少的，它们共同演奏着只属于他们的音符。"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 1.ogg" },
            { "name": _("赤峰兄弟 2"), "intro": _("除去鼓点外，这是一首由两种乐器演奏的音乐，一方负责主旋律，\n一方负责和弦，相辅相成，缺一不可。就旋律来看，这更适合作\n为日常曲，实际上，它也确实总出现在月和空单独相处的时候。"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 2.ogg" },
            { "name": _("赤峰兄弟 3"), "intro": _("非常古风的曲子，在赤峰兄弟的总共四首曲子中最有历史感。这\n是一首缅怀过去的乐曲。不过，缅怀过去是为了面向未来，这是\n毋庸置疑的。"), "path": "sound/BGM/Theme/Schoolboys Theme - Akamine brothers 3.ogg" },
            { "name": _("九尾 1"), "intro": _("平安时代的音乐风格，那也是妖怪和阴阳师的时代。采用日本传\n统乐器制作的这首以降调为主的曲子正是在叙述九尾辉煌的过去\n和微妙的现实。"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 1.ogg" },
            { "name": _("九尾 2"), "intro": _("近代日本的音乐风格，在传统中融入一定量西方元素，以悠扬的\n旋律体现历史的凝重。千年以来，九尾一直在此，直到那一天，\n它遇到……"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 2.ogg" },
            { "name": _("九尾 3"), "intro": _("风格重新回到古日本，不过和九尾的第一首印象曲不同，这首曲\n子非常明快。背景里偶尔出现的人声是神道教祭奠神灵的仪式，\n也就是祭典上常见的声音。九尾终于遇到了自己中意的人，可喜\n可贺，可喜可贺。"), "path": "sound/BGM/Theme/Schoolboys Theme - Kyubi 3.ogg" },
            { "name": _("木村与伊藤"), "intro": _("这是本作电子乐感最强的一首，其次就是三朗的印象曲。曲子本\n身不急不缓，电子乐构成的和弦却给乐曲本身添加了一层紧张感。\n值得一提的是，伊藤早已单恋木村很久，却因为对方有女友而一\n直不敢追求。以对方的幸福优先也是伊藤温柔的地方。"), "path": "sound/BGM/Theme/Schoolboys Theme - Kimura and Itou.ogg" },
            { "name": _("猫山三朗"), "intro": _("这也是野球拳场景的背景音乐。电子乐的大量出现使得这首曲子\n和本作其他乐曲存在较大差别，不过正好反映了三朗喜欢追赶潮\n流而又有些放荡不羁的性格。"), "path": "sound/BGM/Theme/Schoolboys Theme - Saburo.ogg" },
            { "name": _("奥村慎太郎"), "intro": _("基于未知原因，三朗美发店用的就是慎太郎的印象曲，不得不説\n是真爱。曲子本身没有朔那么诡异，但也有点诡异，给人一种想\n要搞事的感觉。不过，作为“御咲学园HOMO计划”的主要负责\n人，这还是非常恰当的。"), "path": "sound/BGM/Theme/Schoolboys Theme - Shintaro.ogg" },
            { "name": _("朔"), "intro": _("朔的所有音乐都很诡异，这可能与他外星人的身份有关。背景中\n偶尔出现的狼的声音代表了他作为WOLFS一员的身份。整体偏西\n化和宗教化的曲风也彰显了他不为人知的神秘一面。"), "path": "sound/BGM/Theme/Schoolboys Theme - Nori.ogg" },
            { "name": _("一之濑翼"), "intro": _("这是一位胆小怕事而又活在过去的少年。\n他不善于交往，终于在中学遇到可能会成为朋友的人，但这个愿\n望也破灭了。他不再前进，不敢追求自己的幸福，过去的一切对\n他而言是最美好的时光。希望有一天他能得到救赎，面向未来。"), "path": "sound/BGM/Theme/Schoolboys Theme - Tsubasa.ogg" },
            { "name": _("森海友 1"), "intro": _("这是友的第一首印象曲，从游戏开始便总是出现。友的印象曲\n中这首最为轻快，究竟这代表的是“轻快”还是“轻浮”就不\n好说了。"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 1.ogg" },
            { "name": _("森海友 2"), "intro": _("与友的其他印象曲一样，这是一首纯粹的钢琴曲。整曲音调偏\n高，变化不定，但都无比轻快。採用的和弦自始至终未曾变化，\n偶尔出现的不稳定音更是令乐曲本身更加贴近呆毛少年的本质。"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 2.ogg" },
            { "name": _("森海友 3"), "intro": _("作为友的三首印象曲中最正经的一首，它出现在第三章“变革\n进行曲“的部分，曲调也从之前的欢快为主变成了冷静的降调。\n这一次，他真的努力了，他真的做到了，这才是成为大人的必\n经之路。"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo 3.ogg" },
            { "name": _("友和忍"), "intro": _("这是一首乍听非常混沌的曲子。不过从中途开始，突然出现的一\n股降调钢琴段落颠覆了这一印象，之后曲调没有变化，但主旋律\n已经被突出，成为整首曲子的主要部分。"), "path": "sound/BGM/Theme/Schoolboys Theme - Tomo and Shinobu.ogg" },
            { "name": _("作哉与翼"), "intro": _("严格来说，这首曲子不是作哉和翼而是翼、作哉和小翼两人一狗\n的曲子。作哉是大家中生日最小的，却总被当做不良少年，但他\n其实非常温柔，就像这首曲子一样。希望他有朝一日能实现自己\n的愿望。"), "path": "sound/BGM/Theme/Schoolboys Theme - Sakuya and Tsubasa-chan.ogg" }
        ]
    }, {
        "name": _("钢琴曲"), "intro": "",
        "item": [
            { "name": _("Gymnopédie"), "intro": _("来自埃里克·萨蒂早年的作品。这是一个希腊语和法语的合成词，\n描述了“活泼的孩子光着脚玩耍”的样子。可惜一到2eme\nGymnopédie同人社团这里，突然就把人家脱光变成全裸了……"), "path": "sound/Piano/sti_gymno_01_pi.ogg" },
            { "name": _("La campanella"), "intro": _("波兰舞曲《英雄》，被认为是肖邦作品中的杰作。"), "path": "sound/Piano/rst_lacam_pi.ogg" },
            { "name": _("库普兰之墓"), "intro": _("为纪念十八世纪法国作曲家库普兰而由拉威尔创作的《库普兰之\n墓》。"), "path": "sound/Piano/rvl_prelude_pi.ogg" },
            { "name": _("悲怆奏鸣曲"), "intro": _("《La campanella》，意为“钟”，是由匈牙利作曲家弗朗茨·李\n斯特创作的《帕格尼尼大练习曲》中的一首钢琴独奏曲。"), "path": "sound/Piano/btb_hisou_2_pi.ogg" },
            { "name": _("英雄"), "intro": _("《Adagio Cantabile》，即贝多芬的《悲怆奏鸣曲》。"), "path": "sound/Piano/hero.ogg" }
        ]
    }]

    jump block_00003CA0

    return

label block_00003CA0:
    # Node: 00003CA0 (Update)
    call screen soundtrack(sound_list)

    jump block_00003C95

    return

screen soundtrack(sound_list):
    frame:
        style "soundtrack_frame"
        area (5, 60, 230, 530)
        has viewport:
            mousewheel "change"
            draggable True
            side_yfill True

        use soundtrack_content(sound_list, soundtract_current_album, soundtrack_playing)
    hbox:
        style "soundtrack_album"
        for i, album in enumerate(sound_list):
            textbutton album["name"]:
                text_style "soundtrack_album_button_text"
                action VariableTracker(i, "soundtract_current_album")
    # Progress will cause infinite loop, I don't know why.
    # add "images/Soundtrack/Progressbar.png" at soundtrack_progressbar(soundtrack_playing[2])
    text "♫ " + sound_list[soundtrack_playing[0]]["name"] + " - " + sound_list[soundtrack_playing[0]]["item"][soundtrack_playing[1]]["name"]:
        style "soundtrack_status_text"
    text sound_list[soundtrack_playing[0]]["item"][soundtrack_playing[1]]["intro"]:
        style "soundtrack_status_intro"
    textbutton _("返回"):
        xpos 700
        ypos 10
        text_style "soundtrack_album_button_text"
        action Return("")

screen soundtrack_content(sound_list, album_index, track_info):
    vbox:
        for i, soundtrack in enumerate(sound_list[album_index]["item"]):
            textbutton sound_list[album_index]["item"][i]["name"]:
                style "soundtrack_content_item"
                action SoundtrackPlayer(album_index, i, sound_list, "soundtrack_playing")

style soundtrack_status_intro:
    xpos 258
    ypos 450
    size 18
    color "#FFFFFF"
style soundtrack_status_text:
    xpos 425
    ypos 71
    size 16
    color "#FFFFFF"
style soundtrack_frame is default
style soundtrack_album:
    xpos 16
    ypos 10
style soundtrack_album_button_text:
    color "#FFFFFF"
    font "font/zcool-happy-ayumi-extended.ttf"
    outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
              (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
              (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]
    selected_color "#2D6BA5"
    selected_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                       (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                       (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
    hover_color "#2D6BA5"
    hover_outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
                    (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
                    (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
style soundtrack_content_item:
    ymargin 5
style soundtrack_content_item_text:
    color "#2D6BA5"
    font "font/source-hans-sans-medium.ttc"
    size 16
    outlines [(absolute(6), "#FFFFFF00", absolute(0), absolute(0)),
              (absolute(4), "#FFFFFF88", absolute(0), absolute(0)),
              (absolute(2), "#FFFFFFFF", absolute(0), absolute(0))]
    selected_color "#FFFFFF"
    selected_outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
                       (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
                       (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]
    hover_color "#FFFFFF"
    hover_outlines [(absolute(6), "#2D6BA500", absolute(0), absolute(0)),
                    (absolute(4), "#2D6BA588", absolute(0), absolute(0)),
                    (absolute(2), "#2D6BA5FF", absolute(0), absolute(0))]

transform soundtrack_progressbar(duration):
    xpos 413
    ypos 66
    block:
        xzoom 0.0
        linear duration xzoom 1.0
        repeat

label block_00003C95:
    # Node: 00003C95 (CLEAR)
    hide tag_747C986A971D4B81833D573429A46067
    hide tag_E6300DB69D254C278710366E7D300298
    hide tag_C6F01EC8F88A4AB093352F6D3F68197C
    hide tag_30A510E5705C4015819C44CDD628028A
    hide tag_7E30B19D592346FAA1C3C3A0E82D602F
    hide tag_83794CD575404B2B99772C15549BE0B7
    with rs_effect_351A8A667ECF419EB1A052B06E597A01

    stop music fadeout 0.5
    $ sys_music_current_file = ""

    jump block_00003C96

    return

label block_00003C96:
    # Node: 00003C96 ()
    $ del soundtract_current_album
    $ del soundtrack_current_index

    return
