#create a set of TLS certs for 443 connection and possible MitM

echo FILENAME=server
# Generate a public/private key pair:
openssl genrsa -out $FILENAME.key 1024
# Generate a self signed certificate:
openssl req -new -key $FILENAME.key -x509 -sha256 -days 3653 -out $FILENAME.crt
# Generate the PEM file by just appending the key and certificate files:
cat $FILENAME.key $FILENAME.crt >$FILENAME.pem
# sudo socat -v -v openssl-listen:443,reuseaddr,fork,cert=$FILENAME.pem,cafile=$FILENAME.crt,verify=0 -
#Redirect to legitimate site
# sudo socat -v -v openssl-listen:443,reuseaddr,fork,cert=$FILENAME.pem,cafile=$FILENAME.crt,verify=0 openssl-connect:[SERVER]:[PORT],verify=0
