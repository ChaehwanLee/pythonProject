def filewrite(name, content):
    try:
        f = open(name, 'wt');
        f.write(content);
    except:
        print('Error');
    finally:
        f.close();

