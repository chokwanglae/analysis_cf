import urllib
from itertools import count
from bs4 import BeautifulSoup
import pandas  as pd
import collection.crawler as cw
import xml.etree.ElementTree as et
from collection.data_dict import sido_dict ,gungu_dict

RESULT_DIRECTORY ='__result__/crawling'
def crawling_pelicana():
    results = []
    for page in count(start=1):
        url = 'http://www.pelicana.co.kr/store/stroe_search.html?gu=&si=&page=%d' % page
        html = cw.crawling(url=url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)

            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))
    #store
    table = pd.DataFrame(results, columns=['name', 'address','sido','gungu'])

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    #proc
    #print(results)


def proc_nene(xml):
    root = et.fromstring(xml)
    results=[]

    for el in root.findall('item'):
        name = el.findtext('aname1')
        sido = el.findtext('aname2')
        gungu = el.findtext('aname3')
        address = el.findtext('anmame5')

        results.append((name,address,sido,gungu))
    return results

def store_nene(data):

    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),
                 encoding='utf-8',
                 mode='w',
                 index=True)
    bs = BeautifulSoup(html, 'html.parser')
    tag_table = bs.find('table', attrs={'class': 'table mt20'})
    tag_tbody = tag_table.find('tbody')
    tags_tr = tag_tbody.findAll('tr')

#    pass

    '''
    cw.crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s ' % (urllib.parse.quote("전체"),urllib.parse.quote( "전체")),
        proc=proc_nene,
        store=store_nene

    )
    '''

    #kyochon

 def crawling_kyochon(data):
    results = []
    for page in count(start=1):
        url = 'http://www.kyochon.com/shop/domestic.asp?sido1=0&sido2=0&txtsearch=%' % page
        html = cw.crawling(url=url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')
    if len(tags_tr) == 0:
        continue

     for sido1 in range(1,18):
         for sido2 in count(start=1):
             if condition :
                 break


        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)

    # table = pd.DataFrame(, columns=['name','sido', 'gungu','address' ])

    # table.to_csv('{0}/kyochon_table.csv'.format(),
    #              encoding='utf=8',
    #              mode='w',
    #              index=True)
    #
    # cw.crawling(
    #     url =
    # )

if __name__ == '__main__':
    #pelicana
    #crawling_pelicana()

    #nene
    kyochon









