import asyncio
from songtracker import SongTracker


async def main() -> None:
    tracker = SongTracker()
    old_song = {"title": "None", "artist": "None"}
    while True:
        if await tracker.get_new_session():
            await tracker.update_current_song()
            if tracker.current_song:
                if (
                    tracker.current_song["title"] != old_song["title"]
                    or tracker.current_song["artist"] != old_song["artist"]
                ):
                    print(tracker.current_song)
                    old_song = tracker.current_song


asyncio.run(main())
