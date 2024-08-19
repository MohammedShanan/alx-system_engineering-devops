# Puppet manifest to increase the open files limit for users

exec { 'increase_nofile_soft_limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['increase_nofile_hard_limit'],
  unless   => 'grep -q "nofile 50000" /etc/security/limits.conf',
}

exec { 'increase_nofile_hard_limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  unless   => 'grep -q "nofile 40000" /etc/security/limits.conf',
}