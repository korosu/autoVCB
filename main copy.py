import sys,os,shutil,re

file_names = [
    "[VCB-Studio] TenPuru [01][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [02][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [03][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [04][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [05][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [06][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [07][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [08][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [09][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [10][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [11][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [12][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [Extra01][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] TenPuru [Extra02][Ma10p_1080p][x265_flac].mkv",
    "[VCB-Studio] IS Infinite Stratos 2 [13(OVA)][Ma10p_1080p][x265_flac].mkv"
]

    
tcSubList = ['tc.srt', 'tc.ssa', 'tc.ass', 'tc.sub', 'tc.sbv', 'tc.smi', 'tc.vtt', 
            'jptc.srt', 'jptc.ssa', 'jptc.ass', 'jptc.sub', 'jptc.sbv', 'jptc.smi', 'jptc.vtt']

accepted_extensions=['.mp4', '.avi', '.mov', '.mkv','.srt', '.ssa', '.ass', '.sub']

ova = re.compile(r'\[ova\]', re.IGNORECASE)
episode = re.compile(r'\[\d{2}\]')
pattern = re.compile(r'\]([^\[]+)\[([^\]]+)\]')

def getEpisode(episodeRaw):
    match = re.search(r'\d+', episodeRaw)
    if match:
        number = match.group() 
    else:
        if "ova" in episodeRaw.lower():
            return "SP01"
        else:
            sys.exit()
    if re.match(r'^\d+$', episodeRaw):
        return "EP"+number
    if "extra" in episodeRaw.lower():
        return "SP"+number
    if int(number)>3:
        return "EP"+number
    return episodeRaw

# 过滤出文件，排除目录
for fileName in file_names:
    name=''
    episode=''
    dir = fileName

    #删除所有文件夹
    if(os.path.isdir(dir)):
        # shutil.rmtree(dir)
        continue

    #删除所有繁体字幕
    if any(suffix in fileName.lower() for suffix in tcSubList):
        # os.remove(dir)
        continue

    #删除所有不相关的文件
    if not fileName.lower().endswith(tuple(accepted_extensions)):
        # os.remove(dir)
        continue

    match = pattern.search(fileName)
    if match:
        # 提取第一个捕获组的内容
        name = match.group(1).strip()
        episode = getEpisode(match.group(2).strip())

    parts = fileName.split('.')
    if len(parts) > 1:
        file_extension = '.' + parts[-1]
    else:
        file_extension = ''  # 文件没有扩展名

    if name and episode and file_extension:
        newName = name+" "+episode+file_extension
        print(fileName)
        print(newName)