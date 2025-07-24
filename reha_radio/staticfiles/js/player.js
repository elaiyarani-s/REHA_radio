document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("audioPlayer");
    const label = document.getElementById("now-playing-label");
    const streamTitle = document.getElementById("stream-title");

    function updateStatus(statusText) {
        label.textContent = statusText;
    }

    audio.addEventListener("playing", () => {
        updateStatus("🎵 Now Playing: " + stationName);
    });

    audio.addEventListener("pause", () => {
        updateStatus("⏸️ Paused");
    });

    audio.addEventListener("waiting", () => {
        updateStatus("⌛ Buffering...");
    });

    audio.addEventListener("error", () => {
        updateStatus("❌ Error playing stream.");
    });

    // Fetch stream metadata using ICY headers (some servers support this)
    function fetchStreamMetadata() {
        fetch(streamUrl, {
            method: 'GET',
            headers: {
                'Icy-MetaData': '1'
            }
        }).then(response => {
            const icyMeta = response.headers.get("icy-name") || response.headers.get("icy-description");
            if (icyMeta) {
                streamTitle.textContent = "📝 " + icyMeta;
            }
        }).catch(error => {
            console.log("Metadata fetch error:", error);
        });
    }

    // Try to fetch metadata every 30 seconds
    setInterval(fetchStreamMetadata, 30000);
    fetchStreamMetadata();
});
    