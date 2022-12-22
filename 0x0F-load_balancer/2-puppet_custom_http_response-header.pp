# Installs a Nginx server with custome HTTP header
include stdlib

exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec { 'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

file_line { 'add_header':
  ensure      => present,
  path        => '/etc/nginx/sites-available/default',  
  line        => '\nadd_header X-Served-By $HOSTNAME',
  match       => '^listen       [::]:80',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
