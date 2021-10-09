from json_views.views import JSONDataView
from rest_framework import permissions
from rest_framework.views import APIView

from Gameplay.logic import Gameplay


class ResetEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(NextEventView, self).get_context_data(**kwargs)
        Gameplay.reset()
        return dict(context, **{
            'message': 'OK'
        })

class NextEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(NextEventView, self).get_context_data(**kwargs)
        return dict(context, **{
            'text': 'продажа',
            'controls': {
                'min': 20,
                'max': 40,
            },
            'actions': [
                {'text': 'продать'},
                {'text': 'купить'},
            ],
        })
