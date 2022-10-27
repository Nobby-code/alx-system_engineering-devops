# Creating a user to login without password

exec{ 'echo "PasswordAuthentiication no\nIdentifyFile ~/.ssh/school" >> /etc/ssh/ssh_config':
	path => '/bin/'
}
