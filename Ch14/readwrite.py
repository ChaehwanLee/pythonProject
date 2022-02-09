def filewrite(name, content):
    try:
        f = open(name, 'wt');
        f.write(content);
    except:
        print('Error');
    finally:
        f.close();

def fileread(name):
    try:
        f = open(name,'rt');
        text = f.read();
    except:
        raise FileNotFoundError;
    finally:
        f.close();
    return text;

# 기능을 분리해서 사용용