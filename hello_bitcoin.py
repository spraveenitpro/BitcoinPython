# import bitcoin

from bitcoin import *

# Generate Private key

my_private_key = random_key()

print("Private Key: %s\n" % my_private_key)


# Generate Public key


my_public_key = privtopub(my_private_key)


# Create bitcoin address

my_address = pubtoaddr(my_public_key)


print my_address

