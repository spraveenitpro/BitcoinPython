# import bitcoin

from bitcoin import *

# Generate Private key

my_private_key1 = random_key()
my_private_key2 = random_key()
my_private_key3 = random_key()


# Generate Public key

my_public_key1 = privtopub(my_private_key1)
my_public_key2 = privtopub(my_private_key2)
my_public_key3 = privtopub(my_private_key3)




# Create multisig address

my_multi_sig = mk_multisig_script(my_public_key1,my_public_key2, my_public_key3, 2, 3)
my_multi_address = scriptaddr(my_multi_sig)

print(my_multi_address)
