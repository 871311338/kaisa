def kaisajiami(a, b):
 
    xiaoxie = 'abcdefghijklmnopqrstuvwxyz'
 
    daxie = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    jiami = xiaoxie[b:] + xiaoxie[:b] + daxie[b:] + daxie[:b]
 
    yingshe1 = ''.maketrans(all, jiami)
 
    return a.translate(yingshe1)

def kaisajiemi(c,d):

    xiaoxie = 'abcdefghijklmnopqrstuvwxyz'
 
    daxie = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    jiemi = xiaoxie[26-d:] + xiaoxie[:26-d] + daxie[26-d:] +daxie[:26-d]

    yingshe2 = ''.maketrans(all,jiemi)

    return c.translate(yingshe2)
 
a = input('请输入待加密字母:')
 
b = int(input('请输入加密偏移量:'))

c = input('请输入待解密字母:')

d = int(input('请输入解密偏移量:'))
 
print(kaisajiami(a,b))

print(kaisajiemi(c,d))
