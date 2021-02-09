from websocket import create_connection

# test websocket connections

test_message = 'Тестовое сообщение из клиента'

ws = create_connection("ws://localhost:8888")
print("Эхо сообщение", test_message)
ws.send(test_message)
result = ws.recv()
print("Ответ сервера: '%s'" % result)
ws.close()