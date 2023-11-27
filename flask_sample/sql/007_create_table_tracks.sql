CREATE TABLE
    IS601_Tracks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        track_id BIGINT NOT NULL,
        readable BOOL,
        title VARCHAR(100) NOT NULL,
        title_short VARCHAR(50),
        track_link VARCHAR(100),
        duration INT NOT NULL,
        track_rank INT,
        artist_name VARCHAR(80),
        album_name VARCHAR(50),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY `title_track_id` (
            `track_id`,
            `title`
        )
    );
