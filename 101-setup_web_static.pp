# 5. Puppet for setup

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

-> file { '/data':
  ensure  => directory
}

# create direcotries /data/web_static/shared/
-> file { '/data/web_static':
  ensure => directory
}

# create direcotries /data/web_static/shared/
-> file { '/data/web_static/shared':
  ensure => directory
}

# create direcotries /data/web_static/shared/
-> file { '/data/web_static/releases':
  ensure => directory
}

# create direcotries /data/web_static/shared/
-> file { '/data/web_static/releases/test':
  ensure => directory
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Holberton School'
}

-> exec { 'symbolik link':
  command  => 'ln -snf /data/web_static/releases/test/ /data/web_static/current',
  user     => 'root',
  provider => 'shell'
}

-> exec { 'Set permission':
  command  => 'chown -R ubuntu:ubuntu /data/',
  user     => 'root',
  provider => 'shell'
}
-> exec { 'Added location':
  command  => 'sed -i "48i location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}

-> exec { 'Start nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
