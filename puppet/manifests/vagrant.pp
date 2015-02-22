#
# puppet magic for dev boxes
#
import "classes/*.pp"

$PROJ_DIR = "/vagrant"
$HOME_DIR = "/home/vagrant"

Exec {
    path => "/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin",
}

class {
    init: ;
    python_setup:;
    ohmyzsh_setup:;
    docker:
        extra_parameters => "--registry-mirror=http://10.0.0.2:5000",
        require => Class[init];
    samba_share: require => Class[init];
}


