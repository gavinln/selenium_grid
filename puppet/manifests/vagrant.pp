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
    docker: require => Class[init];
    samba_share: require => Class[init];
}


