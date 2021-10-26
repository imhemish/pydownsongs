from youtube_dl import YoutubeDL as ytdl_base
import shutil

def download_module(linkofsong, inputquery, qualitylevel):
    opts = {
        "format": "bestaudio/best",
        "quiet": False,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    with ytdl_base(opts) as ytdl:
        ytdl.download([linkofsong])
        info = ytdl.extract_info(linkofsong, download=False)
        title = info["title"]
        title = title.replace("|", "_")
        id = info["id"]
        filename = title+"-"+id+".mp3"
        shutil.move(filename, (inputquery.title()+".mp3"))