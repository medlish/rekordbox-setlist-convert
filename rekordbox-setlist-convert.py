class Track:
    def __init__(self, track_number, title, performer, file, index):
        self.track_number = track_number
        self.title = title
        self.performer = performer
        self.file = file
        self.index = index

def read_tracks(file_path):
    tracks = []

    with open(file_path, 'r') as f:
        # Skip the first 5 lines
        for _ in range(5):
            next(f)

        # Read in 5 lines at a time
        while True:
            try:
                # Skip the first word on each line
                track_number = next(f).strip().split(None, 1)[1]
                title = next(f).strip().split(None, 1)[1]
                performer = next(f).strip().split(None, 1)[1]
                file = next(f).strip().split(None, 1)[1]
                index = next(f).strip().split(None, 1)[1]

                # Ignore blank lines
                if track_number and title and performer and file and index:
                    track = Track(track_number, title, performer, file, index)
                    tracks.append(track)
            except StopIteration:
                break

    return tracks
    
def write_tracks(tracks, file_path):
    with open(file_path, 'w') as f:
        for track in tracks:
            f.write(f"{track.performer} - {track.title}\n")

# Example usage
tracks = read_tracks('01 REC-2022-12-17.cue')
write_tracks(tracks, 'output_file.txt')