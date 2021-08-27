def class_name_changer(MyClass, name):
    MyClass.__name__ = name
    if name[0].isupper() == False or ' ' in name or '!' in name: raise Exception('error')