##f = open("st.txt","r")
##print(f.read())
##f.close()


##answer = input("好きな歌手は？：")
##with open("fav_singer.txt","w",encoding="utf-8") as f:
##    f.write(answer)


##import csv
##movies =[["Top Gun","Tisky Business","Minority Teport"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
##with open("movie.csv","w") as f:
##    w = csv.writer(f,delimiter=",")
##    for movie in movies:
##        w.writerow(movie)
##
##with open("movie.csv","r") as f:
##    print(f.read())



import csv
movies =[["トップガン","リスキービジネス","マイノリティレポート"],["タイタニック","ザレヴナント","インセプション"],["トレーニングデイ","マンオブザイヤー","ファイト"]]
with open("movie.csv","w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for movie in movies:
        w.writerow(movie)

with open("movie.csv","r",encoding="utf-8") as f:
    print(f.read())
