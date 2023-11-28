# Creates a manifest that kills a process killmenow

exec { 'pkill killmenow':
  path      => '/usr/bin',
  command   => 'pkill killmenow',
  provider  => shell,
  returns   => [0, 1]
}
