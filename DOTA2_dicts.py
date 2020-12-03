#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 可以在这里添加新的阴阳怪气, {}为昵称位置

# 单排的阴阳怪气
WIN_NEGATIVE_SOLO = [
    '{}侥幸赢得了比赛',
    '{}走狗屎运赢得了比赛',
    '{}躺赢了比赛',
    '{}打团都没来, 队友4V5赢得了比赛'
]

WIN_POSTIVE_SOLO = [
    '{}带领团队走向了胜利',
    '{}暴打对面后赢得了胜利',
    '{} CARRY全场赢得了胜利',
    '{}把对面当猪宰了, 赢得了胜利',
    '{}又赢了, 这游戏就是这么枯燥, 且乏味',
]

LOSE_NEGATIVE_SOLO = [
    '{}被人按在地上摩擦, 输掉了这场比赛',
    '{}悲惨地输掉了比赛',
    '{}头都被打歪了, 心态爆炸地输掉了比赛',
    '{}捕鱼被鱼吃了, 输掉了比赛',
    '{}打的是个几把'
]

LOSE_POSTIVE_SOLO = [
    '{}无力回天输掉了比赛',
    '{}尽力了, 但还是输了比赛',
    '{}背靠世界树, 虽败犹荣',
    '{}带不动队友, 输了比赛',
    '{}又输了, 很难受, 宁愿输的是我',
]

# 组排的阴阳怪气
WIN_NEGATIVE_PARTY = [
    '{}侥幸赢得了比赛',
    '{}走狗屎运赢得了比赛',
    '{}躺赢了比赛',
    '{}打团都没来, 队友4V5赢得了比赛'
]

WIN_POSTIVE_PARTY = [
    '{}带领团队走向了胜利',
    '{}暴打对面后赢得了胜利',
    '{} CARRY全场赢得了胜利',
    '{}把对面当猪宰了, 赢得了胜利',
    '{}又赢了, 这游戏就是这么枯燥, 且乏味',
]

LOSE_NEGATIVE_PARTY = [
    '{}被人按在地上摩擦, 输掉了这场比赛',
    '{}悲惨地输掉了比赛',
    '{}头都被打歪了, 心态爆炸地输掉了比赛',
    '{}捕鱼被鱼吃了, 输掉了比赛',
    '{}打的是个几把'
]

LOSE_POSTIVE_PARTY = [
    '{}无力回天输掉了比赛',
    '{}尽力了, 但还是输了比赛',
    '{}背靠世界树, 虽败犹荣',
    '{}带不动队友, 输了比赛',
    '{}又输了, 很难受, 宁愿输的是我',
]

GAME_MODE = {
    0: "No Game Mode",
    1: "全英雄选择",
    2: "队长模式",
    3: "随机征召",
    4: "小黑屋",
    5: "全部随机",
    7: "万圣节活动",
    8: "反队长模式",
    9: "贪魔活动",
    10: "教程",
    11: "中路模式",
    12: "生疏模式",
    13: "新手模式",
    14: "Compendium Matchmaking",
    15: "自定义游戏",
    16: "队长征召",
    17: "平衡征召",
    18: "技能征召",
    19: "活动模式",
    20: "全英雄死亡随机",
    21: "中路SOLO",
    22: "全英雄选择",
    23: "加速模式"
}


LOBBY = {
    -1: "非法ID",
    0:  "普通匹配",
    1:  "练习",
    2:  "锦标赛",
    3:  "教程",
    4:  "合作对抗电脑",
    5:  "组排模式",
    6:  "单排模式",
    7:  "天梯匹配",
    8:  "中路SOLO",
    12: "夜魇暗潮"
}


# 服务器ID列表
AREA_CODE = {
    111: "美国西部",
    112: "美国西部",
    114: "美国西部",
    121: "美国东部",
    122: "美国东部",
    123: "美国东部",
    124: "美国东部",
    131: "欧洲西部",
    132: "欧洲西部",
    133: "欧洲西部",
    134: "欧洲西部",
    135: "欧洲西部",
    136: "欧洲西部",
    142: "南韩",
    143: "南韩",
    151: "东南亚",
    152: "东南亚",
    153: "东南亚",
    161: "中国",
    163: "中国",
    171: "澳大利亚",
    181: "俄罗斯",
    182: "俄罗斯",
    183: "俄罗斯",
    184: "俄罗斯",
    185: "俄罗斯",
    186: "俄罗斯",
    191: "欧洲东部",
    192: "欧洲东部",
    200: "南美洲",
    202: "南美洲",
    203: "南美洲",
    204: "南美洲",
    211: "非洲南部",
    212: "非洲南部",
    213: "非洲南部",
    221: "中国",
    222: "中国",
    223: "中国",
    224: "中国",
    225: "中国",
    231: "中国",
    236: "中国",
    242: "智利",
    251: "秘鲁",
    261: "印度"
}


# 英雄昵称
# 每个英雄的第一个为游戏内默认名字
HEROES_LIST_CHINESE = {
    1:   ['敌法师', '敌法', 'AM'],
    2:   ['斧王'],
    3:   ['祸乱之源', '祸乱', '水桶腰'],
    4:   ['血魔'],
    5:   ['水晶室女', '冰女', 'CM'],
    6:   ['卓尔游侠', '小黑'],
    7:   ['撼地者', '小牛'],
    8:   ['主宰', '剑圣', 'jugg', '奶棒人'],
    9:   ['米拉娜', '白虎', 'pom'],
    10:  ['变体精灵', '水人'],
    11:  ['影魔', '影魔王', 'SF', '影儿魔儿'],
    12:  ['幻影长矛手', 'PL'],
    13:  ['帕克'],
    14:  ['帕吉', '屠夫', '扒鸡', '啪唧'],
    15:  ['剃刀', '电魂', '电棍'],
    16:  ['沙王', 'SK'],
    17:  ['风暴之灵', '蓝猫'],
    18:  ['斯温', '流浪剑客', '流浪'],
    19:  ['小小'],
    20:  ['复仇之魂', '复仇', 'VS'],
    21:  ['风行者', '风行', 'WR'],
    22:  ['宙斯'],
    23:  ['昆卡', '船长'],
    25:  ['莉娜', '火女'],
    26:  ['莱恩', '恶魔巫师', 'Lion'],
    27:  ['暗影萨满', '小Y', '小歪'],
    28:  ['斯拉达', '大鱼', '大鱼人'],
    29:  ['潮汐猎人', '潮汐', '西瓜皮'],
    30:  ['巫医'],
    31:  ['巫妖'],
    32:  ['力丸', '隐形刺客', '隐刺'],
    33:  ['谜团'],
    34:  ['修补匠', 'TK', 'Tinker'],
    35:  ['狙击手', '矮人火枪手', '火枪', '传说哥'],
    36:  ['瘟疫法师', '死灵法', 'NEC'],
    37:  ['术士'],
    38:  ['兽王'],
    39:  ['痛苦女王', '女王', 'QOP'],
    40:  ['剧毒术士', '剧毒'],
    41:  ['虚空假面', '虚空', 'JB脸'],
    42:  ['冥魂大帝', '骷髅王'],
    43:  ['死亡先知', 'DP'],
    44:  ['幻影刺客', '幻刺', 'PA'],
    45:  ['帕格纳', '骨法', '湮灭法师'],
    46:  ['圣堂刺客', '圣堂', 'TA'],
    47:  ['冥界亚龙', '毒龙', 'Viper'],
    48:  ['露娜', '月骑', 'Luna'],
    49:  ['龙骑士', '龙骑'],
    50:  ['戴泽', '暗影牧师', '暗牧'],
    51:  ['发条技师', '发条'],
    52:  ['拉席克', '老鹿'],
    53:  ['先知'],
    54:  ['噬魂鬼', '小狗'],
    55:  ['黑暗贤者', '黑贤'],
    56:  ['克林克兹', '小骷髅'],
    57:  ['全能骑士', '全能'],
    58:  ['魅惑魔女', '小鹿'],
    59:  ['哈斯卡', '神灵', '神灵武士'],
    60:  ['暗夜魔王', '夜魔'],
    61:  ['育母蜘蛛', '蜘蛛'],
    62:  ['赏金猎人', '赏金'],
    63:  ['编织者', '蚂蚁'],
    64:  ['杰奇洛', '双头龙'],
    65:  ['蝙蝠骑士', '蝙蝠'],
    66:  ['陈', '老陈'],
    67:  ['幽鬼', 'SPE', 'UG'],
    68:  ['远古冰魄', '冰魂'],
    69:  ['末日使者', '末日', 'Doom'],
    70:  ['熊战士', '拍拍', '拍拍熊'],
    71:  ['裂魂人', '白牛'],
    72:  ['矮人直升机', '飞机'],
    73:  ['炼金术士', '炼金'],
    74:  ['祈求者', '卡尔'],
    75:  ['沉默术士', '沉默'],
    76:  ['殁境神蚀者', '黑鸟'],
    77:  ['狼人'],
    78:  ['酒仙', '熊猫', '熊猫酒仙'],
    79:  ['暗影恶魔', '毒狗'],
    80:  ['德鲁伊', '熊德'],
    81:  ['混沌骑士', '混沌', 'CK'],
    82:  ['米波'],
    83:  ['树精卫士', '大树', '树精'],
    84:  ['食人魔魔法师', '蓝胖'],
    85:  ['不朽尸王', '尸王'],
    86:  ['拉比克'],
    87:  ['干扰者', '萨尔'],
    88:  ['司夜刺客', '小强'],
    89:  ['娜迦海妖', '小娜迦'],
    90:  ['光之守卫', '光法'],
    91:  ['艾欧', '小精灵'],
    92:  ['维萨吉', '死灵龙', '死灵飞龙'],
    93:  ['斯拉克', '小鱼', '小鱼人'],
    94:  ['美杜莎', '一姐', '美杜莎'],
    95:  ['巨魔战将', '巨魔', '巨馍蘸酱'],
    96:  ['半人马战行者', '人马', '半人马'],
    97:  ['马格纳斯', '猛犸'],
    98:  ['伐木机'],
    99:  ['钢背兽', '钢背'],
    100: ['巨牙海民', '海民'],
    101: ['天怒法师', '天怒'],
    102: ['亚巴顿'],
    103: ['上古巨神', '大牛'],
    104: ['军团指挥官', '军团'],
    105: ['工程师', '炸弹', '炸弹人'],
    106: ['灰烬之灵', '火猫'],
    107: ['大地之灵', '土猫'],
    108: ['孽主', '大屁股'],
    109: ['恐怖利刃', 'TB'],
    110: ['凤凰'],
    111: ['神谕者', '神谕'],
    112: ['寒冬飞龙', '冰龙'],
    113: ['天穹守望者', '电狗'],
    114: ['齐天大圣', '大圣'],
    119: ['邪影芳灵', '小仙女'],
    120: ['石鳞剑士', '滚滚'],
    121: ['天涯墨客', '墨客'],
    126: ['虚无之灵', '紫猫'],
    128: ['电炎绝手', '老奶奶'],
    129: ['玛尔斯']
}