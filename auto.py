from dats.core.client import streamer

def response(streamer, recv_data):
	print('recv data : ' +  str(recv_data))

s = streamer(remote_model_url='192.168.0.2')
s.set_ffmpeg_flag(streamer.MACOS_FACETIME_PRESET)
s.set_model_respones_callback(response)
s.start()

