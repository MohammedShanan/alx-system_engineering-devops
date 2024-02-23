# Using Puppet, install flask

# Using Puppet, install flask from pip3
exec{ 'flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}

package { 'flask'
    ensure: installed
}