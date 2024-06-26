from django.core.management.base import BaseCommand, CommandError

from ...utils import import_wordpress


class Command(BaseCommand):
    help = "Import given XML files exported from WordPress"

    def add_arguments(self, parser):
        parser.add_argument("wordpress_xml", nargs="+", type=str)

    def handle(self, *args, **options):
        for wordpress_xml in options["wordpress_xml"]:
            try:
                result = import_wordpress(wordpress_xml)
            except Exception as e:
                self.stderr.write(self.style.ERROR('Failed to import "{}": {}.'.format(wordpress_xml, e)))
                raise CommandError(e)
            if result["errors"]:
                self.stderr.write(self.style.ERROR("Failed to import {} items.".format(wordpress_xml)))
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully imported {authors} authors, {categories} categories, and {items} items from "{xml}".'.format(
                        **result, xml=wordpress_xml
                    )
                )
            )
