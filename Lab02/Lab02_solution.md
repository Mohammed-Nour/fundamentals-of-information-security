# Lab 2 Web Application Security


### Name: Mohamad Nour Shahin
### Group number: B22-CBS-01



# Questions to Answer

## Task 1

Setup a simple web application with a database connectivity (any application works).



---

### Solution:

For solving this task I used the classwork app and i will attached to my solution.
you can check the code inside the zip file.

![alt text](image-41.png)

![alt text](image-44.png)

---

## Task 2

Setup authentication to DB using one of the following methods:



- Basic
- Digest
- Certificate


---




### Solution:
For solving this task I used the classwork app and i will attached to my solution.
you can check the code inside the zip file.

![alt text](image-42.png)

![alt text](image-43.png)
---


## Task 3

Secure your database:




- Disable remote Root Login of the SQL server
- Disable SSH Password Authentication on the host machine
- Assign a password to the SQL Root User
- Perform the MySQL Secure Installation
- Bind the Database to Localhost


### Solution:


1. Disable remote Root Login of the SQL server:
Firstly, I will Log in to the MySQL server as the root user from locale machine and entering the password using command:


```command
sudo mysql -u root -p
```
![alt text](image.png)

Secondly, Run the following SQL script against the MySQL server, to remove all access from remote hosts for the ‘root’ user account:


```command
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
```

![alt text](image-1.png)

Finally, After making changes to permissions/user accounts, make sure you flush the provilege tables using the following command:

```command
FLUSH PRIVILEGES;
```
![alt text](image-2.png)


Testing to connect to from my friend laptop Ali using command in his laptop connecting to same network:

- to know my ip.
```command
ifconfig
```
![alt text](image-3.png)

- running command to connect to my local database using command:
```command
mysql -u root -h 10.100.20.22 -p
```

![alt text](image-4.png)

- So we can say that Ali couldn't connect to my database, because I disabled it 

---

2. Disable SSH Password Authentication on the host machine:

- Firstly, we need to edit the SSH configiration file where we will open its file and edit it using command:

```command
sudo nano /etc/ssh/sshd_config
```

![alt text](image-5.png)
![alt text](image-6.png)

- Secondly, we need to find line #PasswordAuthentication yes and change it to PasswordAuthentication no:

![alt text](image-7.png)

- Thirdly, we need to restart the SSH service using command:
```command
service ssh restart
```

![alt text](image-8.png)

Finally, we will test it with Ali device and I gave him my ip before, and connect to same network:

![alt text](image-9.png)


- So we can say that Ali couldn't connect to device using SSH. 


---

3. Assign a password to the SQL Root User: 
-  we did it before while installing the MySql in the device, but we can change it using commands:
    - Login into Mysql
    ```command
    sudo mysql -u root -p
    ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123123123';
    FLUSH PRIVILEGES;
    ```

    ![alt text](image-10.png)

---


4. Perform the MySQL Secure Installation:

- I will provide the screenshots:

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)


---


5. Bind the Database to Localhost using the command:


Firstly, we will check the configuration file and update the bind-address value to 127.0.0.1 (localhost) on it using command:
```command
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
cat /etc/mysql/mysql.conf.d/mysqld.cnf
sudo systemctl restart mysql
```
![alt text](image-15.png)
![alt text](image-16.png)

![alt text](image-17.png)

---

## Task 4

Configure rate limiting on your web application and run a benchmark utility against the application to test and see when the application starts dropping requests.

> You can use tools like Apache benchmark.

---



### Solution:
firstly, I will use Flask-Limiter to add rate limiting to the web application using commands:
```command
pip install Flask-Limiter
nano my_flask_app/app.py
flask limiter config
flask limiter limits
```
![alt text](image-18.png)

![alt text](image-19.png)


![alt text](image-21.png)

![alt text](image-22.png)


secondly, from the images you can see that I added the limits to my app, now we will move to test it using commands:

```command
ab -V
ab -n 100 -c 10  http://localhost:5000/data_entry
ab -n 100 -c 10  http://localhost:5000/
```

![alt text](image-23.png)
![alt text](image-24.png)
![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)
![alt text](image-28.png)

Finally, in the screenshots you can notice that limter was working.


---



## Task 5

Monitor/protect the webserver using any of the following tools:


- Network Firewall.
- Intrusion Detection System such as Snort or Suricata.
- Web Application Firewalls such as IronBee, WebKnight, Shadow Daemon.
- Monitoring tools such as Prometheus, Grafana.
- Honeypots; Glastopf, WebTrap, honeyhttpd
> https://github.com/paralax/awesome-honeypots 

> https://owasp.org/www-community/Web_Application_Firewall





---



### Solution:
I will use network firewall especially ufw using commands:


```command
sudo apt-get install ufw
sudo ufw allow 80/tcp  
sudo ufw allow 443/tcp 
sudo ufw allow 5000
sudo ufw deny 3306
sudo ufw enable
sudo ufw status
```
- Firstly, i will install the package, and allowing connecting to 80, 443, 5000 (our localhost),  and denying connecting to our database using outside connection using ssh

- here is the screenshots:


![alt text](image-29.png)

![alt text](image-30.png)

![alt text](image-31.png)

![alt text](image-32.png)

![alt text](image-33.png)

![alt text](image-34.png)

![alt text](image-35.png)


- Finally, you can see that the firewall is active and the ports tracking.
---



## Task 6

Salting:

- Use the sha256sum utility to hash your name at least twice. Are the output the same?
- Create two random strings A and B of 6 characters each. These strings are your salts.
- Append string A to your name and hash it.
- Append string B to your name and hash it.
- How do you think such salting practices will help if usernames and passwords get exposed in a database leak.
- Find any database leak with user credentials on the internet. Use only openly available information from sources such as pastbein. Don't perform any active reconnaissance.

---

### Solution:

1. Use the sha256sum utility to hash your name at least twice. Are the output the same using commands: 
```command
echo -n "Mohamad Nour Shahin" | sha256sum
echo -n "Mohamad Nour Shahin" | sha256sum
```
![alt text](image-36.png)

it was the smae hashing

2. Create two random strings A and B of 6 characters each. These strings are your salts using command:.
```command
openssl rand -hex 3
```

![alt text](image-38.png)

3. Append string A to your name and hash it and Append string B to your name and hash it using commands:

```command
echo -n "Mohamad Nour Shahincf8eff" | sha256sum
echo -n "Mohamad Nour Shahin58f79e" | sha256sum
```

![alt text](image-39.png)


now it is different hashing, after adding the slating.

4. How do you think such salting practices will help if usernames and passwords get exposed in a database leak.

Password salting increases password complexity, making them unique and secure without affecting user experience. It also helps prevent hash table attacks and slows down brute-force and dictionary attacks.

5. Find any database leak with user credentials on the internet. Use only openly available information from sources such as pastbein. Don't perform any active reconnaissance.

here is the link to the leak data and a screenshot.

https://pastebin.com/6DENG8xS

![alt text](image-40.png)

---



## Task 7
Describe OWASP Top 10 in your own words.

>
Open Web Application Security Project
https://owasp.org/Top10/
>


---

### Solution:

1. **Broken Access Control**  
   When people can access files or areas they shouldn't. Example: Someone gets into private files that should be hidden.

2. **Cryptographic Failures**  
   Weak or missing encryption that makes it easy to steal data. Example: Not encrypting passwords properly allows hackers to guess them.

3. **Injection**  
   Unfiltered user inputs lead to attacks. Example: A hacker can trick the system using a SQL query.

4. **Insecure Design**  
   Bad system design leads to security problems. Example: Two users buying the same item at the same time and causing issues.

5. **Security Misconfiguration**  
   Mistakes in setup leave security holes. Example: Leaving unnecessary ports open on a server.

6. **Vulnerable and Outdated Components**  
   Using old, unsafe software parts. Example: An old version of a plugin has known issues hackers can exploit.

7. **Identification and Authentication Failures**  
   Issues with verifying users. Example: Allowing weak passwords or letting hackers guess passwords without limits.

8. **Software and Data Integrity Failures**  
   Failure to keep data and software safe from tampering. Example: Relying on untrusted sources for updates.

9. **Security Logging and Monitoring Failures**  
   Not tracking system activity well enough. Example: Failing to log failed login attempts, missing signs of attacks.

10. **Server-Side Request Forgery (SSRF)**  
   The server makes unsafe requests on behalf of a user. Example: Hackers trick the server into connecting to malicious sites.


---

## Task 8

> Is it okay to hardcode secrets such as database passwords in your application source code?

No, hardcoding secrets like database passwords in your application source code is not a good practice. This can expose your sensitive information to attackers, especially if the source code is shared or compromised. It increases the risk of accidental leaks (through version control systems like Git) and can lead to security breaches.


> How can you manage such secrets?

To securely manage secrets like database credentials, you can use a **Secret Management Solution**. Some common methods are:
- **Environment Variables**: Store secrets outside of the source code, typically in environment variables.
- **Encrypted Configuration Files**: Use encrypted files to store secrets and decrypt them at runtime.
- **Secrets Management Tools**: Use dedicated tools such as **HashiCorp Vault**, **AWS Secrets Manager**, or **Azure Key Vault**.



---


## Referneces:

[Refernece 1](https://www.tutorialspoint.com/apache_bench/apache_bench_testing_our_sample_application.htm)
[Refernece 2](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu)
[Refernece 3](https://flask-httpauth.readthedocs.io/en/latest/)
[Refernece 4](https://flask-limiter.readthedocs.io/en/stable/)
 -->
