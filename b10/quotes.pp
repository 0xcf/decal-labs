package { '': } # What package is required for this script to run?

group { 'quotegather':
  ensure  => '', # Do we want the group on this system?
}
user { 'quotes':
  ensure  => '', # Do we want the user on this system?
  gid     => , # Note that we can pass a group name to gid
  home    => '',
  shell   => '',
  # Do not create the user quotes unless the quotegather group exists
  require => Group['quotegather'],
}


cron { 'getquote':
  user     => '', # Which user do we want to run this cron job?
  # You can ignore this, it pulls the quotes from an API and appends
  # them to a file.
  command  => "curl 'https://api.kanye.rest/?format=text' >> quotes && echo >> quotes",
  minute   => '', # Hint: passing * means this runs every minute
}
