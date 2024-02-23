# Using Puppet, install flask

package { 'Flask':
    ensure   => 'installed',
    provider => 'pip3',
    install_options => ['2.1.0'],
}
