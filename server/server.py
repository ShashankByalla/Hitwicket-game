# server/server.py

import asyncio
import websockets
import json
from game_logic import Game

game = Game()

async def handler(websocket, path):
    player = game.players[game.turn]
    await websocket.send(json.dumps({"message": f"{player}'s turn"}))

    async for message in websocket:
        data = json.loads(message)
        x, y = data['x'], data['y']
        success, winner = game.make_move(x, y, player)

        if success:
            board_state = game.get_board()
            if winner:
                await websocket.send(json.dumps({"message": f"{winner} wins!", "board": board_state}))
            else:
                player = game.next_turn()
                await websocket.send(json.dumps({"message": f"{player}'s turn", "board": board_state}))
        else:
            await websocket.send(json.dumps({"message": "Invalid move, try again"}))

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
