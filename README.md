The EML file extension is an acronym for E-mail and created by Microsoft Corporation. 
EML files are stored email messages in plain text formats. 

SQL -DATABASE Creation :
sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY '';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;


 To start the DATABASE 
 /usr/bin/mysql -u sai



