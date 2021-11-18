from DirtRally2 import DirtRally2Decoder

game = DirtRally2Decoder(3)
game.open_game('127.0.0.1', '20777')

for i in range(0, 10):
    arr = game.sample_game(['speed', 'engine_rate', 'throttle_input'])

    if arr is not None:
        arr['speed'] = int(arr['speed'] * 2.23694)
        arr['engine_rate'] = int(arr['engine_rate'] * 10)
        arr['throttle_input'] = int(arr['throttle_input'] * 100)

        print(arr)

game.close_game()