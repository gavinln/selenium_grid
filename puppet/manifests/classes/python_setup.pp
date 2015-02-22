# install python
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { "python-pip":
                ensure => installed
            }
            package { 'fig':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'selenium':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'fabric':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
