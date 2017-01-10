import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


recipients = ['jeffreiher@gmail.com', 'jeffreiher@bulletmail.org', "jreiher2003@yahoo.com", "web-26x2e@mail-tester.com"]
for i in range(len(recipients)):
    try:
        sender = 'email@asciichan-tripplannr.com'
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Signup for Dropbox"
        msg['From'] = formataddr((str(Header('Cloud Storage', 'utf-8')), 'email@asciichan-tripplannr.com'))
        msg["To"] = "".join(recipients[i])

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you %s?\nHere is the dropbox link you wanted:\nhttps://db.tt/wW7clVpS" % recipients[i]
        html = """\
        <html>
          <head>
          </head>
          <body style="background-color:rgba(233,235,238,1);padding:5px;">
            <p style="font-size:14px;>Hi! """ + recipients[i] + """</p><br>
            <p style="font-size:14px;>Here is the <img src='https://cfl.dropboxstatic.com/static/images/icons/blue_dropbox_glyph-vflOJKOUw.png' width="20" alt="Dropbox Logo"> <a href="https://db.tt/wW7clVpS"><b>Dropbox link</b></a> you want.</p>  
            <p>Sign up now and recieve 4GB of storage free</p><p style="visibility:hidden">This is hidden text for a newsletter that is inside an email.  I am doing this to add words to a page.  I think that you should signup to dropbox and love it like I do! Here is some more words to fill up the page and talk about nothing really.</p>
            <br><br>
            <p>The dig utility is pretty convenient to use. The order of the arguments don't really matter.I'll show you some easy examples.
                To get all root name servers use

                # dig
                To get a TXT record of a specific host use

                # dig example.com txt
                # dig host.example.com txt
                To query a specific name server just add @nameserver.tld

                # dig host.example.com txt @a.iana-servers.net
                The SPF RFC4408 says that SPF records can be stored as SPF or TXT. However nearly all use only TXT records at the moment. So you are pretty safe if you only fetch TXT records.

                I made a SPF checker for visualising the SPF records of a domain. It might help you to understand SPF records better. You can find it here: http://spf.myisp.ch
            </p>
            <p style="text-align:left;font-size:7px;">If you'd prefer not to receive future emails, <a href="#">Unsubscribe Here</a> . 
                P.O.Box 4600 Hollywood, FL 33022-9998
            </p>
          </body>
        </html>
        """
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP('mail.asciichan-tripplannr.com')
        s.starttls()
        s.ehlo()
        s.set_debuglevel(1)

        try:

            s.sendmail(sender, [recipients[i]], msg.as_string())
            time.sleep(5)
        finally:
            s.quit()
    except Exception, exc:
        sys.exit("mail failed; %s" % str(exc))

#########################################################


