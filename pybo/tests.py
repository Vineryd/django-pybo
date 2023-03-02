from django.test import TestCase

# Create your tests here.
<<<<<<< HEAD

from pybo.models import Question
from django.utils import timezone

for i in range(300):
    q = Question(
        subject = f'테스트 데이터입니다: [{i:03d}]',
        content = f'테스트 데이터의 내용입니다: [{i:03d}]',
        create_date = timezone.now()
    )
    q.save()


=======
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274
