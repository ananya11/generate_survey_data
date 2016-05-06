import numpy
#import uuid
from datetime import datetime
import csv
import time, random, md5
import cx_Oracle



def getNewID(tag):
        t1 = time.time()
        time.sleep(random.random())
        t2 = time.time()
        base = md5.new(tag + str(t1+t2))
        sid = tag + '_' + base.hexdigest()
        return sid



def generate_fk_data(idst, users):
        id = idst
        with open('fk_data.csv', 'w+') as fkf:
                csvwriter = csv.writer(fkf, delimiter='|', quoting=csv.QUOTE_NONE, quotechar='')
                for i in range(users):
                        #session_key = str(uuid.uuid1()).replace('-','')
                        print i
                        session_key = getNewID('fk')
                        form_id = 12

                        row = []
                        id +=1
                        ques_name = 'age-in-years'
                        user_resp = numpy.random.choice(range(18,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        #ins_txt = "INSERT INTO DYNAMIC_FORMS_FORMMODELDATA (ID, QUES_NAME, USER_RESP, SUBMITTED, SESSION_KEY, FORM_ID) values (" + ', '.join(row) + ")"
                        #print ins_txt
                        #cur.execute(ins_txt)
                        #conn.commit()
                        #cur.close()
                        #conn.close()
                        #break;
                        csvwriter.writerow(row)
  
                          row = []
                        id += 1
                        ques_name = 'your-gender'
                        user_resp = numpy.random.choice(['Male', 'Female'],1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                        row = []
                        id += 1
                        ques_name = 'how-many-people-home'
                        user_resp = numpy.random.choice(range(1,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                        row = []
                        id += 1
                        ques_name = 'household-yearly-income'
                        user_resp = numpy.random.choice(['0 - 24,999', '25,000 - 74,999', '75,000 or more'],1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                       row = []
                        id += 1
                        ques_name = 'when-were-you-sick'
                        weeks = [ "September - week 1",
                                        "September - week 2",
                                        "September - week 3",
                                        "September - week 4",
                                        "September - week 5 or October - week 1",
                                        "October - week 2",
                                        "October - week 3",
                                        "October - week 4",
                                        "October - week 5",
                                        "November - week 1",
                                        "November - week 2",
                                        "November - week 3",
                                        "November - week 4",
                                        "December - week 1",
                                        "December - week 2",
                                        "December - week 3",
                                        "December - week 4",
                                        "December - week 5",
                                        "I did not fall sick"]
                        pick = numpy.random.choice(range(1,6),1)[0]
#                       user_resp = numpy.random.choice(weeks,size=pick,replace=False).tolist()

                        uresp = numpy.random.choice(weeks,size=pick, replace= False)
                        user_resp='['
                        for usr in uresp:
                                user_resp = user_resp + 'u\''+ usr + '\','

                        user_resp = user_resp.rstrip(',') + ']'
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        #print user_resp
                        csvwriter.writerow(row)

                        row = []
                        id += 1
                        ques_name = 'family-members-fell-ill-sept'
                        user_resp = numpy.random.choice(range(1,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                        row = []
                        id += 1
                        ques_name = 'family-members-fell-ill-oct'
                        user_resp = numpy.random.choice(range(1,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                        row = []
                        id += 1
                        ques_name = 'family-members-fell-ill-nov'
                        user_resp = numpy.random.choice(range(1,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)

                       row = []
                        id += 1
                        ques_name = 'family-members-fell-ill-dec'
                        user_resp = numpy.random.choice(range(1,100),1)[0]
                        submitted = datetime.strftime(datetime.now(),'%d-%B-%y %I:%M:%S.%f %p')
                        row.append(id)
                        row.append(ques_name)
                        row.append(user_resp)
                        row.append(submitted)
                        row.append(session_key)
                        row.append(form_id)
                        csvwriter.writerow(row)



def load_fk_data():
        connStr = 'uname/pwd@server:port/service'
        conn =  cx_Oracle.connect(connStr)
        cur = conn.cursor()

        li = []
        with open('fk_data.csv', 'r') as f:
                cur.prepare("""INSERT INTO DYNAMIC_SURVEY_DATA (ID, QUES_NAME, USER_RESP, SUBMITTED, SESSION_KEY, FORM_ID) values (:1, :2, :3, :4, :5, :6)""")
                for line in f:
                        pair = line.split('|')
                        print pair
                        li.append((pair[0], pair[1],pair[2], pair[3], pair[4], pair[5].strip('\r\n')))
                cur.executemany(None, li)
                conn.commit()
        cur.close()
        conn.close()



if __name__ == '__main__':
        idst = 122138
        users = 100000
        generate_fk_data(idst, users)
 #       load_fk_data()

                                                          
