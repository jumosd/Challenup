from django.core.management.base import BaseCommand
import os , shutil
from django.conf import settings
from webtoon.models import Webtoon, upload_to_uid
from account.models import User



class Command(BaseCommand):
    help = '스크립트를 실행하는 사용자 정의 명령'

    def handle(self, *args, **options):

        webtoons = Webtoon.objects.all()



        for i in webtoons:
            author_id = i.author_id

            obj = User.objects.get(id=author_id)
            uid = obj.uid
            new_image_path = os.path.join(str(uid),i.image.name)
            new_thumbnail_path = os.path.join(str(uid),i.thumbnail.name)
      

            shutil.move(os.path.join(settings.MEDIA_ROOT,i.image.name),os.path.join(settings.MEDIA_ROOT))

            shutil.move(os.path.join(settings.MEDIA_ROOT,i.thumbnail.name),os.path.join(settings.MEDIA_ROOT))

            i.image = new_image_path
            i.thumbnail = new_thumbnail_path
            i.save()
        # print("완료")
