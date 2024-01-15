import sys,os,shutil,re

if len(sys.argv) <= 1:
    print('没有路径')
    sys.exit()

default = "/2t/VCB-Studio/"
path = default + sys.argv[1]

tcSubList = ['tc.srt', 'tc.ssa', 'tc.ass', 'tc.sub', 'tc.sbv', 'tc.smi', 'tc.vtt', 
            'jptc.srt', 'jptc.ssa', 'jptc.ass', 'jptc.sub', 'jptc.sbv', 'jptc.smi', 'jptc.vtt']

accepted_extensions=['.mp4', '.avi', '.mov', '.mkv','.srt', '.ssa', '.ass', '.sub']

files_and_dirs = os.listdir(path)
ova = re.compile(r'\[ova\]', re.IGNORECASE)
episode = re.compile(r'\[\d{2}\]')
pattern = re.compile(r'\](.{5,}?)\[(ova|OVA|\d{2}|\d{3})\]')

# 过滤出文件，排除目录
for fileName in files_and_dirs:
    dir = path+"/"+fileName

    #删除所有文件夹
    if(os.path.isdir(dir)):
        shutil.rmtree(dir)
        continue

    #删除所有繁体字幕
    if any(suffix in fileName.lower() for suffix in tcSubList):
        os.remove(dir)
        continue

    #删除所有不相关的文件
    if not fileName.lower().endswith(tuple(accepted_extensions)):
        os.remove(dir)
        continue

    match = pattern.search(fileName)
    if match:
        # 提取第一个捕获组的内容
        name = match.group(1).strip()
        episode = match.group(2).strip()

    parts = fileName.split('.')
    if len(parts) > 1:
        file_extension = '.' + parts[-1]
    else:
        file_extension = ''  # 文件没有扩展名

    if name and episode and file_extension:
        newName = name+" EP"+episode+file_extension
        newDir = path+"/"+newName
        os.rename(dir,newDir)
        print(newName)