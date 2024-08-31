from tiktokvoice import tts
import moviepy.editor as mp
import random

class Video_controller:
    def __init__(self, text):
        self.text = text
        self.audio_filename = "tts.mp3"

    def make_video(self):
        
        # make tts and make sure its worked before creating the video
        if self.make_audio():
            pass
        else:
            return False

        # load video and audio
        video = mp.VideoFileClip("gameplay.webm")
        audio = mp.AudioFileClip("tts.mp3")

        # crop video to random 1 minute section
        video_duration_value = video.duration
        start_time = random.uniform(0, video_duration_value)
        video_clip = video.subclip(start_time, start_time + 60)

        # remove existing audio
        video_clip = video_clip.without_audio()

        # crop audio and overlay onto video
        audio_clip = audio.subclip(0, 60)
        final_video = video_clip.set_audio(audio_clip)

        # export video
        final_video.write_videofile("output.webm", codec="libvpx-vp9", audio_codec="libvorbis")


    def make_audio(self):
        try:
            # here change text however you want, maybe censor curse words
            formatted_text = self.text.replace("AITA", "Am I in the wrong")

            # run the function to create the mp3
            tts(formatted_text, "en_us_006", self.audio_filename)
            return True
        except:
            return Exception

    def delete_video(self):
        ''

    def delete_audio(self):
        ''

