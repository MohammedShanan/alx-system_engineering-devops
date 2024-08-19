# Puppet manifest to increase the file descriptor limit for Nginx

exec { 'replace_file_descriptor_limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart_nginx_service'],
}


exec { 'restart_nginx_service':
  provider => shell,
  command  => 'sudo service nginx restart',
}
