# Using Puppet, install flask

exec { 'install_flask':
    command  => 'pip3 install flask==2.1.0',
    provider => shell,
}
