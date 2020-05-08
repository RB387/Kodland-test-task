from django.test import TestCase
from .models import Post
from django.utils import timezone
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class BlogTest(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(title='title-text',
                                        text='body-text',
                                        published_date=timezone.now())

    def test_post_content(self):
        post = Post.objects.get(title='title-text')
        self.assertEqual(post.text, 'body-text')

    def test_blog_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'body-text')
        self.assertTemplateUsed(response, 'home.html')

    def test_add_post_view(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

