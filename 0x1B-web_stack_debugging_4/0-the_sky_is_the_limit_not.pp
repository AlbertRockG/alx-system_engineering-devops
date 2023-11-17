# Fix problem of high amount of requests supported by nginx

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {
  provider => shell,
  command  => 'sudo service nginx restart',
}