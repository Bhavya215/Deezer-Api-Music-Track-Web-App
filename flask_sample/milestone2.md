<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Bhavya Amish Shah (bs635)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 7:07:16 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/bs635" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <div>Deezer API</div>API - <a href="https://rapidapi.com/deezerdevs/api/deezer-1">Link</a><div>Documentation about the API - <a href="https://rapidapi.com/blog/deezer-api-with-java-python-php-ruby-javascript-examples/">Link</a></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <p>I will be using GET * Search endpoint.<div>It gives me data related to<br>the song tracks.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div><b>Sample API Search Result:</b></div><div>{'id': 72160317, 'readable': True, 'title': 'The Monster', 'title_short': 'The Monster',<br>'title_version': '', 'link': 'https://www.deezer.com/track/72160317', 'duration': 250, 'rank': 930303, 'explicit_lyrics': True, 'explicit_content_lyrics': 1, 'explicit_content_cover':<br>1, 'preview': 'https://cdns-preview-a.dzcdn.net/stream/c-a8f59d5c41501a2a767a088d92946325-1.mp3', 'md5_image': 'b6938db3addc3ccd9575d6d12220e466', 'artist': {'id': 13, 'name': 'Eminem', 'link': 'https://www.deezer.com/artist/13', 'picture':<br>'https://api.deezer.com/artist/13/image', 'picture_small': 'https://e-cdns-images.dzcdn.net/images/artist/19cc38f9d69b352f718782e7a22f9c32/56x56-000000-80-0-0.jpg', 'picture_medium': 'https://e-cdns-images.dzcdn.net/images/artist/19cc38f9d69b352f718782e7a22f9c32/250x250-000000-80-0-0.jpg', 'picture_big': 'https://e-cdns-images.dzcdn.net/images/artist/19cc38f9d69b352f718782e7a22f9c32/500x500-000000-80-0-0.jpg', 'picture_xl': 'https://e-cdns-images.dzcdn.net/images/artist/19cc38f9d69b352f718782e7a22f9c32/1000x1000-000000-80-0-0.jpg', 'tracklist': 'https://api.deezer.com/artist/13/top?limit=50', 'type': 'artist'},<br>'album': {'id': 7090505, 'title': 'The Marshall Mathers LP2 (Deluxe)', 'cover': 'https://api.deezer.com/album/7090505/image', 'cover_small': 'https://e-cdns-images.dzcdn.net/images/cover/b6938db3addc3ccd9575d6d12220e466/56x56-000000-80-0-0.jpg',<br>'cover_medium': 'https://e-cdns-images.dzcdn.net/images/cover/b6938db3addc3ccd9575d6d12220e466/250x250-000000-80-0-0.jpg', 'cover_big': 'https://e-cdns-images.dzcdn.net/images/cover/b6938db3addc3ccd9575d6d12220e466/500x500-000000-80-0-0.jpg', 'cover_xl': 'https://e-cdns-images.dzcdn.net/images/cover/b6938db3addc3ccd9575d6d12220e466/1000x1000-000000-80-0-0.jpg', 'md5_image': 'b6938db3addc3ccd9575d6d12220e466', 'tracklist': 'https://api.deezer.com/album/7090505/tracks', 'type': 'album'}, 'type':<br>'track'}</div><div><br></div><div><div>I will be utilizing the fields (id, readable, title, title_short, link, duration, rank,<br>artist_name, album_name) in my application. These fields provide comprehensive information about the tracks.<br>Specifically, fields such as id, readable, title, title_short, link, duration, and rank offer<br>detailed insights into individual tracks. Additionally, the fields (artist_name, album_name) provide valuable details<br>about the respective artists and albums.</div><div>This information plays a crucial role in presenting<br>a comprehensive overview of each track to the user. By leveraging these fields,<br>I aim to empower users to make informed decisions about their playlists. The<br>details about tracks, artists, and albums collectively contribute to enhancing the user experience,<br>allowing them to curate playlists that align with their preferences and tastes.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>The overarching goal is to leverage this mapped data to create a user-friendly<br>and feature-rich application. Users can explore, search, and organize tracks based on various<br>parameters such as title, duration, artist, and album. The application aims to empower<br>users to curate personalized playlists by providing detailed information about each track, artist,<br>and album. This comprehensive approach enhances the user experience, making the application a<br>valuable tool for music enthusiasts to discover, organize, and enjoy their favorite tracks.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.17.27image.png.webp?alt=media&token=b11e2795-21be-41dd-93ab-4fe09882fe95"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful insertion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.18.03image.png.webp?alt=media&token=a2e93d5d-a3f8-40c2-9435-faa0ba9f6562"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.18.36image.png.webp?alt=media&token=cf07e62d-21c9-42e5-93ba-36c5b34ca9b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prefilled Data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.21.56image.png.webp?alt=media&token=7004c3b3-e281-4432-bc7e-8a66dfdc0bc9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.23.22image.png.webp?alt=media&token=ea1eaca8-3170-44f2-9d2b-80d1e1c8b6b1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation Messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.25.16image.png.webp?alt=media&token=2491eb85-4db8-4117-a8f2-fb3c2f66dafc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record Updated in the database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.27.14image.png.webp?alt=media&token=b39f18ec-846e-4bb5-a8b7-860f12634468"/></td></tr>
<tr><td> <em>Caption:</em> <p>Track Record without any filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.27.52image.png.webp?alt=media&token=5ad5ee1e-4a71-4706-a0eb-c5d5782929bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter based on Artist name - Eminem<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.28.35image.png.webp?alt=media&token=91fe44d1-be24-48d2-8ae9-4e661fbd472e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sort Based on Rank in asc order LIMIT 20<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.29.23image.png.webp?alt=media&token=53cb0ce5-659a-4f1d-acb5-0fdacfa8065e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Based on Name, Artist or Album - &quot;Taylor Swift&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.30.39image.png.webp?alt=media&token=8b544605-2bd2-43d0-a29f-43011c80a7bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limit Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.31.28image.png.webp?alt=media&token=82d43135-77ca-409c-b78d-def95411336b"/></td></tr>
<tr><td> <em>Caption:</em> <p>No results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.33.41image.png.webp?alt=media&token=03564089-777c-410f-92b9-95be44ac5984"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Page with entity fetched by the id(check the url)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.35.37image.png.webp?alt=media&token=6e05f077-d97f-4d6e-828f-8d4e83fc9f2f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid id <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.38.04image.png.webp?alt=media&token=6fc43ffc-a741-4516-9bf0-872708e35400"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form with prefilled Data with proper id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.39.31image.png.webp?alt=media&token=d3f175ea-2744-4e52-83ac-2191ab9f2650"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.41.55image.png.webp?alt=media&token=c6c12352-d7a4-4b86-ba6a-32aa3d72facb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid or Missing ID<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.43.13image.png.webp?alt=media&token=6e6dc6f8-6525-42db-bc7b-fd85bd269555"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit - Title is Heeriye<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.43.38image.png.webp?alt=media&token=51fdbf1c-eb31-4bd1-a2b0-29fbb3d02ef7"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit - Title is Heeriye (feat Arijit)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.45.41image.png.webp?alt=media&token=6614bd44-5b74-40b3-87e3-faf5168942a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting - &quot;Not Afraid&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.45.55image.png.webp?alt=media&token=24b83019-6fa5-4606-8b00-3e9d2271669f"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Successful Delete - &quot;Not Afraid&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.47.30image.png.webp?alt=media&token=e900b002-599a-4933-979d-4fa6f290743f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deletion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.47.47image.png.webp?alt=media&token=f2eee7d7-8a3f-4a60-90e0-b26492ef70ad"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deletion - No records of &quot;Not Afraid&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.50.48image.png.webp?alt=media&token=7cec0889-40d8-415c-b855-a4cc11d6deff"/></td></tr>
<tr><td> <em>Caption:</em> <p>Fetching Data from API and transforming to add it in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.51.34image.png.webp?alt=media&token=624a52c0-c1e0-4ced-80c3-8ec876833fa4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicated Handled, SQL Query to the database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-27T23.53.41image.png.webp?alt=media&token=5f42951d-fb7b-4475-9f04-da33ad4571d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deezer.py file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div>In the application's navigation bar, specifically under the "Tracks" section, the admin can<br>initiate a data fetch by utilizing the search functionality. The search is facilitated<br>through a form accessible via the "fetch" link. Upon entering a query and<br>submitting the form, the Flask application triggers the fetch function. This function, connected<br>to the Deezer API through the Deezer class, performs a search based on<br>the admin's input. The search results, representing music tracks, undergo transformation and are<br>subsequently loaded into the local database. The admin receives feedback on the success<br>or failure of the operation through flash messages. Overall, this integrated search mechanism<br>enhances the application's usability, allowing admins to seamlessly explore and incorporate new tracks<br>into the database.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/26">https://github.com/Bhavya215/bs635-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Learnings:&nbsp;During this milestone, I gained valuable experience in working with external APIs, handling<br>nested data structures, and transforming API responses into a format suitable for database<br>storage. This process enhanced my skills in data manipulation and extraction, and I<br>learned effective strategies for dealing with nested dictionaries. Additionally, troubleshooting issues related to<br>API responses provided insights into debugging and error handling within a web development<br>context.</div><div><br></div>Issues:&nbsp;One challenge I encountered during this milestone was handling nested dictionaries in API<br>responses. To address this, I implemented a systematic approach to navigate through nested<br>structures, ensuring that I extracted the required data accurately. This involved creating utility<br>functions and using loops to iterate through the nested layers of the response.<br>Additionally, I utilized the DictToObject function to convert dictionaries into objects, simplifying access<br>to data attributes. This solution improved code readability and made it easier to<br>work with complex API responses.<br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-bs635-prod-a192a64ea5af.herokuapp.com/login">https://is601-bs635-prod-a192a64ea5af.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-28T00.02.19image.png.webp?alt=media&token=061e5bf7-21e9-4e99-8c4c-c0db04ad998c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Files<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-28T00.02.42image.png.webp?alt=media&token=97dce81d-239a-413f-8217-f1d99ddec7df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dashboard<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/bs635" target="_blank">Grading</a></td></tr></table>