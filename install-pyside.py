import subprocess
import platform
import click

from sys import exit

if platform.system() != 'Linux': exit("Not linux")

distro, version, dname = platform.linux_distribution()
elementary_freya = (dname == 'freya')
ubuntu_trusty = ('14.04' in version) or elementary_freya


@click.command()
@click.confirmation_option(prompt="Do you want to install it?", help="Install pySide")
def install():

	if ubuntu_trusty:
		subprocess.call("sudo apt-get install python3-pyside", shell=True)
	else:
		click.echo("Not install supported for {}-{}-{}".format(distro, dname, version))
		exit()

if __name__ == '__main__':
	
	install()
