ubuntu_docker
=============

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/ubuntu_docker.git

About
-----

This project provides a [Ubuntu (14.04)][2] [Vagrant][3] Virtual Machine (VM)
with [Docker][4] containers to host [IPython notebook][5] servers.

[2]: http://releases.ubuntu.com/14.04/
[3]: http://www.vagrantup.com/
[4]: https://www.docker.com/
[5]: http://ipython.org/notebook.html

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

3. Go to the IPython notebook Docker container directory

    ```bash
    cd /vagrant/docker/ipython
    ```

4. Build the IPython notebook Docker container

    ```bash
    sudo fig build notebook
    ```

5. Run the IPython notebook Docker container

    ```bash
    sudo fig up -d notebook
    ```

6. To view the running containers

    ```bash
    sudo fig ps
    ```

7. Open the browser to the IPython notebook page
http://localhost:PORT_IN_STEP_6/


8. To see the logs from the IPython notebook container

    ```bash
    sudo fig logs notebook
    ```

9. To stop display of the logs type `Ctrl+C`.

10. To stop the Docker IPython notebook container

    ```bash
    sudo fig kill notebook
    ```
11. To remove the notebook Docker container

    ```bash
    sudo fig rm notebook
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

