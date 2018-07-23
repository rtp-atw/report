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
                'ผ่านไลน์ ','จองผ่าน ','drivehub admin ทำการจองให้','drivehub gade ','เพื่อนพี่แทรคเตอร์drivehub',
                'drivehub จอง','drivehub จองให้','จองครับ ','เช่าไปสุพรรณ จองมาทาง lind add',
                'dh ทำจอง','x จองให้','จอง cs ']


def replace_word(data,filter_word):
    data['user_omniauth_provider'] = data['user_omniauth_provider'].fillna('')

    data_replace = data.copy()
    data_replace = data_replace.loc[data_replace['user_omniauth_provider'].isin([''])]

    data_replace['first_name'] = data_replace['first_name'].str.lower().replace([x.lower() for x in filter_word], '',)
    data_replace['last_name'] = data_replace['last_name'].str.lower().replace([x.lower() for x in filter_word], '',)
    
    data.update(data_replace)

    invalid_email_index_list = data.index[data.loc[:, 'email'].str.contains('drivehub.co','drivehib.co')]
    for i in invalid_email_index_list:
        data.loc[i, 'email'] = ''
        data.loc[i,'call_center'] = 'Yes'

    invalid_first_name_index_list = data.index[data.loc[:, 'first_name'].str.contains('drivehub')]
    invalid_last_name_index_list = data.index[data.loc[:, 'last_name'].str.contains('drivehub')]
    for i in invalid_first_name_index_list:
        data.loc[i, 'first_name'] = ''
    for i in invalid_last_name_index_list:
        data.loc[i, 'last_name'] = ''

    return data

def filter_status(data):
    data_filtered_status = data.loc[data['status'].isin(['accepted','delivering'])]
    return data_filtered_status

def save_xlsx(file_fil) :
    name = input("File name : ")
    #name = 'df_result_returning'
    writer = ExcelWriter(name +'.xlsx')
    file_fil.to_excel(writer,'Sheet1')
    writer.save()

def match_row(row1,row2,x,y):
    condition_1 = ((row1['first_name'][x]) == (row2['first_name'][y])) and ((row1['last_name'][x]) == (row2['last_name'][y]))
    condition_2 = ((row1['phone'][x]) == (row2['phone'][y]))
    condition_3 = ((row1['email'][x]) == (row2['email'][y]))

    if (row1['first_name'][x] != '') and (row1['last_name'][x] != ''):
        if condition_1:
            print(str(row1['first_name'][x]).encode('utf-8'),str(row1['last_name'][x]).encode('utf-8'),str(row2['first_name'][y]).encode('utf-8'),str(row2['last_name'][y]).encode('utf-8'))
            return True
    if ((row1['phone'][x] != '') and (row2['phone'][y]) != ''):
        if condition_2:
            print(row1['phone'][x],row2['phone'][y])
            return True
    if ((row1['email'][x] != '') and (row2['email'][y] != '')):
        if condition_3:
            print(row1['email'][x],row2['email'][y])
            return True
    else:
        return False


def loop_data(g1,g2):
    n = 0  
    g1 = g1.reset_index(drop=True)
    g2 = g2.reset_index(drop=True)

    for x in range(len(g1.index)):
        for y in range(len(g2.index)):
            matching = match_row(g1,g2,x,y)
            if matching == True:
                print(x,y,matching)
                n = n+1
                print(n)
    return n

def grouping(data):
    base_data = data.copy()
    group = {}
    list_of_name = []
    data_filter = base_data.filter(items=['booking_creation_year','booking_creation_month'])
    data_filter = data_filter.drop_duplicates(['booking_creation_year','booking_creation_month'])
    df_year_month = data_filter.reset_index(drop=True)

    for i in range(len(df_year_month.index)):
        name = 'group_'+str(int(df_year_month['booking_creation_year'][i]))+'_'+str(int(df_year_month['booking_creation_month'][i]))
        list_of_name.append(name)
        data =  base_data[(base_data['booking_creation_year'] == df_year_month['booking_creation_year'][i]) & (base_data['booking_creation_month'] == df_year_month['booking_creation_month'][i])]
        data =  data.filter(items=['first_name','last_name','phone','email'])
        data =  data.reset_index(drop=True)
        group[name] = data

    data_compare = compare_returning(group,list_of_name)

    return data_compare

def compare_returning(group,list_of_name):
    user_actual_return = {}
    for i in range(len(list_of_name)):

        for x in range(i+1, len(list_of_name)):
            if x < len(list_of_name):
                name = list_of_name[i]+'_'+list_of_name[x]
                print(name)
                data = loop_data(group[list_of_name[i]],group[list_of_name[x]])
                user_actual_return[name] = data
                print(user_actual_return)
    return user_actual_return

def creatDataframe(df):
    base_data = df.copy()
    data_filter = base_data.filter(items=['booking_creation_year','booking_creation_month'])
    data_filter = data_filter.drop_duplicates(['booking_creation_year','booking_creation_month'])
    df_year_month = data_filter.reset_index(drop=True)
    print(df_year_month)
    return True

data = filter_status(df)
data = data.copy()
data = replace_word(data,filter_word)
test_data = grouping(data)
#print(test_data)
#test_df = pd.DataFrame(test_data.items())
#test_df.to_csv('test_df.csv')
#dic = {'key': 3}
#dic_2 = pd.DataFrame(list(dic.items()), columns=['id','value'])
print(creatDataframe(df))


#save_xlsx(data)
#data.to_csv('data_cleaned.csv')
#df_result_returning = sorting(data)
#save_xlsx(df_result_returning)