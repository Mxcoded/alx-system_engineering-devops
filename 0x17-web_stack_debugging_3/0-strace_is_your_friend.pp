# Fix error 500 on Apache web server to address HTTP GET request

exec {'wordpress-fix':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
