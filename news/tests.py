from django.test import TestCase
from models import Editor,Article,tags 

# Create your tests here.
class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
      self.sammy= Editor(first_name='Sammy',last_name='Mutua',email='sammymbevi@gmail.com')

    #Test Instance
    def test_instance(self):
      self.assertTrue(isinstance(self.sammy,Editor))

    #Testing Save Method
    def test_save_method(self):
      self.sammy.save_editor()
      editors = Editor.objects.all()
      self.assertTrue(len(editors)>0)
