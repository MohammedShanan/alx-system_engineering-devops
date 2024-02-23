# Using Puppet, install flask

package { 'flask':
    ensure   => 'installed',
    provider => 'pip3',
}
