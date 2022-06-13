import email.message

msg = email.message.EmailMessage()
# "寄件人"
msg["From"] = "chihm0720@gmail.com"
# "收件人"
msg["To"] = "weichu0114@gmail.com "
msg["Subject"] = "你好,韋筑"

# 寄送純文字的內容
msg.set_content("add oil")
# 寄送多樣式的內容
# msg.add_alternative("<h3>優惠券</h3>滿500送100喔!!", subtype = "html")

# 連線到 SMTP server (驗證寄件人身分並發送郵件)
import smtplib

# 到網路上搜 gmail SMTP server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# ("帳號", "密碼")
server.login("chihm0720@gmail.com", "chicm860720")
server.send_message(msg)
server.close()