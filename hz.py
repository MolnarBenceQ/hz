from random import choice,shuffle




def twlist(list_fagalom,list_meg):
    return  {fogalom: meghatarozas for fogalom, meghatarozas in zip(list_fagalom, list_meg)}


def firstTAskMain():
    fogalmak = ['majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized', 'kilenced', 'robot',
    'szügyhám', 'vetésforgó', 'ugar', 'lovag']
    meghatarozasok = ['Egy-egy nagybirtok vagy valamely részének igazgatásiközpontja.',

                    'Aki ör ökletes használatra megkapja a földet.',
                    'Telkes paraszt,aki aföldesúrtól kapott földön gazdálkodik.',
                    'Kiváltságos réteg.',
                    'Egyházi adó.',
                    'Földesúrnak beszolgáltatott adó.',
                    'Ötvenkét igás,vagy 104 kézimunka napkötelezettség.',
                    'Igavonási találmány,melynek köszönhetően nem az állat nyakábanvan a húzó eszköz.',
                    'A termőföld használata évszakonként más és más.',
                    'Művelés alánem vont terület.',
                    'Vagyonos katonai szolgálattevő lóval,páncéllal.']
    disk = twlist(list_fagalom=fogalmak, list_meg=meghatarozasok)

    rnd_fogalom = choice(list(disk.keys()))
    rnd_meghatarozas = disk[rnd_fogalom]
    print(f"ez a rnd elemet amit ki irunk  a terminálba --> {rnd_meghatarozas}")
    #--------------<>--------------#
    user_in_q = input("ird be ennekl a fagalmat! --> ").lower().strip()
    print(disk[user_in_q])
    print(user_in_q)
    file = open( "user_save_q.txt" ,"w")
    file.write(user_in_q)
    for i in shuffle(fogalmak):
        try: 
            if  disk[user_in_q] == disk[i]:
                print("ügyi vagy :) " )
                file.write("ügyi vagy :) ")
            else:
                print("nem vagy ügyi")
                file.write("nem vagy ügyi")
        except:
            print("nem létző key adtál meg :(")
            file.write("nem létző key adtál meg :(")
    file.close()
    #--------------<>--------------#

def second_task():
    pass




def harmas_task():
    data_list_string_format = """Név;Életkor;Város Németh Kamilla;19;Debrecen FeketeGéza;
    18;Pécs Kovács Péter;27;Budapest Kiss Tibor;20;Debrecen Szabó
    Erzsébet;21;Budapest Szilágyi Ede;18;Pécs Agárdi Pál;26;Budapest Pálosi
    Richárd;23;Budapest Budai Máté;19;Debrecen Karácsony Antal;20;Budapest Aradi
    Márta;27;Pécs Piros Adél;29;Debrecen Bíró Zsolt;16;Budapest Szabados
    Attila;25;Debrecen Román Sarolta;24;Budapest Virág Bertalan;22;Pécs Varga
    Imre;18;Budapest Tóth Sándor;22;Debrecen Nagy Ibolya;23;Pécs Horváth
    Ferenc;17;Budapest Balogh Edina;26;Budapest"""
     
    clean_list = [clean_list.split(";") for rec in data_list_string_format.split()]

