CREATE TABLE
    IS601_PlaylistTracks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        playlist_id INT,
        track_id INT,
        tracks INT DEFAULT 1,
        FOREIGN KEY (playlist_id) REFERENCES IS601_Playlists(id),
        FOREIGN KEY (track_id) REFERENCES IS601_Tracks(id),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE (playlist_id, track_id),
        -- enforces UNIQUE pairs
        check(tracks > 0)
    );