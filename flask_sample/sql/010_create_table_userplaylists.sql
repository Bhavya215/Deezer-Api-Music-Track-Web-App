CREATE TABLE
    IS601_UserPlaylists(
        id int auto_increment PRIMARY KEY,
        playlist_id int not null,
        user_id int not null,
        is_active tinyint(1) default 1,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES IS601_Users(id),
        FOREIGN KEY(playlist_id) REFERENCES IS601_Playlists(id),
        UNIQUE KEY (user_id, playlist_id)
    )