
#!/bin/bash

# Prompt user for input
read -p "Enter the IP address: " ip_address
read -p "Enter the hostname: " hostname

# Set environmental variable
export TARGET="$ip_address"

# Construct the command to update /etc/hosts
update_hosts_command="echo \"$ip_address $hostname\" | sudo tee -a /etc/hosts"

# Execute the command to update /etc/hosts
eval "$update_hosts_command"

# Construct the nmap command
nmap_command="sudo nmap -p\$(nmap -p- --min-rate=1000 -T4 $TARGET -Pn | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//) -sC -sV -Pn -vvv $TARGET -oN nmap_tcp_all.nmap"

# Execute the nmap command
eval "$nmap_command"


##chmod +x htbstart
# note: maybe try adding openvpn start to the script as wellbut must include time delay of 40 seconds. Ideas Adam? I know you better be reading this super vulnerable code....I mean look at me running unvalidated eval !

