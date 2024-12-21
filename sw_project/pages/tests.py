from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import University, Scholarship

User = get_user_model()

class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password123')
        self.client.login(email='test@example.com', password='password123')

        self.universities = [
            University.objects.create(
                universityID=101,
                name="Test University 1",
                location="Location 1",
                about="About 1",
                website="https://www.testuni1.com",
                ranking=1
            ),
            University.objects.create(
                universityID=102,
                name="Test University 2",
                location="Location 2",
                about="About 2",
                website="https://www.testuni2.com",
                ranking=2
            ),
            University.objects.create(
                universityID=103,
                name="Test University 3",
                location="Location 3",
                about="About 3",
                website="https://www.testuni3.com",
                ranking=3
            ),
        ]

        self.scholarships = [
            Scholarship.objects.create(
                scholarshipID=11,
                name="Test Scholarship 1",
                about="Test About 1",
                amount=1000.0,
                short_description="Test Description 1"
            ),
            Scholarship.objects.create(
                scholarshipID=12,
                name="Test Scholarship 2",
                about="Test About 2",
                amount=2000.0,
                short_description="Test Description 2"
            ),
            Scholarship.objects.create(
                scholarshipID=13,
                name="Test Scholarship 3",
                about="Test About 3",
                amount=3000.0,
                short_description="Test Description 3"
            ),
        ]

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('universities', response.context)
        self.assertIn('scholarships', response.context)
        self.assertEqual(len(response.context['universities']), 3)  
        self.assertEqual(len(response.context['scholarships']), 3)  
    def test_profile_view(self):
        response = self.client.get(reverse('profile', args=[self.user.userID]))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_scholarship_details_view(self):
        scholarship = self.scholarships[0]  
        response = self.client.get(reverse('scholarship_details', args=[scholarship.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scholarship-details.html')
        self.assertEqual(response.context['scholarship'], scholarship)

    def test_scholarships_view(self):
        response = self.client.get(reverse('scholarships'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scholarships.html')
        self.assertIn('scholarships', response.context)
        self.assertEqual(len(response.context['scholarships']), 3) 

        response = self.client.get(reverse('scholarships') + '?query=Test')
        self.assertEqual(len(response.context['scholarships']), 3) 

        response = self.client.get(reverse('scholarships') + '?query=Nonexistent')
        self.assertEqual(len(response.context['scholarships']), 0) 

    def test_universities_view(self):
        response = self.client.get(reverse('universities'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'universities.html')
        self.assertIn('universities', response.context)
        self.assertEqual(len(response.context['universities']), 3) 

        response = self.client.get(reverse('universities') + '?query=Test')
        self.assertEqual(len(response.context['universities']), 3)  

        response = self.client.get(reverse('universities') + '?query=Nonexistent')
        self.assertEqual(len(response.context['universities']), 0)  

    def test_university_details_view(self):
        university = self.universities[0]  
        response = self.client.get(reverse('university_details', args=[university.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'university-details.html')
        self.assertEqual(response.context['university'], university)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        response = self.client.post(reverse('login'), {'email': 'test@example.com', 'password': 'password123'})
        self.assertRedirects(response, reverse('index'))

        response = self.client.post(reverse('login'), {'email': 'test@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Invalid email or password')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        response = self.client.post(reverse('signup'), {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        })
        self.assertEqual(User.objects.count(), 2) 
        self.assertRedirects(response, reverse('login'))  
