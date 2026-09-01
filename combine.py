import urllib.request

EXTERNAL_M3U = "https://raw.githubusercontent.com/ryansnetcafe/ott-playlist/refs/heads/main/ryansnetcafe.m3u"

LOCAL_M3U = "my_channels.m3u"
OUTPUT_M3U = "combined.m3u"

def download(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")

local = open(LOCAL_M3U, "r", encoding="utf-8").read()
external = download(EXTERNAL_M3U)

# Remove #EXTM3U from external playlist
external = external.replace("#EXTM3U", "", 1).strip()

combined = local.rstrip() + "\n" + external + "\n"

open(OUTPUT_M3U, "w", encoding="utf-8").write(combined)

print("Playlist updated successfully.")
