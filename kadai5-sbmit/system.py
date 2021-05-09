from menu import Menu
import pandas as pd
from datetime import  datetime
import eel

@eel.expose
def system(csv_name,order,count,amount):

    try:
        # 課題３（発展版）
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        eel.disp('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        df = pd.read_csv('{}'.format(csv_name))
        codes = df['code'].tolist()
        names = df['name'].tolist()
        prices = df['price'].tolist()

        menu_items = []
        for code,name,price in zip(codes,names,prices):
            menu_item = Menu(code,name,price)
            menu_items.append(menu_item)

        for item in menu_items:
            print(item.menu_disp())
            eel.disp(item.menu_disp())

        print('***************************************')
        eel.disp('***************************************')

        # order = int(input('メニューの商品番号を入力してください: '))
        selected_menu = menu_items[int(order)]
        print('選択されたメニュー: ' + selected_menu.name)
        eel.disp('選択されたメニュー: ' + selected_menu.name)

        print('***************************************')
        eel.disp('***************************************')
        # count = int(input('個数を入力してください: '))
        result = selected_menu.get_total(int(count))
        print('注文内容は、\n選択された商品：' + selected_menu.name + '\n' + '個数：' + str(count) + '\n' + '合計金額：' + str(result) + '円\nです。')
        eel.disp('注文内容は、\n選択された商品：' + selected_menu.name + '\n' + '個数：' + str(count) + '\n' + '合計金額：' + str(result) + '円\nです。')

        print('***************************************')
        eel.disp('***************************************')
        # amount = int(input('お預かり金額を入力してください: '))
        # 課題４（発展版）お預かり金額が合計金額より不足する時の対応を追加
        change = int(amount) - result
        if change >= 0:
            print('お預かり金額は' + str(amount) + '円です。\nお釣りは、' + str(change) + '円です。')
            eel.disp('お預かり金額は' + str(amount) + '円です。\nお釣りは、' + str(change) + '円です。')
            now = datetime.now()
            with open('{}.txt'.format(now),'w') as f:
                f.write('注文内容\n商品：' + selected_menu.name + '\n' + '個数：' + str(count) + '\n' + '合計金額：' + str(result) + '円\nお預かり金額：' + str(amount) + '円\nお釣り：' + str(change) + '円')
                print('レシート（ファイル:{}.txt）を確認してください。'.format(now))
                eel.disp('レシート（ファイル:{}.txt）を確認してください。'.format(now))
        else:
            shortage = result - int(amount)
            print('お預かり金額は' + str(amount) + '円です。\n不足金額は、' + str(shortage) + '円です。')
            eel.disp('お預かり金額は' + str(amount) + '円です。\n不足金額は、' + str(shortage) + '円です。')
       
    except:
        print('入力内容が間違っています。最初からやり直してください。')
        eel.disp('入力内容が間違っています。最初からやり直してください。')

eel.init("html")
eel.start("index.html")

