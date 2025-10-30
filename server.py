import os
from livekit import api
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
from livekit.api import LiveKitAPI, ListRoomsRequest
import uuid

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


async def generate_room_name():
    name = "room-" + str(uuid.uuid4())[:8]
    rooms = await get_rooms()
    while name in rooms:
        name = "room-" + str(uuid.uuid4())[:8]
    return name


async def get_rooms():
    api_client = LiveKitAPI()
    rooms = await api_client.room.list_rooms(ListRoomsRequest())
    await api_client.aclose()
    return [room.name for room in rooms.rooms]


@app.route("/getToken")
async def get_token():
    name = request.args.get("name", "my name")
    room = request.args.get("room", None)

    if not room:
        room = await generate_room_name()

    token = api.AccessToken(os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_API_SECRET")) \
        .with_identity(name)\
        .with_name(name)\
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room
        ))

    return token.to_jwt()

from backend.server import *  # re-export moved backend implementation