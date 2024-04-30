import logging

from application import Application


# Set logging level
logging.basicConfig(level=logging.DEBUG)


def main():
	app = Application()
	app.run()


if __name__ == '__main__':
	main()
