import csv
import pandas as pd
from pandas import ExcelWriter
import numpy as np

df = pd.read_csv('BookUpdate13July2018.csv')

filter_word = ['xxxx','jjjjj','xxx','ไดรฟ์ฮับ','','ทดสอบ','testx',
                'drivehub','คับ','test','testing','test','ลุงคิดละ',
                'x','reserve','tester','test003','test02','test004',
                'tesing for top carrent','ex','noo','joy','pattaya',
                'lg','รับด่วน ที่ส่ง 2 คัน','X จอง','gade','เช่ารายเดือน','LINE@',
                'พี่บี','โอเค','จองให้ลูกค้า','V.','เอ็กจองให้','ลค มาทาง line',
                'dfsdfsdf','sdfgsdfsdf','ลุกค้าLine@','จองด่วน','จองผ่าน call center',
                'ลูกค้าจองผ่าน Call Center','Admin by PX','จองแทนลูกค้า','แทรคเตอร์จองแทน',
                'ลูกค้าคนจีน','จองผ่าน Callcenter',"Admin by P'X",'vv','fsssssss',
                'ลูกค้า','25 วัน','ส้ม','ทดสอบ','TT','t','I','nui','cc',
                'พพ','พพพ','drivehubtestCPA','จองเอง2','n','nin',
                'ไลน์ @','จองผ่าน Call','คุณเอก','ผ่านทาง call center','Cnv',
                'iOS','max','dh','hjfj','yjbl','K','hj','จองผ่าน  Callcenter',
                'ทดสอบจองระบบ','By Call Center','Line@','รับรถ7.00','จองผ่าน CS',
                'ผ่าน CS','รับด่วนสนามบิน','รับวันนี้15.00','แป้ง','โทรเข้า CC',
                'ผ่าน CC','ลูกค้าจองด่วน','ทดลองจอง','.','จองด่วนโทรเข้าคอลเซ็นเตอร์',
                'จ','1','เทส','0','(Line@ Ann)','ลองจอง','ลูกค้า Line@','อยู่รร. ริเวอร์ไซด์'
                '4/165 ซ.อนามัยงามเจริญ 11 แขวงท่าข้าม เขตบางขุนเทียน กทม.1050',
                'บริษัท รีโวเด็ค จำกัด','ถกลวรรณ  081-7537819','ลูกค้า','จองพรุ่งนี้','biirrz','น.ส.','k',
                'จอง','ไปกาญ','ลูกค้าจองผ่านคอลเซ็นเตอร์','admin จองให้','ลูกค้าจองผ่าน คอลเซ็นเตอร์',
                'admin ส้ม','ลค จองด่วน','เอ็กทำการจองให้','ลูกค้าจองทาง','callcenter','จองด่วนลูกค้าต่างชาติ',
                'ลูกค้าจองด่วน','ผ่านไลน์','(ผู้จองไม่ใช่ผู้ขับ)','nissan march','admin by pang',
                'ลูกค้าจองผ่าน','admin by som','จองผ่าน','คอลเซ็นเตอร์','รอโอนจอง  ค่ะ','รอโอนจองค่ะ',
                'จองย้อนหลัง','ชาวต่างชาติ','ส.ต.ต.','ิ','drivehub gade','จองผ่าน','นาย','mr.','mrs.',
                'mrs','mr','k.','เอ็กทำการจองให้ พี่หมิวรับทราบ','ลค รับด่วน สนามบิน','เคสพี่เอ้ก','เจมส์ส่งลูกค้าให้จากไลน์@',
                'พี่นิดส่งบุ้คให้ไดรฟ์ฮับ','คุณไอซ์ลูกค้าเก่า','ลูกค้าชาวสิงคโปร์','ของดีลเลอร์ที่จ.น่าน','รอเอกสารจากลูกค้าค่ะ',
                'พี่เอ็กส่งเบอร์ให้','ลูกค้าเคสด่วน','ไดรฟ์ฮับจองแทน','lg จอง','เกดทำบุคเข้าให้','ลูกค้าเช่า1วัน','ลูกค้า รับด่วน 11โมง',
                'คืนสนามบิน','ลูกค้ารับป่าตอง','ลูกค้ามาจาก','call center','คุณปู ลูกค้าline@','จองไปกาญ','ลูกค้าจองด่วน',
                'ผ่านไลน์ ','จองผ่าน ']


def replace_word(data,filter_word):
    data['user_omniauth_provider'] = data['user_omniauth_provider'].fillna('')

    data_replace = data.copy()
    data_replace = data_replace.loc[data_replace['user_omniauth_provider'].isin([''])]

    data_replace['first_name'] = data_replace['first_name'].str.lower().replace([x.lower() for x in filter_word], '',)
    data_replace['last_name'] = data_replace['last_name'].str.lower().replace([x.lower() for x in filter_word], '',)
    
    data.update(data_replace)

    invalid_email_index_list = data.index[data.loc[:, 'email'].str.contains('drivehub.co')]
    for i in invalid_email_index_list:
        data.loc[i, 'email'] = ''
        data.loc[i,'call_center'] = 'Yes'
    return data

def filter_status(data):
    data_filtered_status = data.loc[data['status'].isin(['accepted','delivering'])]
    return data_filtered_status

def save_xlsx(file_fil) :
    name = input("File name : ")
    writer = ExcelWriter(str(name)+'.xlsx')   
    file_fil.to_excel(writer,'Sheet1')
    writer.save()

def match_row(row1,row2,x,y):

    condition_1 = ((row1['first_name'][x]) == (row2['first_name'][y]) and (row1['last_name'][x]) == (row2['last_name'][y])) and ((row1['phone'][x]) == (row2['phone'][y]) and (row1['email'][x]) == (row2['email'][y]))
    condition_2 = ((row1['first_name'][x]) == (row2['first_name'][y]) and (row1['last_name'][x]) == (row2['last_name'][y])) and ((row1['phone'][x]) == (row2['phone'][y]))
    condition_3 = ((row1['first_name'][x]) == (row2['first_name'][y]) and (row1['last_name'][x]) == (row2['last_name'][y])) and ((row1['email'][x]) == (row2['email'][y]))
    condition_4 = ((row1['first_name'][x]) == (row2['first_name'][y]) and (row1['phone'][x]) == (row2['phone'][y])) and (row1['email'][x]) == (row2['email'][y])
    condition_5 = ((row1['first_name'][x]) == (row2['first_name'][y])) and ((row1['last_name'][x]) == (row2['last_name'][y]))
    condition_6 = ((row1['first_name'][x]) == (row2['first_name'][y])) and ((row1['phone'][x]) == (row2['phone'][y]))
    condition_7 = ((row1['first_name'][x]) == (row2['first_name'][y]))  and ((row1['email'][x]) == (row2['email'][y]))
    condition_8 = (row1['last_name'][x]) == (row2['last_name'][y]) and (row1['phone'][x]) == (row2['phone'][y]) and (row1['email'][x]) == (row2['email'][y])
    condition_9 = ((row1['last_name'][x]) == (row2['last_name'][y]) and (row1['phone'][x]) == (row2['phone'][y]))
    condition_10 = ((row1['last_name'][x]) == (row2['last_name'][y])) and ((row1['email'][x]) == (row2['email'][y]))
    condition_11 = ((row1['first_name'][x]) == (row2['first_name'][y]) and (row1['phone'][x]) == (row2['phone'][y])) and (row1['email'][x]) == (row2['email'][y])
    condition_12 = ((row1['phone'][x]) == (row2['phone'][y]) and (row1['email'][x]) == (row2['email'][y]))
    condition_13 = ((row1['phone'][x]) == (row2['phone'][y]))
    condition_14 = ((row1['email'][x]) == (row2['email'][y]))
    condition_all = [condition_1,condition_2,condition_3,condition_4,condition_5,condition_6,
                    condition_7,condition_8,condition_9,condition_10,condition_11,condition_12,
                    condition_13,condition_14]
    for x in condition_all : 
        if x == True:
            return True

def loop_data(g1,g2):
    n = 0
    g1 = g1.reset_index(drop=True)
    g2 = g2.reset_index(drop=True)  
    for x in range(len(g1.index)):
        for y in range(len(g2.index)):
            matching = match_row(g1,g2,x,y)
            if matching == True:
                n = n+1

    return n

def sorting(data):
    base_data = data.copy()

    group_2017_04 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 4)]
    group_2017_04_col_fil = group_2017_04.filter(items=['first_name','last_name','phone','email'])

    group_2017_05 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 5)]
    group_2017_05_col_fil = group_2017_05.filter(items=['first_name','last_name','phone','email'])

    group_2017_06 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 6)]
    group_2017_06_col_fil = group_2017_06.filter(items=['first_name','last_name','phone','email'])

    group_2017_07 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 7)]
    group_2017_07_col_fil = group_2017_07.filter(items=['first_name','last_name','phone','email'])

    group_2017_08 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 8)]
    group_2017_08_col_fil = group_2017_08.filter(items=['first_name','last_name','phone','email'])

    group_2017_09 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 9)]
    group_2017_09_col_fil = group_2017_09.filter(items=['first_name','last_name','phone','email'])

    group_2017_10 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 10)]
    group_2017_10_col_fil = group_2017_10.filter(items=['first_name','last_name','phone','email'])

    group_2017_11 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 11)]
    group_2017_11_col_fil = group_2017_11.filter(items=['first_name','last_name','phone','email'])

    group_2017_12 = base_data[(base_data['booking_creation_year'] == 2017) & (base_data['booking_creation_month'] == 12)]
    group_2017_12_col_fil = group_2017_12.filter(items=['first_name','last_name','phone','email'])

    group_2018_01 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 1)]
    group_2018_01_col_fil = group_2018_01.filter(items=['first_name','last_name','phone','email'])

    group_2018_02 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 2)]
    group_2018_02_col_fil = group_2018_02.filter(items=['first_name','last_name','phone','email'])

    group_2018_03 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 3)]
    group_2018_03_col_fil = group_2018_03.filter(items=['first_name','last_name','phone','email'])

    group_2018_04 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 4)]
    group_2018_04_col_fil = group_2018_04.filter(items=['first_name','last_name','phone','email'])

    group_2018_05 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 5)]
    group_2018_05_col_fil = group_2018_05.filter(items=['first_name','last_name','phone','email'])

    group_2018_06 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 6)]
    group_2018_06_col_fil = group_2018_06.filter(items=['first_name','last_name','phone','email'])

    group_2018_07 = base_data[(base_data['booking_creation_year'] == 2018) & (base_data['booking_creation_month'] == 7)]
    group_2018_07_col_fil = group_2018_07.filter(items=['first_name','last_name','phone','email'])

    
    user_return_04_05 = loop_data(group_2017_04_col_fil,group_2017_05_col_fil)
    user_return_04_06 = loop_data(group_2017_04_col_fil,group_2017_06_col_fil)
    user_return_04_07 = loop_data(group_2017_04_col_fil,group_2017_07_col_fil)
    user_return_04_08 = loop_data(group_2017_04_col_fil,group_2017_08_col_fil)
    user_return_04_09 = loop_data(group_2017_04_col_fil,group_2017_09_col_fil)
    user_return_04_10 = loop_data(group_2017_04_col_fil,group_2017_10_col_fil)
    user_return_04_11 = loop_data(group_2017_04_col_fil,group_2017_11_col_fil)
    user_return_04_12 = loop_data(group_2017_04_col_fil,group_2017_12_col_fil)
    print('test1')
    user_return_05_06 = loop_data(group_2017_05_col_fil,group_2017_06_col_fil)
    user_return_05_07 = loop_data(group_2017_05_col_fil,group_2017_07_col_fil)
    user_return_05_08 = loop_data(group_2017_05_col_fil,group_2017_08_col_fil)
    user_return_05_09 = loop_data(group_2017_05_col_fil,group_2017_09_col_fil)
    user_return_05_10 = loop_data(group_2017_05_col_fil,group_2017_10_col_fil)
    user_return_05_11 = loop_data(group_2017_05_col_fil,group_2017_11_col_fil)
    user_return_05_12 = loop_data(group_2017_05_col_fil,group_2017_12_col_fil)
    print('test2')
    user_return_06_07 = loop_data(group_2017_06_col_fil,group_2017_07_col_fil)
    user_return_06_08 = loop_data(group_2017_06_col_fil,group_2017_08_col_fil)
    user_return_06_09 = loop_data(group_2017_06_col_fil,group_2017_09_col_fil)
    user_return_06_10 = loop_data(group_2017_06_col_fil,group_2017_10_col_fil)
    user_return_06_11 = loop_data(group_2017_06_col_fil,group_2017_11_col_fil)
    user_return_06_12 = loop_data(group_2017_06_col_fil,group_2017_12_col_fil)

    user_return_07_08 = loop_data(group_2017_07_col_fil,group_2017_08_col_fil)
    user_return_07_09 = loop_data(group_2017_07_col_fil,group_2017_09_col_fil)
    user_return_07_10 = loop_data(group_2017_07_col_fil,group_2017_10_col_fil)
    user_return_07_11 = loop_data(group_2017_07_col_fil,group_2017_11_col_fil)
    user_return_07_12 = loop_data(group_2017_07_col_fil,group_2017_12_col_fil)

    user_return_08_09 = loop_data(group_2017_08_col_fil,group_2017_09_col_fil)
    user_return_08_10 = loop_data(group_2017_08_col_fil,group_2017_10_col_fil)
    user_return_08_11 = loop_data(group_2017_08_col_fil,group_2017_11_col_fil)
    user_return_08_12 = loop_data(group_2017_08_col_fil,group_2017_12_col_fil)

    user_return_09_10 = loop_data(group_2017_09_col_fil,group_2017_10_col_fil)
    user_return_09_11 = loop_data(group_2017_09_col_fil,group_2017_11_col_fil)
    user_return_09_12 = loop_data(group_2017_09_col_fil,group_2017_12_col_fil)
    
    user_return_10_11 = loop_data(group_2017_10_col_fil,group_2017_11_col_fil)
    user_return_10_12 = loop_data(group_2017_10_col_fil,group_2017_12_col_fil)

    user_return_11_12 = loop_data(group_2017_11_col_fil,group_2017_12_col_fil)
    print('test18')
    user_return_12_01_18 = loop_data(group_2017_12_col_fil,group_2018_01_col_fil)
    user_return_12_02_18 = loop_data(group_2017_12_col_fil,group_2018_02_col_fil)
    user_return_12_03_18 = loop_data(group_2017_12_col_fil,group_2018_03_col_fil)
    user_return_12_04_18 = loop_data(group_2017_12_col_fil,group_2018_04_col_fil)
    user_return_12_05_18 = loop_data(group_2017_12_col_fil,group_2018_05_col_fil)
    user_return_12_06_18 = loop_data(group_2017_12_col_fil,group_2018_06_col_fil)
    user_return_12_07_18 = loop_data(group_2017_12_col_fil,group_2018_07_col_fil)

    user_return_01_02_18 = loop_data(group_2018_01_col_fil,group_2018_02_col_fil)
    user_return_01_03_18 = loop_data(group_2018_01_col_fil,group_2018_03_col_fil)
    user_return_01_04_18 = loop_data(group_2018_01_col_fil,group_2018_04_col_fil)
    user_return_01_05_18 = loop_data(group_2018_01_col_fil,group_2018_05_col_fil)
    user_return_01_06_18 = loop_data(group_2018_01_col_fil,group_2018_06_col_fil)
    user_return_01_07_18 = loop_data(group_2018_01_col_fil,group_2018_07_col_fil)
    
    user_return_02_03_18 = loop_data(group_2018_02_col_fil,group_2018_03_col_fil)
    user_return_02_04_18 = loop_data(group_2018_02_col_fil,group_2018_04_col_fil)
    user_return_02_05_18 = loop_data(group_2018_02_col_fil,group_2018_05_col_fil)
    user_return_02_06_18 = loop_data(group_2018_02_col_fil,group_2018_06_col_fil)
    user_return_02_07_18 = loop_data(group_2018_02_col_fil,group_2018_07_col_fil)
    print('test020318') 
    user_return_03_04_18 = loop_data(group_2018_03_col_fil,group_2018_04_col_fil)
    user_return_03_05_18 = loop_data(group_2018_03_col_fil,group_2018_05_col_fil)
    user_return_03_06_18 = loop_data(group_2018_03_col_fil,group_2018_06_col_fil)
    user_return_03_07_18 = loop_data(group_2018_03_col_fil,group_2018_07_col_fil)
    
    user_return_04_05_18 = loop_data(group_2018_04_col_fil,group_2018_05_col_fil)
    user_return_04_06_18 = loop_data(group_2018_04_col_fil,group_2018_06_col_fil)
    user_return_04_07_18 = loop_data(group_2018_04_col_fil,group_2018_07_col_fil)

    user_return_05_06_18 = loop_data(group_2018_05_col_fil,group_2018_06_col_fil)
    user_return_05_07_18 = loop_data(group_2018_05_col_fil,group_2018_07_col_fil)

    user_return_06_07_18 = loop_data(group_2018_06_col_fil,group_2018_07_col_fil)

    user_return_04_01_18 = loop_data(group_2017_04_col_fil,group_2018_01_col_fil)
    user_return_04_02_18 = loop_data(group_2017_04_col_fil,group_2018_02_col_fil)
    user_return_04_03_18 = loop_data(group_2017_04_col_fil,group_2018_03_col_fil)
    user_return_04_04_18 = loop_data(group_2017_04_col_fil,group_2018_04_col_fil)
    user_return_04_05_18 = loop_data(group_2017_04_col_fil,group_2018_05_col_fil)
    user_return_04_06_18 = loop_data(group_2017_04_col_fil,group_2018_06_col_fil)
    user_return_04_07_18 = loop_data(group_2017_04_col_fil,group_2018_07_col_fil)

    user_return_05_01_18 = loop_data(group_2017_05_col_fil,group_2018_01_col_fil)
    user_return_05_02_18 = loop_data(group_2017_05_col_fil,group_2018_02_col_fil)
    user_return_05_03_18 = loop_data(group_2017_05_col_fil,group_2018_03_col_fil)
    user_return_05_04_18 = loop_data(group_2017_05_col_fil,group_2018_04_col_fil)
    user_return_05_05_18 = loop_data(group_2017_05_col_fil,group_2018_05_col_fil)
    user_return_05_06_18 = loop_data(group_2017_05_col_fil,group_2018_06_col_fil)
    user_return_05_07_18 = loop_data(group_2017_05_col_fil,group_2018_07_col_fil)
    print('test0518')
    user_return_06_01_18 = loop_data(group_2017_06_col_fil,group_2018_01_col_fil)
    user_return_06_02_18 = loop_data(group_2017_06_col_fil,group_2018_02_col_fil)
    user_return_06_03_18 = loop_data(group_2017_06_col_fil,group_2018_03_col_fil)
    user_return_06_04_18 = loop_data(group_2017_06_col_fil,group_2018_04_col_fil)
    user_return_06_05_18 = loop_data(group_2017_06_col_fil,group_2018_05_col_fil)
    user_return_06_06_18 = loop_data(group_2017_06_col_fil,group_2018_06_col_fil)
    user_return_06_07_18 = loop_data(group_2017_06_col_fil,group_2018_07_col_fil)

    user_return_07_01_18 = loop_data(group_2017_07_col_fil,group_2018_01_col_fil)
    user_return_07_02_18 = loop_data(group_2017_07_col_fil,group_2018_02_col_fil)
    user_return_07_03_18 = loop_data(group_2017_07_col_fil,group_2018_03_col_fil)
    user_return_07_04_18 = loop_data(group_2017_07_col_fil,group_2018_04_col_fil)
    user_return_07_05_18 = loop_data(group_2017_07_col_fil,group_2018_05_col_fil)
    user_return_07_06_18 = loop_data(group_2017_07_col_fil,group_2018_06_col_fil)
    user_return_07_07_18 = loop_data(group_2017_07_col_fil,group_2018_07_col_fil)

    user_return_08_01_18 = loop_data(group_2017_08_col_fil,group_2018_01_col_fil)
    user_return_08_02_18 = loop_data(group_2017_08_col_fil,group_2018_02_col_fil)
    user_return_08_03_18 = loop_data(group_2017_08_col_fil,group_2018_03_col_fil)
    user_return_08_04_18 = loop_data(group_2017_08_col_fil,group_2018_04_col_fil)
    user_return_08_05_18 = loop_data(group_2017_08_col_fil,group_2018_05_col_fil)
    user_return_08_06_18 = loop_data(group_2017_08_col_fil,group_2018_06_col_fil)
    user_return_08_07_18 = loop_data(group_2017_08_col_fil,group_2018_07_col_fil)

    user_return_09_01_18 = loop_data(group_2017_09_col_fil,group_2018_01_col_fil)
    user_return_09_02_18 = loop_data(group_2017_09_col_fil,group_2018_02_col_fil)
    user_return_09_03_18 = loop_data(group_2017_09_col_fil,group_2018_03_col_fil)
    user_return_09_04_18 = loop_data(group_2017_09_col_fil,group_2018_04_col_fil)
    user_return_09_05_18 = loop_data(group_2017_09_col_fil,group_2018_05_col_fil)
    user_return_09_06_18 = loop_data(group_2017_09_col_fil,group_2018_06_col_fil)
    user_return_09_07_18 = loop_data(group_2017_09_col_fil,group_2018_07_col_fil)

    user_return_10_01_18 = loop_data(group_2017_10_col_fil,group_2018_01_col_fil)
    user_return_10_02_18 = loop_data(group_2017_10_col_fil,group_2018_02_col_fil)
    user_return_10_03_18 = loop_data(group_2017_10_col_fil,group_2018_03_col_fil)
    user_return_10_04_18 = loop_data(group_2017_10_col_fil,group_2018_04_col_fil)
    user_return_10_05_18 = loop_data(group_2017_10_col_fil,group_2018_05_col_fil)
    user_return_10_06_18 = loop_data(group_2017_10_col_fil,group_2018_06_col_fil)
    user_return_10_07_18 = loop_data(group_2017_10_col_fil,group_2018_07_col_fil)
    print('test100718')
    user_return_11_01_18 = loop_data(group_2017_11_col_fil,group_2018_01_col_fil)
    user_return_11_02_18 = loop_data(group_2017_11_col_fil,group_2018_02_col_fil)
    user_return_11_03_18 = loop_data(group_2017_11_col_fil,group_2018_03_col_fil)
    user_return_11_04_18 = loop_data(group_2017_11_col_fil,group_2018_04_col_fil)
    user_return_11_05_18 = loop_data(group_2017_11_col_fil,group_2018_05_col_fil)
    user_return_11_06_18 = loop_data(group_2017_11_col_fil,group_2018_06_col_fil)
    user_return_11_07_18 = loop_data(group_2017_11_col_fil,group_2018_07_col_fil)

    user_return_12_01_18 = loop_data(group_2017_12_col_fil,group_2018_01_col_fil)
    user_return_12_02_18 = loop_data(group_2017_12_col_fil,group_2018_02_col_fil)
    user_return_12_03_18 = loop_data(group_2017_12_col_fil,group_2018_03_col_fil)
    user_return_12_04_18 = loop_data(group_2017_12_col_fil,group_2018_04_col_fil)
    user_return_12_05_18 = loop_data(group_2017_12_col_fil,group_2018_05_col_fil)
    user_return_12_06_18 = loop_data(group_2017_12_col_fil,group_2018_06_col_fil)
    user_return_12_07_18 = loop_data(group_2017_12_col_fil,group_2018_07_col_fil)

    user_return_per_month = {'': ['user_04_17', 'user_05_17', 'user_06_17', 'user_07_17', 'user_08_17', 'user_09_17', 'user_10_17', 'user_11_17', 'user_12_17','user_01_18','user_02_18','user_03_18','user_04_18','user_05_18','user_06_18','user_07_18','user_08_18'], 
                            '04': ['','','','','','','','','','','','','','','',''],
                            '05': [user_return_04_05],
                            '06': [user_return_04_06, user_return_05_06],
                            '07': [user_return_04_07, user_return_05_07,user_return_06_07],
                            '08': [user_return_04_08, user_return_05_08,user_return_06_08,user_return_07_08],
                            '09': [user_return_04_09, user_return_05_09,user_return_06_09,user_return_07_09,user_return_08_09],
                            '10': [user_return_04_10, user_return_05_10,user_return_06_10,user_return_07_10,user_return_08_10,user_return_09_10],
                            '11': [user_return_04_11, user_return_05_11,user_return_06_11,user_return_07_11,user_return_08_11,user_return_09_11,user_return_10_11],
                            '12': [user_return_04_12, user_return_05_12,user_return_06_12,user_return_07_12,user_return_08_12,user_return_09_12,user_return_10_12,user_return_11_12],
                            '01_18': [user_return_04_01_18,user_return_05_01_18,user_return_06_01_18,user_return_07_01_18,user_return_08_01_18,user_return_09_01_18,user_return_10_01_18,user_return_11_01_18,user_return_12_01_18],
                            '02_18': [user_return_04_02_18,user_return_05_02_18,user_return_06_02_18,user_return_07_02_18,user_return_08_02_18,user_return_09_02_18,user_return_10_02_18,user_return_11_02_18,user_return_12_02_18,user_return_01_02_18],
                            '03_18': [user_return_04_03_18,user_return_05_03_18,user_return_06_03_18,user_return_07_03_18,user_return_08_03_18,user_return_09_03_18,user_return_10_03_18,user_return_11_03_18,user_return_12_03_18,user_return_01_03_18,user_return_02_03_18],
                            '04_18': [user_return_04_04_18,user_return_05_04_18,user_return_06_04_18,user_return_07_04_18,user_return_08_04_18,user_return_09_04_18,user_return_10_04_18,user_return_11_04_18,user_return_12_04_18,user_return_01_04_18,user_return_02_04_18,user_return_03_04_18],
                            '05_18': [user_return_04_05_18,user_return_05_05_18,user_return_06_05_18,user_return_07_05_18,user_return_08_05_18,user_return_09_05_18,user_return_10_05_18,user_return_11_05_18,user_return_12_05_18,user_return_01_05_18,user_return_02_05_18,user_return_03_05_18,user_return_04_05_18],
                            '06_18': [user_return_04_06_18,user_return_05_06_18,user_return_06_06_18,user_return_07_06_18,user_return_08_06_18,user_return_09_06_18,user_return_10_06_18,user_return_11_06_18,user_return_12_06_18,user_return_01_06_18,user_return_02_06_18,user_return_03_06_18,user_return_04_06_18,user_return_05_06_18],
                            '07_18': [user_return_04_07_18,user_return_05_07_18,user_return_06_07_18,user_return_07_07_18,user_return_08_07_18,user_return_09_07_18,user_return_10_07_18,user_return_11_07_18,user_return_12_07_18,user_return_01_07_18,user_return_02_07_18,user_return_03_07_18,user_return_04_07_18,user_return_05_07_18,user_return_06_07_18]}
    df = pd.DataFrame(data=user_return_per_month)      
    return df

data = filter_status(df)
data = data.copy()
data = replace_word(data,filter_word)
#save_xlsx(data)
#save_xlsx(data_fil_cc)
#data.to_csv('data_clean.csv')
print(sorting(data))

""" def filter_condition(data):
    condition_first_name = data.index[data.loc[:, 'first_name'].str.contains('')]
    for x in condition_first_name:
        if (data['email'][x] == '') & (data['phone'][x] == '') & (data['last_name'][x] == ''):
            data = data.drop(x , axis=0)
            data.reset_index(drop=True)

    condition_last_name = data.index[data.loc[:, 'last_name'].str.contains('')]
    for x in condition_last_name:
        if ((data['email'][x] == '') & (data['phone'][x] == '')) & (data['first_name'][x] == ''):
            data = data.drop(x , axis=0)
            data.reset_index(drop=True)
    return data """

"""         if  condition_1 == True :
        return True
    if condition_2 == True :
        return True
    if condition_3 == True :
        return True
    if condition_4 == True :
        return True
    if condition_5 == True :
        return True            
    if condition_6 == True :
        return True
    if condition_7 == True :
        return True
    if condition_8 == True :
        return True
    if condition_9 == True :
        return True
    if condition_10 == True :
        return True
    if condition_11 == True :
        return True
    if condition_12 == True :
        return True
    if condition_13 == True :
        return True
    if condition_14 == True :
        return True
 """