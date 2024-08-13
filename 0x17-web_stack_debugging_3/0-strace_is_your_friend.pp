# Puppet script to fixe a typo in the WordPress configuration file

exec { 'Fix wp-settings.php':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin:/sbin',
}