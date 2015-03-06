ubuntu_docker
=============

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/selenium_grid.git

About
-----

This project provides a [Ubuntu (14.04)][2] [Vagrant][3] Virtual Machine (VM)
with [Docker][4] containers to host a [Selenium Grid][5] with Chrome.

[2]: http://releases.ubuntu.com/14.04/
[3]: http://www.vagrantup.com/
[4]: https://www.docker.com/
[5]: https://code.google.com/p/selenium/wiki/Grid2

There are [Puppet][6] scripts that automatically install the software when the VM is started.

[6]: http://puppetlabs.com/

Running
-------

1. To start the virtual machine(VM) type

    ```
    vagrant up
    ```

2. Connect to the VM

    ```
    vagrant ssh
    ```

3. Go to the Selenium Docker container directory

    ```bash
    cd /vagrant/docker/selenium
    ```

4. Pull the latest Selenium images

    ```bash
    sudo fig pull
    ```

5. Change to the Python driver program directory

    ```bash
    cd /vagrant/python
    ```

6. Start the Selenium grid (hub & node)

    ```bash
    fab grid_start
    ```

7. Open VNC to 192.168.33.10:5900 (password: secret)

8. Open the browser to http://192.168.33.10:4444/grid/console

9. Run the Selenium test (takes about 5 seconds). Refresh the browser in step
   8 to see the available webdriver being used when the test is run.

    ```bash
    fab run_test
    ```

10. Stop the Selenium grid (hub & node)

    ```bash
    fab grid_stop
    ```

11. Start Selenium standalone instance

    ```bash
    fab standalone_start
    ```

12. Open the browser to http://192.168.33.10:4444/wd/hub


13. Run the Selenium test (takes about 5 seconds). Click the "Refresh sessions"
button to see the sessions started.

    ```bash
    fab run_test
    ```

14. Stop the Selenium standalone instance

    ```bash
    fab standalone_stop
    ```

15. Type `exit` to quit the virtual machine

16. To halt the VM type (fast to startup after a halt command)

    ```
    vagrant halt
    ```

17. To destroy the VM (slow to create VM after a destroy command)

    ```
    vagrant destroy
    ```

Requirements
------------

The following software is needed to get the software from github and run
Vagrant. The Git environment also provides an [SSH client][7] for Windows.

* [Oracle VM VirtualBox][8]
* [Vagrant][9]
* [Git][10]

[7]: http://en.wikipedia.org/wiki/Secure_Shell
[8]: https://www.virtualbox.org/
[9]: http://vagrantup.com/
[10]: http://git-scm.com/

