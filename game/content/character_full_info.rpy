init 1000 python:
    def find_chatracter_version(character):
        result = { "addons": [] }
        for key, value in character.iteritems():
            if isinstance(value, list):
                result[key] = None
                for item in value:
                    if isinstance(item, dict):
                        if eval(item["condition"]):
                            result[key] = item["content"]
                            result["addons"].extend(item["addons"])
                    else:
                        result[key] = item
            else:
                result[key] = value
        return result

    character_full_info = [
        {
            "id": "Tomo",
            "name": _("{size=12}MORIUMI TOMO{/size}\n森海友"),
            "age": _("中学二年级"),
            "height": _("155cm"),
            "weight": _("48kg"),
            "birthdate": _("7月21日"),
            "blood": _("O"),
            "club": _("小钢琴部兼一班班长"),
            "pants": _("比基尼"),
            "appearances": [[
                ["C0SShinobu"],
                ["C1S1", "C1S2", "C1S3", "C1S5", "C1SSabuShin", "C1QNewsclub", "C1QKimuraConference", "C1QSabuShin", "C1QTsubasa", "C1QMatsuta"],
                ["C2S2", "C2S6", "C2SNori", "C2SYuuhi", "C2QNewsclub", "C2QKimuraConference", "C2QYuuhi", "C2QSora"],
                ["C3S1", "C3S3", "C3S4", "C3S5", "C3S6", "C3SPark", "C3SPhoto", "C3SShiroYuki", "C3SYukiToki", "C3QNewsclub", "C3QKimuraConference", "C3QShiro", "C3QNakayama", "C3QYakyuken", "C3QNori"]
            ]],
            "description": _("元气满满的小笨蛋。\n和忍是青梅竹马，住在同一所\n公寓的上面一层。对性的好奇心\n非常旺盛，随时持有“电摩”。\n因为母亲是钢琴家，以前也练习过，\n钢琴很不错。自己做饭，拿手料理\n“蛋包饭”。对呆毛很在意。")
        }, {
            "id": "Shinobu",
            "name": _("{size=12}AYASE SHINOBU{/size}\n绫濑忍"),
            "age": _("中学二年级"),
            "height": _("149cm"),
            "weight": _("40kg"),
            "birthdate": _("2月14日"),
            "blood": _("A"),
            "club": _("空手道部"),
            "pants": _("短裤"),
            "appearances": [[
                ["C0SShinobu"],
                ["C1S1", "C1S2", "C1S5"],
                ["C2S1", "C2S2", "C2S6"],
                ["C3S1", "C3S2", "C3S3", "C3S5", "C3S6", "C3SPhoto"]
            ]],
            "description": _("矮小无口的少年。\n一般来看很酷，但只要和青梅竹马\n的友说起话来就很孩子气。\n因为长相中性常被认错性别，\n对此有些烦恼。空手道黑带。\n生气时常用铁拳制裁。")
        }, {
            "id": "Tsubasa",
            "name": _("{size=12}ICHINOSE TSUBASA{/size}\n一之濑翼"),
            "age": _("中学二年级"),
            "height": _("155cm"),
            "weight": _("45kg"),
            "birthdate": _("1月11日"),
            "blood": _("O"),
            "club": _("小钢琴部兼二班班长"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1S2", "C1S3", "C1QTsubasa"],
                ["C2S2", "C2S6", "C2QKimuraConference"],
                ["C3S2", "C3S3", "C3S4", "C3S5", "C3S6", "C3QSakuyaWalk1"]
            ]],
            "description": [
                _("总是战战兢兢的弱气的男孩子。\n因为学号是1就被副班主任弄成了\n班长。年级开会时遇到了友，不知所措\n时被友的温柔感动，喜欢上了友。\n现在也仍然如此。之后和友组建了\n小钢琴部。偶尔会有些病娇。"),
                {
                    "condition": "C2S2 == True",
                    "content": _("总是战战兢兢的弱气的男孩子。\n因为学号是1就被副班主任弄成了\n班长。年级开会时遇到了友，不知所措\n时被友的温柔感动，喜欢上了友。\n现在也仍然如此。之后和友组建了\n小钢琴部。偶尔会有些病娇。"),
                    "addons": [
                        {
                            "content": _("追记：终于和作哉重归于好，现在两人一起照顾\n小翼，也开始学习饲育知识了。"),
                            "transform": Transform(xpos=233, ypos=550)
                        }
                    ]
                }
            ]
        }, {
            "id": "Shintarou",
            "name": _("{size=12}OKUMURA SHINTAROU{/size}\n奥村慎太郎"),
            "age": _("中学二年级"),
            "height": _("159cm"),
            "weight": _("50kg"),
            "birthdate": _("8月1日"),
            "blood": _("AB"),
            "club": _("花乃汤前台"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1S3", "C1SSabuShin", "C1QSabuShin"],
                ["C2S2", "C2S3", "C2S4", "C2S6"],
                ["C3S2", "C3S3", "C3S4", "C3S5", "C3S6", "C3SSabuShin", "C3QKimuraConference"]
            ]],
            "description": [
                _("性知识丰富的工口工口星人。\n自家的澡堂“花乃汤”其实在\n“那个”圈子里很有名。有次\n三朗误闯结果就变成了待宰羔羊。\n会接受恋爱咨询，给各种人建议，\n在御咲学园不断促成一对对情侣。"),
                {
                    "condition": "C2S4 == True",
                    "content": _("性知识丰富的工口工口星人。\n自家的澡堂“花乃汤”其实在\n{color=#FF0000}{s}“那个”圈子里很有名{/s}{/color}。有次\n三朗误闯结果就变成了待宰羔羊。\n会接受恋爱咨询，给各种人建议，\n在御咲学园不断促成一对对情侣。"),
                    "addons": [
                        {
                            "content": _("以后不会再有这种事情了"),
                            "transform": Transform(xpos=490,ypos=385)
                        }
                    ]
                }
            ]
        }, {
            "id": "Sakuya",
            "name": _("{size=12}HOUMI SAKUYA{/size}\n穗海作哉"),
            "age": _("中学二年级"),
            "height": _("162cm"),
            "weight": _("50kg"),
            "birthdate": _("4月1日"),
            "blood": _("B"),
            "club": _("篮球部兼二班体育委员"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                ["C1S1", "C1S4", "C1QTsubasa"],
                ["C2S2", "C2S6", "C2QSakuya"],
                ["C3S2", "C3S3", "C3S4", "C3S5", "C3S6", "C3QSakuyaWalk1", "C3QSakuyaWalk2"]
            ]],
            "description": [
                _("非常强势、有点不良感的少年。\n超喜欢动物，所以悄悄收留了\n在学校里迷路的小狗。对一之濑翼\n非常不友好，但这有原因，并不是\n讨厌。也因为这种极佳的照料水平\n受到低年级某些学生的仰慕。"),
                {
                    "condition": "C2S2 == True",
                    "content": _("非常强势、有点不良感的少年。\n超喜欢动物，所以悄悄收留了\n在学校里迷路的小狗。对一之濑翼\n非常不友好，但这有原因，并不是\n讨厌。也因为这种极佳的照料水平\n受到低年级某些学生的仰慕。"),
                    "addons": [
                        {
                            "content": _("追加：终于和翼和解，现在两人一起在滑子老师\n的援助下照顾小翼，完全变成饲育系了"),
                            "transform": Transform(xpos=233,ypos=553)
                        }
                    ]
                }
            ]
        }, {
            "id": "Tsuki",
            "name": _("{size=12}AKAMINE TSUKI{/size}\n赤峰月"),
            "age": _("中学二年级"),
            "height": _("166cm"),
            "weight": _("55kg"),
            "birthdate": _("6月9日"),
            "blood": _("A"),
            "club": _("剑道部"),
            "pants": _("传统兜裆布"),
            "appearances": [[
                [],
                ["C1S1", "C1QMatsuta"],
                ["C2S1", "C2S2", "C2S6", "C2QSakuya", "C2QSora"],
                ["C3S1", "C3S2", "C3S3", "C3S5", "C3S6", "C3QKimuraConference"]
            ]],
            "description": [
                _("空的异卵双胞胎哥哥。平时\n稳重冷静，可一旦遇到有关弟弟\n的事就会各种暴走。高智商低情商，\n最近因为视力下降开始戴眼镜。\n剑道部主将，自家也是道场，\n非常有希望成为继承人。"),
                {
                    "condition": "C1S1 == True",
                    "content": _("空的异卵双胞胎哥哥。平时\n稳重冷静，可一旦遇到有关弟弟\n的事就会各种暴走。高智商低情商，\n最近因为视力下降开始戴眼镜。\n剑道部主将，自家也是道场，\n非常有希望成为继承人。"),
                    "addons": [
                        {
                            "content": _("追记：已经是赤峰家道场的继承人了"),
                            "transform": Transform(xpos=240,ypos=549)
                        }
                    ]
                }
            ]
        }, {
            "id": "Sora",
            "name": _("{size=12}AKAMINE SORA{/size}\n赤峰空"),
            "age": _("中学二年级"),
            "height": _("161cm"),
            "weight": _("49kg"),
            "birthdate": _("6月9日"),
            "blood": _("B"),
            "club": _("剑道部"),
            "pants": _("传统兜裆布"),
            "appearances": [[
                [],
                ["C1S1", "C1QMatsuta"],
                ["C2S1", "C2S2", "C2S6", "C2QSora"],
                ["C3S2", "C3S3", "C3S4", "C3S5", "C3S6"]
            ]],
            "description": [
                _("温柔体贴，朋友很多，害怕虫子，\n喜欢甜食。点心做得很好，女子力\n极高。和哥哥月是双胞胎，但却总\n被认为是有年龄差的兄弟，对此有些\n想法。因为自己总是比不过哥哥怀有\n强烈的劣等感。"),
                {
                    "condition": "C1S1 == True",
                    "content": _("温柔体贴，朋友很多，害怕虫子，\n喜欢甜食。点心做得很好，女子力\n极高。和哥哥月是双胞胎，但却总\n被认为是有年龄差的兄弟，对此有些\n想法。{color=#FF0000}{s}因为自己总是比不过哥哥怀有\n强烈的劣等感。{/s}{/color}"),
                    "addons": [
                        {
                            "content": _("已经不存在这种事了"),
                            "transform": Transform(xpos=470,ypos=520)
                        }
                    ]
                }
            ]
        }, {
            "id": "Saburou",
            "name": _("{size=12}NEKOYAMA SABUROU{/size}\n猫山三朗"),
            "age": _("中学二年级"),
            "height": _("162cm"),
            "weight": _("48kg"),
            "birthdate": _("2月22日"),
            "blood": _("B"),
            "club": [
                _("篮球部"),
                {
                    "condition": "C2S4 == True",
                    "content": _("{color=#FF0000}{s}篮球部{/s}{/color}"),
                    "addons": [
                        {
                            "content": _("追加：现在是花乃汤前台"),
                            "transform": Transform(xpos=365,ypos=228)
                        }
                    ]
                }
            ],
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1S3", "C1QSabuShin"],
                ["C2S2", "C2S4", "C2S6"],
                ["C3S3", "C3S4", "C3S5", "C3S6", "C3SSabuShin", "C3SPark"]
            ]],
            "description": [
                _("喜欢说关西腔的活泼孩子。\n人如其名，怕狗怕水怕木天蓼。\n虽然在御咲学园却喜欢女人，\n曾向附近的御咲女学院的学生搭讪收获好人卡。\n很怕慎太郎，因为对方试图把自己弄弯。\n不知为何觉得作哉喜欢友。"),
                {
                    "condition": "C2S4 == True",
                    "content": _("喜欢说关西腔的活泼孩子。\n人如其名，怕狗怕水怕木天蓼。\n虽然在御咲学园却喜欢女人，\n曾向附近的御咲女学院的学生搭讪收获好人卡。\n{color=#FF0000}{s}很怕慎太郎{/s}{/color}，因为对方试图把自己弄弯。\n不知为何觉得作哉喜欢友。"),
                    "addons": [
                        {
                            "content": _("追加：终于意识到自己的感情\n开始和慎太郎交往了"),
                            "transform": Transform(xpos=240,ypos=549)
                        }
                    ]
                }
            ]
        }, {
            "id": "Shirou",
            "name": _("{size=12}NEKOYAMA SHIROU{/size}\n猫山四朗"),
            "age": _("小学六年级"),
            "height": _("144cm"),
            "weight": _("36kg"),
            "birthdate": _("5月5日"),
            "blood": _("A"),
            "club": _("篮球部"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S4"],
                ["C2S5", "C2QSakuya"],
                ["C3S3", "C3S5", "C3SYukiToki", "C3SShiroYuki", "C3QSakuyaWalk2", "C3QShiro"]
            ]],
            "description": _("三朗的弟弟。觉得自己的哥哥整个\n就是一反面教材，很鄙视。非常\n仰慕作哉，期待下一年能进入\n御咲学园。性格很认真，经常被\n雪绪恶作剧。")
        }, {
            "id": "Yukio",
            "name": _("{size=12}SAKAKI YUKIO{/size}\n榊雪绪"),
            "age": _("小学六年级"),
            "height": _("143cm"),
            "weight": _("37kg"),
            "birthdate": _("10月31日"),
            "blood": _("O"),
            "club": _("远足部"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S4"],
                ["C2S5"],
                ["C3S3", "C3S5", "C3SYukiToki", "C3SShiroYuki", "C3QSakuyaWalk2"]
            ]],
            "description": _("四朗的好朋友，喜欢恶作剧。\n说话经常带嘲讽语气。\n喜欢冒险，喜欢探索，所以夏天和\n四朗一起去爬银刚山。本该是\n很高兴的事，但从那之后身体\n经常变得很奇怪。")
        }, {
            "id": "Tsubasa-chan",
            "name": _("{size=12}TSUBASA{/size}\n小翼"),
            "age": _("十个月左右"),
            "height": _("50cm"),
            "weight": _("5kg"),
            "birthdate": _("12月27日"),
            "appearances": [[
                [],
                ["C1S4"],
                ["C2QSakuya"],
                ["C3S3", "C3S4", "C3QSakuyaWalk1", "C3QSakuyaWalk2"]
            ]],
            "description": _("曾迷路在御咲学园的非纯种狗，\n被作哉发现后养起来了。\n目前正在健康成长，对人友善，\n好奇心旺盛，总是元气满满。\n不过特别喜欢舔别人。")
        }, {
            "id": "Tsubasa-chan (Human)",
            "name": _("{size=12}TSUBASA{/size}\n小翼（人类版）"),
            "age": _("十三岁左右"),
            "height": _("155cm"),
            "weight": _("45kg"),
            "birthdate": _("12月27日"),
            "pants": _("没穿"),
            "appearances": [[
                [],
                ["C1S4"],
                [],
                ["C3S3", "C3QShiro"]
            ]],
            "description": _("喝下某触手给的药后小翼的样子。\n外表基本是复制了饲主作哉喜欢\n的一之濑翼的外貌。不过药效\n只有一天，天黑就变回狗了。\n之后在想能否有一天再把药拿到手\n继续变成人类的样子和大家一起玩。")
        }, {
            "id": "Nameko",
            "name": _("{size=12}Mr. NAMEKO{/size}\n滑子老师"),
            "age": _("四十岁"),
            "height": _("175cm"),
            "weight": _("80kg"),
            "club": _("二年级一班的班主任"),
            "appearances": [[
                [],
                [],
                ["C2S2"],
                ["C3S2"]
            ]],
            "description": _("生气起来非常可怕、但也非常\n体谅学生的可以信赖的好老师。\n对大型赛事很热衷。\n和二班的海老师关系不错。\n对妻子爱得非常深沉。")
        }, {
            "id": "Itou",
            "name": _("{size=12}ITOU KEI{/size}\n伊藤圭"),
            "age": _("中学二年级"),
            "height": _("157cm"),
            "weight": _("49kg"),
            "birthdate": _("6月6日"),
            "blood": _("O"),
            "club": _("田径部的经理"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QKimuraConference"],
                ["C2S3", "C2QKimuraConference"],
                ["C3S3", "C3S5", "C3QKimuraConference"]
            ]],
            "description": [
                _("作哉·三朗·木村所在的双低\n（智商、情商）集团唯一的良心。\n单恋木村许久，一直在因为对方有恋人\n而烦恼要不要放弃。按摩很拿手。"),
                {
                    "condition": "C2S3 == True",
                    "content": _("作哉·三朗·木村所在的双低\n（智商、情商）集团唯一的良心。\n单恋木村许久，{color=#FF0000}{s}一直在因为对方有恋人\n而烦恼要不要放弃{/s}{/color}。按摩很拿手。"),
                    "addons": [
                        {
                            "content": _("追加：终于结束单恋和木村顺利交往了"),
                            "transform": Transform(xpos=240,ypos=547)
                        }
                    ]
                }
            ]
        }, {
            "id": "Kimura",
            "name": _("{size=12}KIMURA ITSUKI{/size}\n木村树"),
            "age": _("中学二年级"),
            "height": _("165cm"),
            "weight": _("53kg"),
            "birthdate": _("10月10日"),
            "blood": _("A"),
            "club": _("田径部"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QKimuraConference"],
                ["C2S3", "C2QKimuraConference"],
                ["C3S3", "C3S5", "C3QKimuraConference"]
            ]],
            "description": [
                _("典型的脑袋是肌肉长的。\n有恋人，但交往不怎么顺利。\n体型很好，所以穿运动服的样子很\n吸引人，有不少粉丝。本人则非常迟钝，\n所以伊藤长久的单恋完全没有效果，\n罪恶深重的男人。性欲超强。"),
                {
                    "condition": "C2S3 == True",
                    "content": _("典型的脑袋是肌肉长的。\n{color=#FF0000}{s}有恋人，但交往不怎么顺利。{/s}{/color}\n体型很好，所以传、穿运动服的样子很\n吸引人，有不少粉丝。本人则非常迟钝，\n{color=#FF0000}{s}所以伊藤长久的单恋完全没有效果，{/s}{/color}\n罪恶深重的男人。性欲超强。"),
                    "addons": [
                        {
                            "content": _("已经两情相悦了"),
                            "transform": Transform(xpos=540,ypos=525)
                        }
                    ]
                }
            ]
        }, {
            "id": "Katou",
            "name": _("{size=12}KATOU JUNTA{/size}\n加藤准太"),
            "age": _("中学二年级"),
            "height": _("160cm"),
            "weight": _("51kg"),
            "birthdate": _("7月20日"),
            "blood": _("O"),
            "club": _("棒球部兼一班体育委员"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QKimuraConference"],
                ["C2S2", "C2QKimuraConference"],
                ["C3S3", "C3S5", "C3S6", "C3SPark", "C3QYakyuken"]
            ]],
            "description": _("元气满满的体育系男生！\n也完全不介意光膀子！\n成绩差到和友一个程度。\n放学后有时会和同学一起在\n商店街比谁吃得多。\n喜欢的类型是年上肌肉男！？")
        }, {
            "id": "Matsuda",
            "name": _("{size=12}MATSUDA KENJI{/size}\n松田健治"),
            "age": _("中学二年级"),
            "height": _("167cm"),
            "weight": _("55kg"),
            "birthdate": _("9月17日"),
            "blood": _("O"),
            "club": _("篮球部兼一班音乐委员"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QKimuraConference", "C1QMatsuta"],
                ["C2S2", "C2QKimuraConference"],
                ["C3S3", "C3S5", "C3S6", "C3SPark", "C3QYakyuken"]
            ]],
            "description": _("很有大人的样子，看起来像不良，\n其实很认真很喜欢照顾人。\n经常带着打火机，但只是为了\n掩盖拿了哥哥的烟的事实。\n觉得作哉很可爱。")
        }, {
            "id": "Izumi",
            "name": _("{size=12}IZUMI KAKERU{/size}\n泉翔"),
            "age": _("中学二年级"),
            "height": _("160cm"),
            "weight": _("48kg"),
            "birthdate": _("4月4日"),
            "blood": _("A"),
            "club": _("排球部"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1"],
                ["C2S2"],
                ["C3S3", "C3S5", "C3S6", "C3QNakayama", "C3QYakyuken"]
            ]],
            "description": _("温柔善良的性格。\n之前一直单恋排球部的前辈，\n在和慎太郎商讨过后成功交往。\n现在正因为恋人之间事情越来越多\n越来越复杂而困扰。")
        }, {
            "id": "Sato",
            "name": _("{size=12}SATOU HIKARU{/size}\n佐藤光"),
            "age": _("中学二年级"),
            "height": _("157cm"),
            "weight": _("47kg"),
            "birthdate": _("12月22日"),
            "blood": _("B"),
            "club": _("吹奏乐部兼二班音乐委员"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                ["C1S1"],
                ["C2S2"],
                ["C3S3", "C3S5", "C3S6"]
            ]],
            "description": _("看着老实，实则闹腾，喜欢古典\n音乐，经常炫耀自己精通这个。\n进入御咲学园似乎是为了加入\n很强的吹奏乐部。\n似乎在部内有在意的前辈，\n但本人极力否认。")
        }, {
            "id": "Okajima",
            "name": _("{size=12}OKAJIMA NAOYA{/size}\n冈岛直弥"),
            "age": _("中学二年级"),
            "height": _("161cm"),
            "weight": _("47kg"),
            "birthdate": _("2月21日"),
            "blood": _("AB"),
            "club": _("新闻部"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QNewsclub"],
                ["C2QNewsclub"],
                ["C3S3", "C3S5", "C3QNewsclub"]
            ]],
            "description": _("学习优秀、成绩进步的学霸。\n但却是一个和小岛一起成立新闻部、\n醉心于搞大新闻的奇怪少年。\n根本就没有性知识，那方面的话题\n完全跟不上。一般总是和小岛佐藤\n在一起。有一个三年级的哥哥，\n制服也是这麽来的。")
        }, {
            "id": "Kojima",
            "name": _("{size=12}KOJIMA TADASHI{/size}\n小岛正"),
            "age": _("中学二年级"),
            "height": _("148cm"),
            "weight": _("38kg"),
            "birthdate": _("11月30日"),
            "blood": _("AB"),
            "club": _("新闻部"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S1", "C1QNewsclub"],
                ["C2QNewsclub", "C2QKimuraConference"],
                ["C3S3", "C3S5", "C3QNewsclub"]
            ]],
            "description": _("在新闻部负责摄影，和部长不同是\n个很安静的怪孩子。会给提供有趣\n情报的人对方喜欢的照片。据本人说，\n“我们尊重肖像权”。非常喜欢部长\n冈岛，但有些过保护。")
        }, {
            "id": "Kiyo",
            "name": _("{size=12}KIYOSHI TAKEHITO{/size}\n清武一"),
            "age": _("中学一年级"),
            "height": _("150cm"),
            "weight": _("45kg"),
            "birthdate": _("10月25日"),
            "blood": _("O"),
            "club": _("空手道部"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S1", "C3S5", "C3QNakayama"]
            ]],
            "description": _("人如其名，清廉正直富有正义感。\n非常敬爱同部的前辈绫濑忍，\n梦想能成为前辈一样的人。")
        }, {
            "id": "Nakayama",
            "name": _("{size=12}NAKAYAMA KANON{/size}\n中山花音"),
            "age": _("中学一年级"),
            "height": _("150cm"),
            "weight": _("41kg"),
            "birthdate": _("3月6日"),
            "blood": _("A"),
            "club": _("排球部"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S1", "C3S5", "C3QNakayama"]
            ]],
            "description": _("轻浮性格。在和之前的恋人分手后，\n某天拾到了相性不错的大叔，\n开始了调教之旅。\n和清关系不错。")
        }, {
            "id": "Okajima-senior",
            "name": _("{size=12}OKAJIMA YUUSUKE{/size}\n冈岛雄介"),
            "age": _("中学三年级"),
            "height": _("165cm"),
            "weight": _("53kg"),
            "birthdate": _("3月14日"),
            "blood": _("AB"),
            "club": _("吹奏乐部"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S6"]
            ]],
            "description": [
                _("新闻部的冈岛直弥的哥哥。\n因为是吹奏乐部唯一的钢琴手，\n态度偶尔不端正。而后辈中的佐藤\n对此觉得很是问题。"),
                {
                    "condition": "C3S6 == True",
                    "content": _("新闻部的冈岛直弥的哥哥。\n{color=#FF0000}{s}因为是吹奏乐部唯一的钢琴手，\n态度偶尔不端正。而后辈中的佐藤\n对此觉得很是问题。{/s}{/color}"),
                    "addons": [
                        {
                            "content": _("在佐藤的计策下已经改掉这个问题了\n期待两人今后的发展"),
                            "transform": Transform(xpos=322,ypos=487)
                        }
                    ]
                }
            ]
        }, {
            "id": "Nakayama-senior",
            "name": _("{size=12}NAKAYAMA SHION{/size}\n中山紫音"),
            "age": _("中学三年级"),
            "height": _("172cm"),
            "weight": _("56kg"),
            "birthdate": _("4月7日"),
            "blood": _("A"),
            "club": _("排球部"),
            "pants": _("短裤"),
            "appearances": [[
                [],
                [],
                [],
                []
            ]],
            "description": _("中山花音的哥哥。和弟弟不同对各种事\n非常无所谓。恋人是排球部的泉。\n偶尔冷战，但一直很重视对方。")
        }, {
            "id": "Yuuhi",
            "name": _("{size=12}YUUHI{/size}\n夕阳"),
            "age": _("中学一年级"),
            "height": _("157cm"),
            "weight": _("50kg"),
            "birthdate": _("9月2日"),
            "blood": _("O"),
            "club": _("足球部兼魔法师"),
            "pants": _("四角裤或比基尼"),
            "appearances": [[
                [],
                [],
                ["C2S6", "C2SYuuhi", "C2QYuuhi"],
                ["C3S2", "C3QNewsclub", "C3QNori"]
            ]],
            "description": _("被师父认可才能后作为正义的\n魔法师守护着城市的和平。\n因为不愿学习，初级魔法都\n用不好。一直在和企图征服世界\n的Wolf's的朔进行工口战斗，打着\n打着就喜欢上对方了。")
        }, {
            "id": "Mamoru",
            "name": _("{size=12}SEIGI MAMORU{/size}\n世依木守"),
            "age": _("中学一年级"),
            "height": _("157cm"),
            "weight": _("46kg"),
            "birthdate": _("6月1日"),
            "blood": _("A"),
            "club": _("足球部兼英雄"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                [],
                ["C2S6"],
                ["C3S2", "C3QNewsclub"]
            ]],
            "description": _("和魔法师夕阳一起守护城市的\n正义的英雄，特技是GYMNO BEAM。\n恋人是过去战斗过并打倒的\n章鱼章鱼星人。似乎在不为人知\n的地方会做这样那样的事？")
        }, {
            "id": "Tentacle-earthworm",
            "name": _("{size=12}TENTACLE EARTHWORM{/size}\n触手A"),
            "height": _("没量过"),
            "weight": _("似乎很轻？"),
            "birthdate": _("不知"),
            "club": _("Wolf's"),
            "appearances": [[
                [],
                ["C1QNewsclub"],
                ["C2S6"],
                []
            ]],
            "description": _("Wolf's的一员。最早开始侍奉朔\n的触手，同时也是管家。说话\n像老妈子，很绅士。\n被其他触手信赖。")
        }, {
            "id": "Tentacle-starfish",
            "name": _("{size=12}TENTACLE STARFISH{/size}\n触手B"),
            "height": _("没量过"),
            "weight": _("似乎很轻？"),
            "birthdate": _("不知"),
            "club": _("Wolf's"),
            "appearances": [[
                [],
                [],
                ["C2S6"],
                []
            ]],
            "description": _("Wolf's的一员。才刚开始加入朔\n的队伍。背后有无数触手，\n是备受期待的新人。看起来似乎\n不很努力，但也在奋力学习\n如何侍奉。")
        }, {
            "id": "Tour-guide",
            "name": _("{size=12}TOUR GUIDE?{/size}\n导游？"),
            "age": _("不知"),
            "height": _("190cm"),
            "weight": _("不详"),
            "appearances": [[
                [],
                [],
                ["C2S6"],
                []
            ]],
            "description": _("离岛的度假酒店的导游……\n才不是，其实里面是触手A和触手B。\n整个旅行都是朔的计划。")
        }, {
            "id": "Nori",
            "name": _("{size=12}NORI{/size}\n朔"),
            "age": _("十三岁左右？"),
            "height": _("152cm"),
            "weight": _("40kg"),
            "club": _("Wolf's"),
            "pants": _("没有资料"),
            "appearances": [[
                [],
                ["C1S5"],
                ["C2S6", "C2SNori"],
                ["C3QNori"]
            ]],
            "description": _("企图征服世界的组织Wolf's的一员。\n操纵着触手怪物，喜欢玩弄敌人。\n某些意义上和忍关系很好，\n偶尔一起出门。\n正在进行从欲望中提取能量的研究，\n为此不断寻找实验体。")
        }, {
            "id": "Kai",
            "name": _("{size=12}KAI{/size}\n晦"),
            "age": _("二十左右"),
            "height": _("159cm"),
            "weight": _("46kg"),
            "birthdate": _("5月14日"),
            "club": _("Wolf's"),
            "pants": _("这……"),
            "appearances": [[
                [],
                [],
                ["C2S6"],
                []
            ]],
            "description": _("朔的哥哥，豪迈奔放。\n和Wolf's一贯的方针不同，\n现在正在地球上离岛的宾馆悠闲度日。\n在梅咲开的酒吧一下子就成了热门。\n好像有个高中生恋人。")
        }, {
            "id": "Dark lesser",
            "name": _("{size=12}DARK LESSER{/size}\n暗黑小熊猫"),
            "height": _("两到三米"),
            "weight": _("150kg-250kg"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S2"]
            ]],
            "description": _("英文叫Dark lesser，是小熊猫型的巨大怪兽。\n外表凶恶，爪子锋利，\n但其实只是好奇心旺盛，无甚危害。\n喜欢苹果。")
        }, {
            "id": "MonsterA",
            "name": _("{size=12}MONSTER A{/size}\n妖怪A"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S5"]
            ]],
            "description": _("从“上古封印之箱”里逃出来的\n妖怪中的一个。因为兴致总是\n很好，被认为是妖怪们的领导。\n计划把御咲学园封闭在异空间内，\n但被以忍为首的救援组打败了。")
        }, {
            "id": "MonsterB",
            "name": _("{size=12}MONSTER B{/size}\n妖怪B"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S5"]
            ]],
            "description": _("从“上古封印之箱”里逃出来的\n妖怪中的一个。总是很知性、很\n做作的样子，在和作哉们所在的\n回收组战斗时最后在九尾手上\n灰飞烟灭。")
        }, {
            "id": "MonsterC",
            "name": _("{size=12}MONSTER C{/size}\n妖怪C"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S5"]
            ]],
            "description": _("从“上古封印之箱”里逃出来的\n正太控妖怪的一个。曾经从箱子\n里出来过一次夜里“拜访”\n慎太郎，但手都没下去，为此\n耿耿于怀，最后被常磐给的\n符咒打败。")
        }, {
            "id": "Kobayashi",
            "name": _("{size=12}KOBAYASHI{/size}\n小林"),
            "age": _("小学四年级"),
            "height": _("133cm"),
            "weight": _("30kg"),
            "birthdate": _("1月17日"),
            "blood": _("O"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S4"],
                [],
                []
            ]],
            "description": _("放学后总是和南在公园玩的活泼\n的男孩子，也经常和友、慎太郎、\n空、散歩中的作哉玩。最近迷上了\n老游戏。本人言：每当看到南时\n心跳就会不自觉加快……")
        }, {
            "id": "Minami",
            "name": _("{size=12}MINAMI{/size}\n南"),
            "age": _("小学四年级"),
            "height": _("132cm"),
            "weight": _("31kg"),
            "birthdate": _("2月28日"),
            "blood": _("O"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S4"],
                [],
                []
            ]],
            "description": _("和小林关系好到不得了。\n有小气的一面，但好奇心旺盛，\n经常和小林到处捣乱。\n完全不知道下流梗。\n家里养了只猫。")
        }, {
            "id": "Sugimoto",
            "name": _("{size=12}SUGIMOTO KOKORO{/size}\n杉本志"),
            "age": _("小学六年级"),
            "height": _("146cm"),
            "weight": _("38kg"),
            "birthdate": _("8月9日"),
            "blood": _("B"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                ["C1S1"],
                [],
                []
            ]],
            "description": _("吉木与行所属“陆田&杉本”中的\n玩梗担当。成为艺人刚一年多。\n经常玩以前从没有人玩过的梗，\n外加体型问题，在部分人中获得了赞赏。\n刚出道所以只在关西地方偶像圈，\n不过目标是全国！\n大家也要来多多应援！")
        }, {
            "id": "Rikuta",
            "name": _("{size=12}RIKUTA ISAO{/size}\n陆田功"),
            "age": _("小学六年级"),
            "height": _("145cm"),
            "weight": _("38kg"),
            "birthdate": _("11月5日"),
            "blood": _("B"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S1"],
                [],
                []
            ]],
            "description": _("吉木与行所属“陆田&杉本”中的\n吐槽担当。槽点都是杉本想的，\n不过在听到内容后也能给出精彩的吐槽。\n和杉本是青梅竹马，虽说舞台上吐槽\n毫不留情，但其实比谁都要重视杉本，\n认为他是自己最重要的人。")
        }, {
            "id": "Kyuubi",
            "name": _("{size=12}KYUUBI{/size}\n九尾"),
            "age": _("千岁以上"),
            "birthdate": _("怎么可能知道"),
            "pants": _("和雪绪一样吧"),
            "appearances": [[
                [],
                [],
                ["C2S5"],
                ["C3S5", "C3SYukiToki", "C3QSakuyaWalk2"]
            ]],
            "description": _("银刚山深处作为神受到祭祀的狐狸。\n似乎是顶级妖怪。\n以前凭依体毁坏所以失去了大部分力量，\n现在附身在波长吻合的雪绪身上。\n通过在各种意义上不断做各种事情\n正逐渐取回力量。")
        }, {
            "id": "Tokiwa",
            "name": _("{size=12}TOKIWA SUSUMU{/size}\n常磐进"),
            "age": _("中学三年级？"),
            "height": _("160cm"),
            "weight": _("46kg"),
            "birthdate": _("问不出来"),
            "pants": _("三角裤"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S5", "C3SYukiToki"]
            ]],
            "description": _("不知为何一直静静地站在学园外的厕所旁。\n总能事先察觉到周围的异常和未来的事情，\n并据此给各种人各种有益的建议。\n表情一直很寂寞，似乎并不开心。")
        }, {
            "id": "Shougintoki",
            "name": _("{size=12}SUWABE SHOUGINTOKI{/size}\n诹访部翔银时"),
            "age": _("八十八岁"),
            "height": _("180cm"),
            "weight": _("74kg"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S3", "C3QSakuyaWalk2"]
            ]],
            "description": _("经常光顾花乃汤的老大爷，\n被其他客人称呼为“会长”。\n曾是御咲学园的学生，性格\n硬派刚正。现在非常担心慎太郎的\n身体健康。有一个25岁的孙子。")
        }, {
            "id": "Shouhei",
            "name": _("{size=12}SUWABE SHOUHEI{/size}\n诹访部翔平"),
            "age": _("二十五岁"),
            "height": _("176cm"),
            "weight": _("65kg"),
            "appearances": [[
                [],
                [],
                [],
                ["C3S1"]
            ]],
            "description": _("超重度正太控上班族。\n经常目不转睛看着各种少年，\n要是少年什么都好。\n人型自走大变态。\n当然，被请去喝茶还是没有过的。\n持有合气道段位，意外很强。")
        }, {
            "id": "Sakase",
            "name": _("{size=12}SAKASE KOUYA{/size}\n逆濑荒哉"),
            "age": _("中学二年级"),
            "height": _("162cm"),
            "weight": _("50kg"),
            "birthdate": _("4月30日"),
            "blood": _("A"),
            "pants": _("四角裤"),
            "appearances": [[
                [],
                ["C1S5"],
                [],
                []
            ]],
            "description": _("小学的时候特别喜欢欺负友和忍。\n因为父母的工作经常搬家，\n那时候也因为这个有半年\n转到了其他学校。\n现在住在关东。")
        }, {
            "id": "He--",
            "name": _("{size=12}HE{/size}\n黑——"),
            "height": _("60cm"),
            "weight": _("6kg"),
            "appearances": [[
                [],
                [],
                [],
                []
            ]],
            "description": _("感情内敛的小熊猫。\n脾气不大好。")
        }, {
            "id": "Be--",
            "name": _("{size=12}BE{/size}\n贝——"),
            "height": _("60cm"),
            "weight": _("6kg"),
            "appearances": [[
                [],
                ["C1S4"],
                [],
                ["C3QShiro"]
            ]],
            "description": _("和小翼很要好的小熊猫。\n不知为何不待见友。")
        }
    ]

    scene_var_description = {
        "C0SShinobu": _("可选对话《帮帮我，忍A梦！》"),
        "C1S1": _("事件《大家来相扑》"),
        "C1S2": _("事件《翼的流转音符》"),
        "C1S3": _("事件《寻求刺激·解》"),
        "C1S4": _("事件《不可思议！猫狗物语》"),
        "C1S5": _("事件《久远回忆》"),
        "C1SSabuShin": _("小故事《三朗的烦恼》"),
        "C2S1": _("事件《并驶之舟》"),
        "C2S2": _("事件《傲娇男孩子的治疗法》"),
        "C2S3": _("事件《RUN☆RUN☆LOVERS》"),
        "C2S4": _("事件《我是直的，现无对象》"),
        "C2S5": _("事件《狐的报恩》"),
        "C2S6": _("事件《欢迎来到食人狼之馆》"),
        "C2SNori": _("小故事《在意的魔法师 续》"),
        "C2SYuuhi": _("小故事《魔法森林》"),
        "C3S1": _("事件《异我战纪》"),
        "C3S2": _("事件《正义的教训》"),
        "C3S3": _("事件《集合！御咲花车祭》"),
        "C3S4": _("事件《傲娇男孩子的激效疗》"),
        "C3S5": _("事件《学园怪谈》"),
        "C3S6": _("事件《变革进行曲》"),
        "C3SSabuShin": _("小故事《慎太郎的烦恼》"),
        "C3SPark": _("小故事《埋伏作战》"),
        "C3SPhoto": _("小故事《照片和记忆》"),
        "C3SYukiToki": _("小故事《常磐前辈》"),
        "C3SShiroYuki": _("小故事《喝茶风波》"),
        "C1QNewsclub": _("委托《找到巨大蚯蚓》"),
        "C1QKimuraConference": _("委托《木村讨论会 上》"),
        "C1QSabuShin": _("委托《抓捕三朗》"),
        "C1QTsubasa": _("委托《翼的守护神？》"),
        "C1QMatsuta": _("委托《月是花花公子！？》"),
        "C2QNewsclub": _("委托《厕所的花子君》"),
        "C2QKimuraConference": _("委托《木村讨论会 中》"),
        "C2QYuuhi": _("委托《在意的魔法师》"),
        "C2QSakuya": _("委托《猫狗物语 续》"),
        "C2QSora": _("委托《蛋糕大作战》"),
        "C3QNewsclub": _("委托《与此世之恶交战的少年们》"),
        "C3QKimuraConference": _("委托《木村讨论会 下》"),
        "C3QSakuyaWalk1": _("委托《饲育系未来计划》"),
        "C3QSakuyaWalk2": _("委托《前进》"),
        "C3QShiro": _("委托《脑残游戏》"),
        "C3QNakayama": _("委托《重归于好？》"),
        "C3QYakyuken": _("委托《野球拳》"),
        "C3QNori": _("委托《见习魔法师的任务 II》")
    }
