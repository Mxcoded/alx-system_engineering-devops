# Create a manifest that terminates a process called killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
