#ver1 寫法一 我自己想的
code = 'a123456'
number = 3 #剩餘機會
while number >= 1:
    pwd = input('請輸入密碼，最多輸入3次:')
    if code == pwd:
        print('密碼正確') #逃出迴圈
        break
    else:
        number = number - 1
        print('密碼錯誤! 還有', number,'次機會')


#ver2 寫法二 老師教的寫法
code = 'a123456'
number = 3 #剩餘機會
while True:
    pwd = input('請輸入密碼，最多輸入3次:')
    if code == pwd:
        print('密碼正確') #逃出迴圈
        break
    else:
        number = number - 1
        print('密碼錯誤! 還有', number,'次機會')
        if number = 0:
            break

#ver2 寫法三 老師教的寫法，當不能使用while True的時候怎麼辦
code = 'a123456'
number = 3 #剩餘機會
while number > 0:
    pwd = input('請輸入密碼，最多輸入3次:')
    if code == pwd:
        print('密碼正確') #逃出迴圈
        break
    else:
        number = number - 1
        print('密碼錯誤! 還有', number,'次機會')
