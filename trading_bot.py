#!/usr/bin/python


# import modules

from exchanges.bitfinex import Bitfinex
import smtplib

# Function to send email

def trigger_email(msg):
	#Email details
	email_user = "admin@admin.dev"
	email_password = "password"
	smtp_server = 'smtp.gmail.com'
	smtp_port = 587
	email_from = "bitcoin@gmail.com"
	email_to = "eth@gmail.com"

	# Login to email server

	server = smtplib.SMTP( smtp_server, smtp_port)
	server.starttls()
	server.login(email_user, email_password)

	# Send Email

	server.sendmail(email_from,email_to,msg)
	server.quit()


# Define buy and sell for BTC

buy_thresh = 4000
sell_thresh = 4400

# Get BTC prices

btc_sell_price = Bitfinex().get_current_bid
btc_buy_price = Bitfinex().get_current_ask

# Trigger buy email if the buy price is less than the threshold

if btc_buy_price < buy_thresh:

	email_msg = """
	Bitcoin buy price is %s which is lower than
	threshold price of %s.
	Good time to buy""" % (btc_buy_price, buy_thresh)
	trigger_email(email_msg)

# Trigger sell email if the sell price is higher than the threshold

if btc_sell_price  > sell_thresh:
	email_msg = """
	Bitcoin sell price is %s which is higher than
	the threshold price of %s.
	Good time to sell""" % (btc_sell_price, sell_thresh)
	trigger_email(email_msg)





