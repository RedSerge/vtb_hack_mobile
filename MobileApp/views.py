from django.http import HttpResponse
from json_views.views import JSONDataView
from rest_framework import permissions
from rest_framework.views import APIView
import json

from Gameplay.logic import (
    Gameplay as Game,
    START_CASH,
)


class ResetEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(ResetEventView, self).get_context_data(**kwargs)
        Game.reset()
        return dict(context, **{
            'message': 'OK'
        })


class NextEventView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(NextEventView, self).get_context_data(**kwargs)
        success = Game.active_player.run()
        if not success and Game.active_player.event_type == 0:
            Game.active_player.restful = {
                "error": f"Игра закончилась, вы {'выиграли' if Game.active_player.cash > START_CASH else 'проиграли'}",
            }
        return dict(context, **Game.active_player.restful)


class StatusView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        return dict(context, **{
            'money': Game.active_player.cash,
            'statistics': Game.active_player.history_stats,
            'history': Game.active_player.history_deeds,
        })


class SelectOkView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        if Game.active_player.event_type == 1:
            Game.active_player.event_type = 0
            Game.active_player.event_response = 1
        context = super(SelectOkView, self).get_context_data(**kwargs)
        return dict(context, **{})


class SelectCancelView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        if Game.active_player.event_type == 1:
            Game.active_player.event_type = 0
            Game.active_player.event_response = 0
        context = super(SelectCancelView, self).get_context_data(**kwargs)
        return dict(context, **{})


class SelectSellView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if Game.active_player.event_type == 2:
            value = int(self.request.GET.get('value', ''))
            Game.active_player.event_type = 0
            Game.active_player.event_response = [value, False]
        return HttpResponse()


class SelectBuyView(JSONDataView, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if Game.active_player.event_type == 2:
            value = int(self.request.GET.get('value', ''))
            Game.active_player.event_type = 0
            Game.active_player.event_response = [value, True]
        return HttpResponse()
