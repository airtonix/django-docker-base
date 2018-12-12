from django.urls import include, path
from django.conf.urls import url

from polls.api import QuestionResource

urlpatterns = [
    # The usual suspects, then...

    url(r'^questions/', include(QuestionResource.urls())),
]