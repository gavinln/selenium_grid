# Commands to run before all others in puppet.
class init {
    group { "puppet":
        ensure => "present",
    }
    case $operatingsystem {
        ubuntu: {
            exec { "apt-update":
                command => "sudo apt-get update",
            }
            Exec["apt-update"] -> Package <| |>
            $misc_packages = ['git-core']
            package { $misc_packages:
                ensure => present,
            }
        }
    }
    file { "/var/jenkins_home":
        ensure => "directory",
        owner  => "root",
        group  => "root",
        mode   => 777,
    }
}
