from json_views.views import JSONDataView
from rest_framework import permissions
from rest_framework.views import APIView

from Gameplay.logic import Gameplay as Game


class ResetEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(NextEventView, self).get_context_data(**kwargs)
        Game.reset()
        return dict(context, **{
            'message': 'OK'
        })


class NextEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(NextEventView, self).get_context_data(**kwargs)
        success = Game.active_player.run()
        if not success:
            Game.active_player.restful = {
                "error": "Игра-то закончилась"
            }
        return dict(context, **Game.active_player.restful)


class StatusView(JSONDataView, APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        return dict(context, **{})
