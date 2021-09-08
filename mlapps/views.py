from django.shortcuts import render

def entrance(request):
    return render(request, 'mlapps/entrance.html', {})

questions = {'questions' : {
        'あなたの性別は何ですか？(0. 男性, 1. 女性)'
        ,'あなたは文系ですか？理系ですか？(0. 文系, 1. 理系)'
        ,'あなたの卒業した高校の入学当時の偏差値はおよそいくつでしたか？(0. ~29, 1. 30~39, 2. 40~49, 3. 50~59, 4. 60~69, 5. 70~)'
        ,'あなたは高校時代に何か部活に加入していましたか？(0. 運動部, 1. 文化部, 2. その他(加入していない含む))'
        ,'あなたは大学進学という進路選択について、明確な目的意識がありましたか？(0. はい, 1. いいえ)'
        ,'あなたはファッションに興味がありますか？(0. はい, 1. いいえ)'
        ,'あなたは周りと合わせるよりも自分の道を突き通す方ですか？(0. はい, 1. いいえ)'
        ,'あなたは音楽を聴きながら勉強していましたか？(0. はい, 1. いいえ)'
        ,'あなたは塾・予備校(またはそれに準ずるサービス等)を利用していましたか？(0. はい, 1. いいえ)'
        ,'あなたは青学合格年度の夏に一日平均どの程度勉強していましたか？(0. 0~2時間, 1. 2~4時間, 2. 4~6時間, 3. 6~8時間, 4. 8~10時間, 5. 10時間以上)'
        ,'あなたは青学合格年度に一日平均どの程度睡眠をとっていましたか？(0. ~5時間, 1. 6~7時間, 2. 8~時間)'
        ,'あなたは受験期にスマホやテレビ等の使用制限をかけていましたか？(0. はい, 1. いいえ)'
        ,'あなたが使用していた付箋の色の数はいくつでしたか？(0. 0色(付箋は使用していない), 1. 1色, 2. 2色, 3. 3色, 4. 4色以上)'
        ,'あなたが使用していたボールペン(蛍光ペン)の色の数はいくつでしたか？(0. 0色(ボールペンは使用していない), 1. 1色, 2. 2色, 3. 3色, 4. 4色以上)'
        ,'第一志望大学群はどこでしたか？(0. 最難関国公立(東京一工)・早慶, 1. 難関国公立(金岡千広等)・上智理科大, 2. 準難関国公立(5S等)・MARCH, 3. 標準国立(stars等)・日東駒専, 4. その他)'
        ,'あなたは青学を第何志望校として設定していましたか？(0. 第一志望校, 1. 第二志望校, 2. 第三志望校, 3. その他(第四志望校以下))'
        ,'夏に何らかの模試を受けましたか？(0. 河合模試, 1. 駿台模試, 2. 東進模試, 3. 代々木模試, 4. 進研模試, 5. 複数受験した, 6. その他(受けていない含む))'
        ,'[最重要]ハトは"良い"ですか？(0. はい, 1. いいえ, 810. ｵﾊｰﾄ🐦)'
}}
bayes_columns =['あなたの性別は何ですか？', 'あなたは文系ですか？理系ですか？', 'あなたは高校時代に何か部活に加入していましたか？', 'あなたは大学進学という進路選択について、明確な目的意識がありましたか？', 'あなたはファッションに興味がありますか？', 'あなたは周りと合わせるよりも自分の道を突き通す方ですか？', 'あなたは音楽を聴きながら勉強していましたか？', 'あなたは塾・予備校(またはそれに準ずるサービス等)を利用していましたか？', 'あなたは青学合格年度に一日平均どの程度睡眠をとっていましたか？', 'あなたは受験期にスマホやテレビ等の使用制限をかけていましたか？', '第一志望大学群はどこでしたか？']
lr_columns = ['あなたは大学進学という進路選択について、明確な目的意識がありましたか？', 'あなたはファッションに興味がありますか？', 'あなたは周りと合わせるよりも自分の道を突き通す方ですか？', 'あなたは音楽を聴きながら勉強していましたか？', 'あなたは塾・予備校(またはそれに準ずるサービス等)を利用していましたか？', 'あなたは受験期にスマホやテレビ等の使用制限をかけていましたか？', '第一志望大学群はどこでしたか？']
svm_columns = ['あなたはファッションに興味がありますか？']
prediction = {
    0.:'A',
    1.:'B',
    2.:'C',
    3.:'D',
    4.:'E'
}
#ques = {'lists':[i for i in range(18)]}

def score(request):
    if request.method == 'GET':
        return render(request, 'mlapps/score.html', {'questions':questions})
    else:
        try:
            df = pd.DataFrame({
                'あなたの性別は何ですか？':judge0
                ,'あなたは文系ですか？理系ですか？':judge1
                ,'あなたの卒業した高校の入学当時の偏差値はおよそいくつでしたか？':judge2
                ,'あなたは高校時代に何か部活に加入していましたか？':judge3
                ,'あなたは大学進学という進路選択について、明確な目的意識がありましたか？':judge4
                ,'あなたはファッションに興味がありますか？':judge5
                ,'あなたは周りと合わせるよりも自分の道を突き通す方ですか？':judge6
                ,'あなたは音楽を聴きながら勉強していましたか？':judge7
                ,'あなたは塾・予備校(またはそれに準ずるサービス等)を利用していましたか？':judge8
                ,'あなたは青学合格年度の夏に一日平均どの程度勉強していましたか？':judge9
                ,'あなたは青学合格年度に一日平均どの程度睡眠をとっていましたか？':judge10
                ,'あなたは受験期にスマホやテレビ等の使用制限をかけていましたか？':judge11
                ,'あなたが使用していた付箋の色の数はいくつでしたか？':judge12
                ,'あなたが使用していたボールペン(蛍光ペン)の色の数はいくつでしたか？':judge13
                ,'第一志望大学群はどこでしたか？':judge14
                ,'あなたは青学を第何志望校として設定していましたか？':judge15
                ,'夏に何らかの模試を受けましたか？':judge16
                ,'[最重要]ハトは"良い"ですか？':judge17
            })

            return render(request, 'mlapps/score.html',
            {
                'judge0':judge0,
                'judge1':judge1,
            })
        except:
            return render(request, 'mlapps/score.html', {'questions':questions})

def rent(request):
    return render(request, 'mlapps/rent.html', {})

def travel(request):
    return render(request, 'mlapps/travel.html', {})