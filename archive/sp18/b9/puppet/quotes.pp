package { '': }

group { 'quotegather':
  ensure  => '',
}

user { 'quotes':
  ensure  => '',
  gid     => ,
  home    => '',
  shell   => '',
  require => Group['quotegather'],
}

cron { 'getquote':
  user     => '',
  command  => "curl -X POST http://api.forismatic.com/api/1.0/ -d 'method=getQuote' -d 'format=text' -d 'lang=en' >> quotes && echo >> quotes",
  minute   => '',
}
