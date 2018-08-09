import csv


filter_word = ['xxxx', 'jjjjj', 'xxx', 'ไดรฟ์ฮับ', '', 'ทดสอบ', 'testx',
               'Drivehub', 'คับ', 'test', 'testing', 'test', 'ลุงคิดละ',
               'x', 'reserve', 'tester', 'test003', 'test02', 'test004',
               'tesing for top carrent', 'ex', 'noo', 'joy', 'pattaya',
               'lg', 'รับด่วน ที่ส่ง 2 คัน', 'X จอง', 'gade', 'เช่ารายเดือน', 'LINE@',
               'พี่บี', 'โอเค', 'จองให้ลูกค้า', 'V.', 'เอ็กจองให้', 'ลค มาทาง line',
               'dfsdfsdf', 'sdfgsdfsdf', 'ลุกค้าLine@', 'จองด่วน', 'จองผ่าน call center',
               'ลูกค้าจองผ่าน Call Center', 'Admin by PX', 'จองแทนลูกค้า', 'แทรคเตอร์จองแทน',
               'ลูกค้าคนจีน', 'จองผ่าน Callcenter', "Admin by P'X", 'vv', 'fsssssss',
               'ลูกค้า', '25 วัน', 'ส้ม', 'ทดสอบ', 'TT', 't', 'I', 'nui', 'cc',
               'พพ', 'พพพ', 'drivehubtestCPA', 'จองเอง2', 'n', 'nin',
               'ไลน์ @', 'จองผ่าน Call', 'คุณเอก', 'ผ่านทาง call center', 'Cnv',
               'iOS', 'max', 'dh', 'hjfj', 'yjbl', 'K', 'hj', 'จองผ่าน  Callcenter',
               'ทดสอบจองระบบ', 'By Call Center', 'Line@', 'รับรถ7.00', 'จองผ่าน CS',
               'ผ่าน CS', 'รับด่วนสนามบิน', 'รับวันนี้15.00', 'แป้ง', 'โทรเข้า CC',
               'ผ่าน CC', 'ลูกค้าจองด่วน', 'ทดลองจอง', '.', 'จองด่วนโทรเข้าคอลเซ็นเตอร์',
               'จ', '1', 'เทส', '0', '(Line@ Ann)', 'ลองจอง', 'ลูกค้า Line@', 'อยู่รร. ริเวอร์ไซด์'
                                                                              '4/165 ซ.อนามัยงามเจริญ 11 แขวงท่าข้าม เขตบางขุนเทียน กทม.1050',
               'บริษัท รีโวเด็ค จำกัด', 'ถกลวรรณ  081-7537819', 'ลูกค้า', 'จองพรุ่งนี้', 'biirrz', 'น.ส.', 'k',
               'จอง', 'ไปกาญ', 'ลูกค้าจองผ่านคอลเซ็นเตอร์', 'admin จองให้', 'ลูกค้าจองผ่าน คอลเซ็นเตอร์',
               'admin ส้ม', 'ลค จองด่วน', 'เอ็กทำการจองให้', 'ลูกค้าจองทาง', 'callcenter', 'จองด่วนลูกค้าต่างชาติ',
               'ลูกค้าจองด่วน', 'ผ่านไลน์', '(ผู้จองไม่ใช่ผู้ขับ)', 'nissan march', 'admin by pang',
               'ลูกค้าจองผ่าน', 'admin by som', 'จองผ่าน', 'คอลเซ็นเตอร์', 'รอโอนจอง  ค่ะ', 'รอโอนจองค่ะ',
               'จองย้อนหลัง', 'ชาวต่างชาติ', 'ส.ต.ต.', 'ิ', 'drivehub gade', 'จองผ่าน', 'นาย', 'mr.', 'mrs.',
               'mrs', 'mr', 'k.', 'เอ็กทำการจองให้ พี่หมิวรับทราบ', 'ลค รับด่วน สนามบิน', 'เคสพี่เอ้ก',
               'เจมส์ส่งลูกค้าให้จากไลน์@',
               'พี่นิดส่งบุ้คให้ไดรฟ์ฮับ', 'คุณไอซ์ลูกค้าเก่า', 'ลูกค้าชาวสิงคโปร์', 'ของดีลเลอร์ที่จ.น่าน',
               'รอเอกสารจากลูกค้าค่ะ',
               'พี่เอ็กส่งเบอร์ให้', 'ลูกค้าเคสด่วน', 'ไดรฟ์ฮับจองแทน', 'lg จอง', 'เกดทำบุคเข้าให้', 'ลูกค้าเช่า1วัน',
               'ลูกค้า รับด่วน 11โมง',
               'คืนสนามบิน', 'ลูกค้ารับป่าตอง', 'ลูกค้ามาจาก', 'call center', 'คุณปู ลูกค้าline@', 'จองไปกาญ',
               'ลูกค้าจองด่วน',
               'ผ่านไลน์ ', 'จองผ่าน ', 'drivehub admin ทำการจองให้', 'drivehub gade ', 'เพื่อนพี่แทรคเตอร์drivehub',
               'drivehub จอง', 'drivehub จองให้', 'จองครับ ', 'เช่าไปสุพรรณ จองมาทาง lind add',
               'dh ทำจอง', 'x จองให้', 'จอง cs ', 'z']


def replace_word(data, filter_word):
    word = 'drivehub.co'
    for x in filter_word:
        if data['user_omniauth_provider'] == '':
            continue
        data['first_name'] = data['first_name'].replace(x, '', )
        data['last_name'] = data['last_name'].replace(x, '', )
    if word in data['email']:
        data['email'] = ''
    return data

def getName(group1):
    name = ''
    for i in group1:
        name = i['booking_creation_year']+'/'+ i['booking_creation_month']
        break
    return name


def compare_data(group1, group2):
    n = 0
    for i in group1:
        for x in group2:
            if i['first_name'] != '' and x['first_name'] != '':
                if i['first_name'] == x['first_name'] and i['last_name'] == x['last_name']:
                    n +=1
                    # return True
            elif i['email'] != '' and x['email'] != '':
                if i['email'] == x['email']:
                    n += 1
                    # return True
            elif i['phone'] != '' and x['phone'] != '':
                if i['phone'] == x['phone']:
                    n += 1
                    # return True
            else:
                return False
    return n

def loop_data(datas):

    returnUser = []
    returnPerMonth = {}
    for i in range(len(datas)):
        name = getName(datas[i])
        for x in range(i + 1, len(datas)):
            data = compare_data(datas[i], datas[x])
            returnUser.append(data)
        returnPerMonth[name] = returnUser
        returnUser = []

    return returnPerMonth

    # return print(len(datas))

def calReturnUser(datas):

    user_return = loop_data(datas)

    return print(user_return)


with open("book2.tsv") as f:
    datas = []
    year_month_datas = []
    current_year_month = '20174'

    for line in f:
        splitted = line.split('	')
        if splitted[8] == 'cancelled' or splitted[8] == 'rejected':
            continue

        data = {}
        data['first_name'] = splitted[3]
        data['last_name'] = splitted[4]
        data['phone'] = splitted[5]
        data['email'] = splitted[2]
        data['booking_creation_month'] = splitted[12]
        data['booking_creation_year'] = splitted[11]
        data['user_id'] = splitted[1]
        data['user_omniauth_provider'] = splitted[34]

        data = replace_word(data, filter_word)

        if data['booking_creation_year'] + data['booking_creation_month'] == current_year_month:

            year_month_datas.append(data)
        else:
            current_year_month = data['booking_creation_year'] + data['booking_creation_month']
            if (len(year_month_datas) != 0):
                datas.append(year_month_datas)
            year_month_datas = []

    if (len(year_month_datas) != 0):
        datas.append(year_month_datas)
    print(datas)
    calReturnUser(datas)
    # group1 = datas[11]
    # group2 = datas[12]
    # test = compare_data(group1,group2)
    with open("output.csv", "wt") as f:
        writer = csv.writer(f)
        writer.writerows(datas)
