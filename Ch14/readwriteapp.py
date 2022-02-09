import readwrite;

def start():
    name = input('Input File Name...?');
    content = input('Write Contents..:');
    readwrite.filewrite(name,content);

# 마우스로 아이콘을 클릭했을 때, 휴대폰으로 앱을 눌렀을 때

if __name__ == '__main__':
    start();