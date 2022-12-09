# Create a file in /tmp

file {
  ensure  => 'present',
  content => 'I love Pupper',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school'
}
