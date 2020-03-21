#最終版 老師教的寫法，進行微調--->就用這個
code = 'a123456'
number = 3 #剩餘機會
while number > 0:
    number = number - 1 #每次問問題就減少一次機會
    pwd = input('請輸入密碼，最多輸入3次:')
    if code == pwd:
        print('密碼正確') #逃出迴圈
        break
    else:
        print('密碼錯誤!')
        if number > 0: #不要印出密碼錯誤還有0次
            print('還有', number,'次機會')