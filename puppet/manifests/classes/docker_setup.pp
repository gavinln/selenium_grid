# install docker
class docker_setup {
    class { 'docker':
    }
    user {'vagrant':
        ensure => 'present'
    }
    exec {"vagrant_in_docker":
      unless => "grep -q 'docker\\S*vagrant' /etc/group",
      command => "usermod -aG docker vagrant",
      require => [User['vagrant'], Class['docker']]
    }
}


