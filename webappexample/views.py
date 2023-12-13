import json
import os
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

import requests

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "user_id": request.session.get("user_id"),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    auth0_userid = token.get("userinfo").get("sub")
    request.session["user_id"] = auth0_userid
    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def userhub_callback(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect(request.build_absolute_uri(reverse("index")))
 
    api_url = "https://api.userhub.com/admin/v1"
    api_key = os.environ["USERHUB_ADMIN_API_KEY"]
    connection_id = os.environ["USERHUB_USERS_PROVIDER_CONNECTION_ID"]
    portal_url = request.GET["portalUrl"]
 
    res = requests.post(
        url=f"{api_url}/users/{user_id}@{connection_id}:createPortalSession",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"portalUrl": portal_url},
    )
    res.raise_for_status()
    res_data = res.json()
 
    return redirect(res_data["redirectUrl"])

def userhub_webhook(request):
    action = request.GET.get("action")
    if action == "challenge":
        data = json.loads(request.body)
        return JsonResponse(data, status=200)
    return JsonResponse({}, status=400)



