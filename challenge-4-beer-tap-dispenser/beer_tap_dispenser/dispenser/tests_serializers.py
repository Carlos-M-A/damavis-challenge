from django.test import TestCase
from dispenser.models import  Dispenser, Usage
from dispenser.serializers import DispenserSerializer, DispenserStatusSerializer, DispenserSerializerCreation, UsageSerializer

class UsageSerializerTestCase(TestCase):
    def setUp(self):
        dispenser = Dispenser(flow_volume=2)
        dispenser.save()
        self.usage = Usage()
        self.usage.opened_at = "2023-01-01T10:00:00Z"
        self.usage.flow_volume = 2
        self.usage.total_spent = 0
        self.usage.dispenser = dispenser
        self.usage.save()
    
        self.usage_serializer = UsageSerializer(self.usage)
    

    def test_OK(self):
        self.assertEqual(self.usage_serializer.data['opened_at'], "2023-01-01T10:00:00Z")
        self.assertIsNone(self.usage_serializer.data['closed_at'])
        self.assertEqual(self.usage_serializer.data['flow_volume'], 2)
        self.assertEqual(self.usage_serializer.data['total_spent'], 0)

class DispenserSerializerTestCase(TestCase):
    def setUp(self):
        self.dispenser = Dispenser(flow_volume=2)
        self.dispenser.save()
        self.usage = Usage()
        self.usage.opened_at = "2023-01-01T10:00:00Z"
        self.usage.opened_at = "2023-01-01T10:00:10Z"
        self.usage.flow_volume = 2
        self.usage.total_spent = 20 * Dispenser.BEER_PRICE_PER_LITRE
        self.usage.dispenser = self.dispenser
        self.usage.save()
        self.usage = Usage()
        self.usage.opened_at = "2023-01-01T10:00:00Z"
        self.usage.flow_volume = 2
        self.usage.total_spent = 0
        self.usage.dispenser = self.dispenser
        self.usage.save()

        self.dispenser_serializer = DispenserSerializer(self.dispenser)

    def test_OK(self):
        self.assertEqual(self.dispenser_serializer.data['amount'], 20*Dispenser.BEER_PRICE_PER_LITRE)
        self.assertEqual(self.dispenser_serializer.data['usages'][0]['flow_volume'], 2)

class DispenserSerializerCreationTestCase(TestCase):
    def setUp(self):
        self.dispenser = Dispenser(flow_volume=2)
        self.dispenser.save()
        self.dispenser_serializer = DispenserSerializerCreation(self.dispenser)

    def test_OK(self):
        self.assertEqual(self.dispenser_serializer.data['id'], str(self.dispenser.unique_id))
        self.assertEqual(self.dispenser_serializer.data['flow_volume'], 2)

class DispenserStatusSerializerTestCase(TestCase):
    def setUp(self):
        self.data = {"status":"open", "updated_at":"2023-01-01T10:00:00Z"}

        self.dispenser = Dispenser(flow_volume=2)
        self.dispenser.save()

        self.dispenser_serializer = DispenserStatusSerializer(self.dispenser, data=self.data)
    
    def test_OK(self):
        self.assertTrue(self.dispenser_serializer.is_valid())
    
        self.dispenser_serializer.save()

        data = {"status":"close", "updated_at":"2023-01-01T10:00:10Z"}
        self.dispenser_serializer = DispenserStatusSerializer(self.dispenser, data=data)
        self.assertTrue(self.dispenser_serializer.is_valid())

        self.dispenser_serializer.save()

        data = {"status":"close", "updated_at":"2023-01-01T10:00:10Z"}
        self.dispenser_serializer = DispenserStatusSerializer(self.dispenser, data=data)
        self.assertFalse(self.dispenser_serializer.is_valid())

