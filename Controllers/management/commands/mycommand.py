from django.core.management.base import BaseCommand , CommandError

class Command(BaseCommand):
	help = "Welcom To Help Section Of This Command !"
	def add_arguments(self , parser):
		parser.add_argument("first" , type=int , help="This Argument Should Less 100 And Be A Integer")
		parser.add_argument("-option1" , type=str , default="Default Value" , help="This Argument Is Optional")
	def handle(self , *args , **options):
		if options['first'] < 100:
			self.stdout.write(self.style.SUCCESS('Greate Job !'))
		else:
			raise CommandError('The Number is Grater Than 100')
