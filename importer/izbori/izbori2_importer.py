# coding=utf-8
from flask_pymongo import MongoClient
import cyrtranslit
from slugify import slugify
from tqdm import tqdm
import csv


# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo['datacentar']
collection = 'izbori2'
class Izbori2DataImporter(object):
    def get_political_parties(self, kandidat_name=None):
        data = []
        # year 2000
        # parlamentarni 2003
        data.append({
            'slug': "g17-plus",
            "name": "Г17 плус",
            "color": "#a6cee3"
        })
        data.append({
            'slug': "srs",
            "name": "СРС",
            "color": "#1f78b4"
        })
        data.append({
            'slug': "dss",
            "name": "ДСС",
            "color": "#b2df8a"
        })
        data.append({
            'slug': "da",
            "name": "ДА",
            "color": "#33a02c"
        })
        data.append({
            'slug': "ds",
            "name": "ДС",
            "color": "#fb9a99"
        })
        data.append({
            'slug': "spo-ns",
            "name": "СПО - НС",
            "color": "#e31a1c"
        })
        data.append({
            'slug': "otpor",
            "name": "Отпор",
            "color": "#fdbf6f"
        })

        data.append({
            'slug': "za-narodno-jedinstvo",
            "name": "За народно јединство",
            "color": "#ff7f00"
        })
        data.append({
            'slug': "sps",
            "name": "СПС",
            "color": "#cab2d6"
        })
        data.append({
            'slug': "samostalna-srbija",
            "name": "Самостална Србија",
            "color": "#6a3d9a"
        })

        data.append({
            'slug': 'odbrana-i-pravda',
            "name": "Одбрана и правда",
            "color": "#b15928"
        })
        data.append({
            'slug': "zajedno-za-toleranciju",
            "name": "Заједно за толеранцију",
            "color": "#8dd3c7"
        })
        data.append({
            'slug': "liberali-srbije",
            "name": "Либерали Србије",
            "color": "#bebada"
        })
        data.append({
            'slug': 'reformisti',
            "name": "Реформисти",
            "color": "#fb8072"
        })
        data.append({
            'slug': "sns",
            "name": "СНС",
            "color": "#80b1d3"
        })
        data.append({
            'slug': 'privredna-snaga-srbije-i-dijaspora',
            "name": "Привредна снага Србије и дијаспора",
            "color": "#fdb462"
        })
        data.append({
            'slug': "laburist-partija-srbije",
            "name": "Лабурист. партија Србије",
            "color": "#b3de69"
        })
        data.append({
            'slug': "savez-srba-vojvodine",
            "name": " Савез Срба Војводине",
            "color": "#bc80bd"
        })
        data.append({
            'slug': "jul",
            "name": " ЈУЛ",
            "color": "#8dd3c7"
        })
        #end of year 2003 parlamentarni

        #year 2007 parlamentarni
        #end of year 2007 parlamentarni

        #year 2008 parlamentarni
        data.append({
            'slug': "za-evropsku-srbiju-boris-tadic",
            "name": "ЗА ЕВРОПСКУ СРБИЈУ - БОРИС ТАДИЋ",
            "color": "#a6cee3"
        })
        data.append({
            'slug': "liberalno-demokratska-partija-cedomir-jovanovic",
            "name": 'ЛИБЕРАЛНО ДЕМОКРАТСКА ПАРТИЈА - ЧЕДОМИР ЈОВАНОВИЋ',
            "color": "#1f78b4"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-nova-srbija-vojislav-kostunica",
            "name": "Демократска странка Србије - Нова Србија - Војислав Коштуница",
            "color": "#b2df8a"
        })
        data.append({
            'slug': "srpska-radikalna-stranka-dr-vojislav-seselj",
            "name": "Српска радикална странка - др Војислав Шешељ",
            "color": "#33a02c"
        })
        data.append({
            'slug': "socijalisticka-partija-srbije-partija-ujedinjenih-penzionera-srbije-jedinstvena-srbija",
            "name": 'Социјалистичка партија Србије - Партија уједињених пензионера Србије - Јединствена Србија',
            "color": "#fb9a99"
        })
        data.append({
            'slug': "bosnjacka-lista-za-evropski-sandzak-dr-sulejman-ugljanin",
            "name": "БОШЊАЧКА ЛИСТА ЗА ЕВРОПСКИ САНЏАК - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "#e31a1c"
        })
        data.append({
            'slug': "madarska-koalicija-istvan-pastor",
            "name": 'МАЂАРСКА КОАЛИЦИЈА - ИШТВАН ПАСТОР',
            "color": "#fdbf6f"
        })

        data.append({
            'slug': "da-se-selo-pita-narodna-seljacka-stranka-marijan-risticevic",
            "name": 'ДА СЕ СЕЛО ПИТА - Народна сељачка странка - Маријан Ристичевић',
            "color": "#6a3d9a"
        })
        data.append({
            'slug': "pokret-snaga-srbije-bogoljub-karic",
            "name": 'Покрет СНАГА СРБИЈЕ - Богољуб Карић',
            "color": "#b15928"
        })
        data.append({
            'slug': "gradanska-inicijativa-goranaca-gig",
            "name": 'ГРАЂАНСКА ИНИЦИЈАТИВА ГОРАНАЦА - ГИГ',
            "color": "#8dd3c7"
        })

        data.append({
            'slug': "ujedinjeni-vlasi-srbije-dr-predrag-balasevic",
            "name": 'УЈЕДИЊЕНИ ВЛАСИ СРБИЈЕ - др Предраг Балашевић',
            "color": "#bebada"
        })
        data.append({
            'slug': "koalicija-vojvodanske-partije-mr-igor-kurjacki",
            "name": 'Коалиција \"Војвођанске партије\" - мр Игор Курјачки',
            "color": "#fb8072"
        })
        data.append({
            'slug': "romi-za-roma-milos-paunkovic",
            "name": 'РОМИ ЗА РОМА - МИЛОШ ПАУНКОВИЋ',
            "color": "#80b1d3"
        })

        data.append({
            'slug': "crnogorska-partija-nenad-stevovic",
            "name": 'Црногорска партија - Ненад Стевовић',
            "color": "#fdb462"
        })
        data.append({
            'slug': "unija-roma-srbije-dr-rajko-duric",
            "name": 'УНИЈА РОМА СРБИЈЕ - ДР РАЈКО ЂУРИЋ',
            "color": "#b3de69"
        })
        data.append({
            'slug': "koalicija-albanaca-presevske-doline",
            "name": 'КОАЛИЦИЈА АЛБАНАЦА ПРЕШЕВСКЕ ДОЛИНЕ',
            "color": "#bc80bd"
        })
        data.append({
            'slug': "savez-backih-bunjevaca-mirko-bajic",
            "name": 'САВЕЗ БАЧКИХ БУЊЕВАЦА - МИРКО БАЈИЋ',
            "color": "#a6cee3"
        })
        data.append({
            'slug': "pokret-moja-srbija-branislav-lecic",
            "name": 'Покрет Моја Србија - Бранислав Лечић',
            "color": "#1f78b4"
        })
        data.append({
            'slug': "narodni-pokret-za-srbiju-milan-paroski",
            "name": 'Народни покрет за Србију - Милан Парошки',
            "color": "#b2df8a"
        })
        data.append({
            'slug': "patriotska-snaga-dijaspore-zoran-milinkovic",
            "name": 'ПАТРИОТСКА СНАГА ДИЈАСПОРЕ - ЗОРАН МИЛИНКОВИЋ',
            "color": "#33a02c"
        })
        data.append({
            'slug': "romska-partija-srdan-sajn",
            "name": 'РОМСКА ПАРТИЈА - СРЂАН ШАЈН',
            "color": "#e31a1c"
        })
        #end of year 2008 parlamentarni
        #star the year parlamentarni 2012
        data.append({
            'slug': "izbor-za-bolji-zivot-boris-tadic",
            "name": "Избор за бољи живот - Борис Тадић",
            "color": "#a6cee3"
        })
        data.append({
            'slug': "ujedinjeni-regioni-srbije-mladan-dinkic",
            "name": "УЈЕДИЊЕНИ РЕГИОНИ СРБИЈЕ - МЛАЂАН ДИНКИЋ",
            "color": "#1f78b4"
        })
        data.append({
            'slug': "cedomir-jovanovic-preokret",
            "name": "Чедомир Јовановић - Преокрет",
            "color": "#b2df8a"
        })
        data.append({
            'slug': "pokrenimo-srbiju-tomislav-nikolic",
            "name": 'Покренимо Србију - Томислав Николић',
            "color": "#33a02c"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostunica",
            "name": "Демократска странка Србије - Војислав Коштуница",
            "color": "#fb9a99"
        })
        data.append({
            'slug': "ivica-dacic-socijalisticka-partija-srbije-sps-partija-ujedinjenih-penzionera-srbije-pups-jedinstvena-srbija-js",
            "name": 'Ивица Дачић - "Социјалистичка партија Србије (СПС), Партија уједињених пензионера Србије (ПУПС), Јединствена Србија (ЈС)"',
            "color": "#e31a1c"
        })
        data.append({
            'slug': "dveri-za-zivot-srbije",
            "name": 'Двери за живот Србије',
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "savez-vojodanskih-madara-istvan-pastor",
            "name": 'Савез војођанских Мађара - Иштван Пастор',
            "color": "#ff7f00"
        })
        data.append({
            'slug': "reformisticka-stranka-prof-dr-milan-visnjic",
            "name": 'Реформистичка странка - проф. др Милан Вишњић',
            "color": "#cab2d6"
        })
        data.append({
            'slug': "stranka-demokratske-akcije-sandzaka-dr-sulejman-ugljanin",
            "name": 'Странка демократске акције Санџака - др Сулејман Угљанин',
            "color": "#6a3d9a"
        })
        data.append({
            'slug': "pokret-radnika-i-seljaka",
            "name": "Покрет радника и сељака",
            "color": "#b15928"
        })
        data.append({
            'slug': "socijaldemokratski-savez-nebojsa-lekovic",
            "name": 'Социјалдемократски савез - Небојша Лековић',
            "color": "#8dd3c7"
        })
        data.append({
            'slug': "sve-zajedno-bdz-gsm-dzh-dzvm-slovacka-stranka-emir-elfic",
            "name": 'Све заједно: БДЗ, ГСМ, ДЗХ, ДЗВМ, Словачка странка - Емир Елфић',
            "color": "#bebada"
        })
        data.append({
            'slug': "koalicija-albanaca-presevske-doline",
            "name": 'КОАЛИЦИЈА АЛБАНАЦА ПРЕШЕВСКЕ ДОЛИНЕ',
            "color": "#fb8072"
        })
        data.append({
            'slug': "komunisticka-partija-josip-broz",
            "name": "Комунистичка партија - Јосип Броз",
            "color": "#80b1d3"
        })
        data.append({
            'slug': "nijedan-od-ponudenih-odgovora",
            "name": 'Ниједан од понуђених одговора',
            "color": "#fdb462"
        })
        #end of year 2012

        #parlamentarni 2014
        data.append({
            'slug': "aleksandar-vucic-sns-sdps-ns-spo-ps",
            "name": "АЛЕКСАНДАР ВУЧИЋ - СНС, СДПС, НС, СПО, ПС",
            "color": "#a6cee3"
        })
        data.append({
            'slug': "ivica-dacic-sps-pups-js",
            "name": 'ИВИЦА ДАЧИЋ - СПС, ПУПС, ЈС',
            "color": "#1f78b4"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostinica",
            "name": 'ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА',
            "color": "#b2df8a"
        })
        data.append({
            'slug': "cedomir-jovanovic-ldp-bdzs-sdu",
            "name": 'ЧЕДОМИР ЈОВАНОВИЋ - ЛДП, БДЗС, СДУ',
            "color": "#33a02c"
        })
        data.append({
            'slug': "savez-vojvodanskih-madara-istvan-pastor",
            "name": "САВЕЗ ВОЈВОЂАНСКИХ МАЂАРА - ИШТВАН ПАСТОР",
            "color": "#fb9a99"
        })
        data.append({
            'slug': "sa-demokratskom-strankom-za-demokratsku-srbiju",
            "name": "СА ДЕМОКРАТСКОМ СТРАНКОМ ЗА ДЕМОКРАТСКУ СРБИЈУ",
            "color": "#e31a1c"
        })
        data.append({
            'slug': "dveri-bosko-obradovic",
            "name": "ДВЕРИ - БОШКО ОБРАДОВИЋ",
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "sda-sandzaka-dr-sulejman-ugljanin",
            "name": "СДА САНЏАКА - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "#ff7f00"
        })
        data.append({
            'slug': "boris-tadic-nds-lsv-zzs-vmdk-zzv-dlr",
            "name": "БОРИС ТАДИЋ - НДС, ЛСВ, ЗЗС, ВМДК, ЗЗВ, ДЛР",
            "color": "#cab2d6"
        })
        data.append({
            'slug': "treca-srbija-za-sve-vredne-ljude",
            "name": "ТРЕЋА СРБИЈА - ЗА СВЕ ВРЕДНЕ ЉУДЕ",
            "color": "#6a3d9a"
        })
        data.append({
            'slug': "crnogorska-partija-josip-broz",
            "name": "ЦРНОГОРСКА ПАРТИЈА - ЈОСИП БРОЗ",
            "color": "#b15928"
        })
        data.append({
            'slug': "crnogorska-partija-josip-broz",
            "name": "ЦРНОГОРСКА ПАРТИЈА - ЈОСИП БРОЗ",
            "color": "#8dd3c7"
        })
        data.append({
            'slug': "lista-nacionalnih-zajednica-emir-elfic",
            "name": "ЛИСТА НАЦИОНАЛНИХ ЗАЈЕДНИЦА - ЕМИР ЕЛФИЋ",
            "color": "#bebada"
        })
        data.append({
            'slug': "dosta-je-bilo-sasa-radulovic",
            "name": "ДОСТА ЈЕ БИЛО - САША РАДУЛОВИЋ",
            "color": "#fb8072"
        })
        data.append({
            'slug': "koalicija-gradana-svih-naroda-i-narodnosti",
            "name": "КОАЛИЦИЈА ГРАЂАНА СВИХ НАРОДА И НАРОДНОСТИ",
            "color": "#80b1d3"
        })
        data.append({
            'slug': "grupa-gradana-patriotski-front",
            "name": 'ГРУПА ГРАЂАНА \"ПАТРИОТСКИ ФРОНТ\"',
            "color": "#fdb462"
        })
        data.append({
            'slug': "ruska-stranka-slobodan-nikolic",
            "name": "РУСКА СТРАНКА - СЛОБОДАН НИКОЛИЋ",
            "color": "#b3de69"
        })
        data.append({
            'slug': "partija-za-demokratsko-delovanje-riza-halimi",
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ - РИЗА ХАЛИМИ",
            "color": "#bc80bd"
        })
        #end of parlamentarni 2014
        #presidential 2002
        data.append({
            'slug': "vuk-draskovic-spo",
            "name": "Вук Драшковић (СПО)",
            "color": "#a6cee3"
        })
        data.append({
            'slug': "velimir-bata-zivojinovic-sps",
            "name": "Велимир-Бата Живојиновић (СПС)",
            "color": "#1f78b4"
        })
        data.append({
            'slug': "prof-dr-branislav-bane-ivkovic-gg",
            "name": "проф. др Бранислав-Бане Ивковић (ГГ)",
            "color": "#b2df8a"
        })
        data.append({
            'slug': "vojislav-kostunica-dss",
            "name": "Војислав Коштуница (ДСС)",
            "color": "#33a02c"
        })
        data.append({
            'slug': "dr-miroljub-labus-gg",
            "name": "др Мирољуб Лабус      (ГГ) ",
            "color": "#fb9a99"
        })
        data.append({
            'slug': "dr-tomislav-lalosevic-gg",
            "name": "др Томислав Лалошевић (ГГ)",
            "color": "#e31a1c"
        })
        data.append({
            'slug': "dr-vuk-obradovic-sd",
            "name": "др Вук Обрадовић  (СД)",
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "nebojsa-pavkovic-gg",
            "name": "Небојша Павковић  (ГГ)",
            "color": "#ff7f00"
        })
        data.append({
            'slug': "prof-borislav-pelevic-ssj",
            "name": "проф. Борислав  Пелевић  (ССЈ)",
            "color": "#6a3d9a"
        })
        data.append({
            'slug': "dr-dragan-radenovic-gg",
            "name": "др Драган Раденовић (ГГ)",
            "color": "#b15928"
        })
        data.append({
            'slug': "dr-vojislav-seselj-srs",
            "name": "др Војислав Шешељ (СРС)",
            "color": "#8dd3c7"
        })
        #end of presidential 2002

        # 2003 presidential
        data.append({
            'slug': "radoslav-avlijas-dso",
            "name": 'Радослав Авлијаш (ДСО)',
            "color": "#ffffcc"
        })
        data.append({
            'slug': "velimir-ilic-ns",
            "name": 'Велимир Илић (НС)',
            "color": "#41b6c4"
        })
        data.append({
            'slug': "prof-dr-dragoljub-micunovic-dos",
            "name": 'Проф. др Драгољуб Мићуновић (ДОС)',
            "color": "#2c7fb8"
        })
        data.append({
            'slug': "tomislav-nikolic-srs",
            "name": 'Томислав Николић (СРС)',
            "color": "#253494"
        })
        data.append({
            'slug': "marijan-risticevic-nss",
            "name": 'Маријан Ристичевић (НСС)',
            "color": "#7fcdbb"
        })
        data.append({
            'slug': "dragan-s-tomic-sns",
            "name": 'Драган С. Томић (СНС)',
            "color": "#c7e9b4"
        })
        #end of presidential 2003
        #presidential 2008
        data.append({
            'slug': "tomislav-nikolic",
            "name": 'Томислав Николић',
            "color": "#a6cee3"
        })
        data.append({
            'slug': "jugoslav-dobri-canin",
            "name": 'Југослав Добри-чанин',
            "color": "#1f78b4"
        })
        data.append({
            'slug': "boris-tadic",
            "name": 'Борис Тадић',
            "color": "#b2df8a"
        })
        data.append({
            'slug': "velimir-ilic",
            "name": 'Велимир Илић',
            "color": "#33a02c"
        })
        data.append({
            'slug': "istvan-pastor",
            "name": 'Иштван Пастор',
            "color": "#fb9a99"
        })
        data.append({
            'slug': "marijan-risti-cevic",
            "name": 'Маријан Ристи-чевић',
            "color": "#e31a1c"
        })
        data.append({
            'slug': "cedomir-jova-novic",
            "name": 'Чедомир Јова-новић',
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "milanka-karic",
            "name": 'Миланка Карић',
            "color": "#ff7f00"
        })
        #end of presidential 2008
        #presidential 2012
        data.append({
            'slug': "boris-tadic",
            "name": 'Борис Тадић',
            "color": "#a6cee3"
        })
        data.append({
            'slug': "tomislav-nikolic",
            "name": 'Томислав Николић',
            "color": "#1f78b4"
        })
        data.append({
            'slug': "prof-dr-zoran-stankovic",
            "name": 'проф. др  Зоран Станковић',
            "color": "#b2df8a"
        })
        data.append({
            'slug': "vladan-glisic",
            "name": 'Владан Глишић',
            "color": "#33a02c"
        })
        data.append({
            'slug': "prof-dr-zoran-dragisic",
            "name": 'проф. др Зоран Драгишић',
            "color": "#fb9a99"
        })
        data.append({
            'slug': "jadranka-seselj",
            "name": 'Јадранка Шешељ',
            "color": "#e31a1c"
        })
        data.append({
            'slug': "muamer-zukorlic",
            "name": 'Муамер Зукорлић',
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "danica-grujicic",
            "name": 'Даница Грујичић',
            "color": "#ff7f00"
        })
        data.append({
            'slug': "ivica-dacic",
            "name": 'Ивица Дачић',
            "color": "#6a3d9a"
        })
        data.append({
            'slug': "cedomir-jovanovic",
            "name": 'Чедомир Јовановић',
            "color": "#b15928"
        })
        data.append({
            'slug': "istvan-pastor",
            "name": 'Иштван Пастор',
            "color": "#8dd3c7"
        })
        data.append({
            'slug': "tomislav-nikolic",
            "name": 'Томислав Николић',
            "color": "#bebada"
        })
        #end of presidential 2012
        data.append({
            'slug': "bosnjacka-lista-za-evropski-sandzak-dr-sulejman-ugljanin",
            "name": 'БОШЊАЧКА ЛИСТА ЗА ЕВРОПСКИ САНЏАК - ДР СУЛЕЈМАН УГЉАНИН',
            "color": "#fdbf6f"
        })
        data.append({
            'slug': "pokret-snaga-srbije-bogoljub-karic",
            "name": 'Покрет СНАГА СРБИЈЕ - Богољуб Карић',
            "color": "#ff7f00"
        })

        if kandidat_name is not None:
            jsondata = {}
            selected_color = ""
            for name in data:
                if kandidat_name == name['name']:
                    jsondata = {'color': name['color'], 'slug': name['slug'], 'name': name['name']}

            return jsondata
        else:

            return data

    def import_data(self, election_type, year, month=None, rnd=None):
        if election_type == 'parlamentarni' and int(year) == 2016:
            self.import_data_parliament_2016()
        elif election_type == 'parlamentarni' and int(year) == 2008:
            self.import_data_parliament_2008()
        elif election_type == 'parlamentarni' and int(year) == 2007:
            self.import_data_parliament_2007()
        else:
            self.import_data_rest(election_type, year, month, rnd)

    def import_data_parliament_2007(self):
        election_type = 'parlamentarni'
        year = 2007
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in range(12, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '')
                else:
                    territory = row[2].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[3].strip())
                    polling_station_address = row[4].strip()
                    ballots_received_count = int(row[5].strip())
                    unused_ballots_count = int(row[6].strip())
                    number_of_voters_registered=int(row[7].strip())
                    voters_who_voted_count = int(row[8].strip())
                    ballots_in_ballot_box_count = int(row[9].strip())
                    invalid_ballots_count = int(row[10].strip())
                    valid_ballots_count = int(row[11].strip())


                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(12, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print ""
                        else:

                            doc['boja'] = boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_parliament_2008(self):
        election_type = 'parlamentarni'
        year = 2008
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in xrange(10, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()


                elif row_count == 1:
                    pass

                else:
                    territory = row[0].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                    polling_station_address = row[2].strip()
                    ballots_received_count = int(row[3].strip())
                    unused_ballots_count = int(row[4].strip())
                    number_of_voters_registered=int(row[5].strip())
                    ballots_in_ballot_box_count = int(row[6].strip())
                    invalid_ballots_count = int(row[7].strip())
                    valid_ballots_count = int(row[8].strip())
                    voters_who_voted_count=int(row[9].strip())

                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(10, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])

                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print ""
                        else:

                            doc['boja']=boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)


    def import_data_parliament_2016(self):
        election_type = 'parlamentarni'
        year = 2016
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in xrange(10, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()


                elif row_count == 1:
                    pass

                else:
                    territory = row[0].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                    polling_station_address = row[2].strip()
                    ballots_received_count = int(row[3].strip())
                    unused_ballots_count = int(row[4].strip())
                    number_of_voters_registered = int(row[5].strip())
                    ballots_in_ballot_box_count = int(row[6].strip())
                    invalid_ballots_count = int(row[7].strip())
                    valid_ballots_count = int(row[8].strip())
                    voters_who_voted_count = int(row[9].strip())

                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica'] = unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici'] = invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes = 0
                    udeo = 0

                    for j in range(10, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])

                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print ""
                        else:

                            doc['boja'] = boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_parliament_2016(self):
        election_type = 'parlamentarni'
        year = 2016
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in xrange(10, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                elif row_count == 1:
                    pass

                else:

                    territory = row[0].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                    polling_station_address = row[2].strip()
                    number_of_voters_registered = int(row[3].strip())
                    ballots_received_count = int(row[4].strip())
                    unused_ballots_count = int(row[5].strip())
                    voters_who_voted_count = int(row[6].strip())
                    ballots_in_ballot_box_count = int(row[7].strip())
                    invalid_ballots_count = int(row[8].strip())
                    valid_ballots_count = int(row[9].strip())


                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica'] = unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici'] = invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes = 0
                    udeo = 0
                    for j in range(10, len(row)):


                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])

                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print ""
                        else:

                            doc['boja'] = boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_rest(self, election_type, year, month=None, rnd=None):

        self.prep_import(election_type, year, month, rnd)

        file_path = self.get_data_file_path(election_type, year, month, rnd)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:

                    if int(year) == 2004 and election_type == "predsjednicki":

                        for i in xrange(11, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2008 and election_type == "predsjednicki":
                        for i in xrange(8, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2003 and election_type in ["predsjednicki", "parlamentarni"]:
                        for i in xrange(6, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        for i in xrange(6, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    else:
                        for i in xrange(13, len(row), 2):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                elif row_count == 1:
                    print "1"
                    pass

                else:
                    if int(year)==2004 and election_type=="predsjednicki":
                        territory = row[1].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[2].strip())
                        polling_station_address = row[3].strip()
                        ballots_received_count = int(row[4].strip())
                        unused_ballots_count = int(row[5].strip())
                        registered_voters_count = int(row[6].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        valid_ballots_count = int(row[10].strip())

                    else:

                        territory = row[0].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                        polling_station_address = row[2].strip()

                        registered_voters_count = int(row[3].strip())

                    if int(year) == 2012 and election_type == "predsjednicki":
                        print row_count
                        print float(row[10].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    if int(year) == 2012 and election_type == "parlamentarni":
                        voters_who_voted_count = int(row[4].strip())
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count=int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    if int(year)==2008 and election_type=="predsjednicki":
                        voters_who_voted_count = int(row[6].strip())
                        voters_who_voted_percent=float(row[7].strip())

                    if int(year) not in [2008, 2012]  and election_type != "predsjednicki":
                        voters_who_voted_count = int(row[4].strip())

                    if int(year) == 2003 and election_type in["predsjednicki","parlamentarni"]:
                        voters_who_voted_count = int(row[4].strip())
                        total_voter_turn_out = float(row[5].strip())
                    if int(year) == 2002 and election_type == "predsjednicki":
                        voters_who_voted_count = int(row[4].strip())
                        total_voter_turn_out = float(row[5].strip())


                    if int(year) not in [2002, 2003,2004] and election_type not in ["predsjednicki"]:
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    doc['brojUpisanihBiracaUBirackiSpisak'] = registered_voters_count
                    doc['biraciKojiSuGlasali'] = {}

                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count

                    if int(year) in [2002, 2003] and election_type in ["predsjednicki", "parlamentarni"]:
                        doc['odzivBiraca']=total_voter_turn_out

                    if int(year) not in [2002, 2003] and election_type not in ["predsjednicki", "parlamentarni"]:

                        doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                        doc['brojPrimljenihGlasackihListica'] = ballots_received_count
                        doc['brojNeupoTrebljenihGlasackihListica'] = unused_ballots_count
                        if int(year) not in [2012, 2004] and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji'] = ballots_in_ballot_box_count
                        doc['brojGlasackihListicaUKutiji'] = {}
                        doc['brojGlasackihListicaUKutiji']['broj'] = invalid_ballots_count
                        if int(year)!=2004 and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji']['udeo'] = invalid_ballots_percent
                        doc['vazeciGlasackiListici'] = {}
                        doc['vazeciGlasackiListici']['broj'] = valid_ballots_count
                        if int(year) != 2004 and election_type != "predsjednicki":
                            doc['vazeciGlasackiListici']['udeo'] = valid_ballots_percent
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug\
                            or territory_slug in ['grad-beograd', 'inostranstvo']\
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)

                    elif polling_station_num is not '':

                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address

                    if int(year)==2003 and election_type in ["parlamentarni"]:
                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])


                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0

                            doc['rezultat']['udeo'] =udeo
                            doc['izbornaLista'] = candidates_or_parties[str(j)]
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)
                            if not boja:
                                print ""
                            else:

                                doc['boja'] = boja['color']
                            doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}


                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:

                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)
                            if not boja:
                                print ""
                            else:

                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                              to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2003 and election_type == "predsjednicki":

                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}


                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:

                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)

                            if not boja:
                                print ""
                            else:

                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                              to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                    elif int(year) == 2004 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(11, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}

                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)

                            if not boja:
                                print ""
                            else:

                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2008 and election_type == "predsjednicki":
                        total_votes = 0
                        udeo = 0
                        for j in xrange(8, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}

                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)

                            if not boja:
                                print ""
                            else:

                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                    else:

                        total_votes=0
                        udeo=0
                        for j in xrange(13, len(row), 2):
                            # Set generic values
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election
                            if election_type == 'predsjednicki':
                                month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                                rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                                doc['mesec'] = month_cyr
                                doc['krug'] = rnd_cyr
                                doc['kandidat'] = candidates_or_parties[str(j)].title()
                                ime = candidates_or_parties[str(j)]
                                boja = self.get_political_parties(ime)

                                if not boja:
                                    print ""
                                else:

                                    doc['boja'] = boja['color']
                                doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            else:
                                ime = candidates_or_parties[str(j)]
                                boja = self.get_political_parties(ime)

                                if not boja:
                                    print ""
                                else:

                                    doc['boja'] = boja['color']
                                doc['izbornaLista'] = candidates_or_parties[str(j)]
                                doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:

            db[collection].insert(docs)


    def prep_import(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            print '\nRemoving previously imported data for %s %s %s %s...' % (election_type, year, month, rnd)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year),
                'mesec': cyrtranslit.to_cyrillic(month.title(), 'sr'),
                'krug': cyrtranslit.to_cyrillic(rnd.title(), 'sr')
            })

            print 'Importing data for %s %s %s %s...' % (election_type, year, month, rnd)

        else:
            print '\nRemoving previously imported data for %s %s...' % (election_type, year)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year)
            })

            print 'Importing data for %s %s...' % (election_type, year)

    def get_data_file_path(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            return "data/izbori2/%s/%s-%s-%s.csv" % (election_type, year, month, rnd)
        else:
            return "data/izbori2/%s/%s.csv" % (election_type, year)
