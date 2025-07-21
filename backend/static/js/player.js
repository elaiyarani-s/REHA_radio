document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("audioPlayer");
    const label = document.getElementById("now-playing-label");
    const streamTitle = document.getElementById("stream-title");

    // Show playback status
    function updateStatus(statusText) {
        label.textContent = statusText;
    }

    // Local notification (only if running in Capacitor environment)
    async function showNowPlayingNotification() {
        if (window.Capacitor && Capacitor.isNativePlatform()) {
            const { LocalNotifications } = await import('@capacitor/local-notifications');

            await LocalNotifications.requestPermissions(); // Ask permission first

            await LocalNotifications.schedule({
                notifications: [
                    {
                        title: "Now Playing",
                        body: stationName + " is streaming",
                        id: 1,
                        schedule: { at: new Date(Date.now() + 1000) }
                    }
                ]
            });
        }
    }

    // Playback events
    audio.addEventListener("playing", () => {
        updateStatus("🎵 Now Playing: " + stationName);
        showNowPlayingNotification();
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

    // Stream metadata (ICY headers)
    function fetchStreamMetadata() {
        fetch(streamUrl, {
            method: 'GET',
            headers: {
                'Icy-MetaData': '1'
            }
        })
        .then(response => {
            const icyMeta = response.headers.get("icy-name") || response.headers.get("icy-description");
            if (icyMeta) {
                streamTitle.textContent = "📝 " + icyMeta;
            }
        })
        .catch(error => {
            console.log("Metadata fetch error:", error);
        });
    }

    // Metadata refresh every 30 seconds
    setInterval(fetchStreamMetadata, 30000);
    fetchStreamMetadata();
});
