from django.core.management.base import BaseCommand
from api.models import Step

# ==============================================================================
class Command(BaseCommand):
    help = "Populate chat steps into the DB"

    # ------------------------------------------------------------------------------
    def handle(self, *args, **options):

        steps = {
            'greeting': {'response_message': 'Hello! Hope you are having a wonderful day', 'next_state': 'question'},
            'question': {'response_message': 'Would you like to me to tell you a joke? (yes/no)', 'next_state': 'answer'},
            'answer': {'response_message': 'You run in front of a car, you get tired. You run at the back of a car, you get exhausted.', 'next_state': 'end'},
            'end': {'response_message': 'Thank you for chatting! Cheers!', 'next_state': None},
        }

        for step_name, step_data in steps.items():
            Step.objects.create(
                name=step_name,
                response_message=step_data['response_message'],
                next_state=step_data.get('next_state', None)
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the Step entries.")
        )
