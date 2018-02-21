from django.test import TestCase

from .models import Agenda

class ModelTestCase(TestCase):

    def setUp(self):
        self.bucketlist_descricao = "Write world class code"
        self.bucketlist = Agenda(descricao=self.bucketlist_descricao)

    def test_model_can_create_a_agenda(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Agenda.objects.count()
        self.bucketlist.save()
        new_count = Agenda.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        agenda = Agenda.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': agenda.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Agenda.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)