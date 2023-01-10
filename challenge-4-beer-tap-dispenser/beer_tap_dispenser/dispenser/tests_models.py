from django.test import TestCase
from dispenser.models import  Dispenser, Usage
import datetime

class DispenserTestCase(TestCase):

    def test_OK_dispenser_with_no_usages(self):
        dispenser = Dispenser()
        dispenser.flow_volume = 1
        dispenser.save()

        self.assertEqual(dispenser.amount, 0)
        self.assertEqual(dispenser.status, "close")
        self.assertIsNone(dispenser.updated_at)

    def test_OK(self):
        dispenser = Dispenser()
        dispenser.flow_volume = 1
        dispenser.save()

        usage = Usage()
        usage.opened_at = datetime.datetime(2023,1,1,10,0,0)
        usage.closed_at = datetime.datetime(2023,1,1,10,0,10)
        usage.flow_volume = 1
        usage.total_spent = 122.5
        usage.dispenser = dispenser
        usage.save()

        usage = Usage()
        usage.opened_at = datetime.datetime(2023,1,1,10,0,0)
        usage.closed_at = datetime.datetime(2023,1,1,10,0,20)
        usage.flow_volume = 1
        usage.total_spent = 245
        usage.dispenser = dispenser
        usage.save()

        self.assertEqual(dispenser.amount, 367.5)
        self.assertEqual(dispenser.status, "close")
        

        usage = Usage()
        usage.opened_at = datetime.datetime(2023,1,1,11,11,11)
        usage.flow_volume = 1
        usage.dispenser = dispenser
        usage.save()

        self.assertEqual(dispenser.amount, 367.5)
        self.assertEqual(dispenser.status, "open")
