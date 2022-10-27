# Creating a user to login without password

user { 'root':
    ensure     => 'present',
    shell      => '/bin/bash',
    password   => '*',
}
