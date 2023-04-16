# Banzer

Banzer is a small vehicle built as a project for UNI. It is operated by a Raspberry Pi 3 Model B+ from 2017.

## Features

- **Badass:** Banzer has a cool and impressive design.
- **Fast:** It can move quickly and efficiently.
- **Smart:** It uses advanced technology to perform tasks.
- **Etc:** There are many other great features that Banzer offers.

## Installation



### Dependencies

Banzer requires the following libraries to be installed:

- **WiringPi:** This library can be downloaded from the official [WiringPi repository](https://github.com/WiringPi/WiringPi).
Alternatively to download and build  the library, use the following commands:

  ```bash
  $ git clone https://github.com/WiringPi/WiringPi.git
  $ cd WiringPi
  $ git pull origin
  $ ./build
  
- **RSi.GPIO:** pre-installed in the PI_OS

- **Pytorch:** This library can be downloaded from the official [Pytorch webpage](https://pytorch.org/).

## Usage
Control Banzer ...

## Configuration
### Instructions 
To make the Pi run the driver 'program' at boot we used a bash script for compiling/building and runing the Program excutable to automate the process then created a linux service to run the command at boot.


To create the linux service do the following:\
Go to the folder located at

```bash
/etc/systemd/system/
```

Create a foo.service file and open it for edit.


If ur programming on the Pi just run:

```bash
$ sudo nano /etc/systemd/system/foo.service
```

Replace foo with an appropriate task name.

Next copy the following code to ur foo.service file 

```markdown
[Unit]
Description=driver

[Service]
ExecStart=/home/user/path/to/my/driver
Restart=on-failure
Restartsec=30s
User=root

[Install]
WantedBy=multi-user.target
```
After saving the changes and exiting the nano text editor run the following command to reload the systemd 

```bash
$ sudo systemctl daemon-reload
```
To enable the service to run at boot run 

```bash
$ sudo systemctl enable foo.service
```
To make sure the file has the correct permission to run at boot run

```bash
$ sudo chmod 644 /etc/systemd/system/foo.service
```

Then
```bash
$ sudo chown root:root /etc/systemd/system/foo.service
```



## License
TBD

## Contact
missing.

