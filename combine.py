import urllib.request

EXTERNAL_M3U_1 = "https://raw.githubusercontent.com/ryansnetcafe/ott-playlist/refs/heads/main/ryansnetcafe.m3u"
EXTERNAL_M3U_2 = "https://cdn.djdoolky76.net/udptv/phc-free.m3u"

LOCAL_M3U = "my_channels.m3u"
OUTPUT_M3U = "combined.m3u"


def download(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def clean_playlist(playlist):
    return playlist.replace("#EXTM3U", "", 1).strip()


local = open(LOCAL_M3U, "r", encoding="utf-8").read()

external_1 = download(EXTERNAL_M3U_1)
external_2 = download(EXTERNAL_M3U_2)

external_1 = clean_playlist(external_1)
external_2 = clean_playlist(external_2)

combined = (
    local.rstrip()
    + "\n"
    + external_1
    + "\n"
    + external_2
    + "\n"
)

open(OUTPUT_M3U, "w", encoding="utf-8").write(combined)

print("Playlist updated successfully.")
