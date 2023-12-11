<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Bhavya Amish Shah (bs635)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2023 6:45:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/bs635" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <div>Users can utilize the tracks from the API to manage playlists in the<br>following ways:</div><div><br></div><div>1. View Playlists: Users can see their existing playlists and their details.</div><div>2.<br>Create New Playlist: Users can create a new playlist, receiving an ID for<br>further interactions.</div><div>3. Add Tracks: Users can search for and add specific tracks(fetched from<br>the API) to a chosen playlist.</div><div>4. View Playlist Details: Users can retrieve detailed<br>information about a playlist.</div><div>5. Edit Playlist: Users can modify existing playlists, such as<br>changing names or track order.</div><div>6. Delete Playlist: Users can remove unwanted playlists from<br>their collection.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <div>1. Manual Edit Form:</div><div>Users submit changes through the form.</div><div>The backend processes and immediately<br>reflects the edits in the associated data.</div><div><br></div><div>2.API Data Sync:</div><div>Sync fetches updates from an<br>external source.</div><div>Backend fetches data via API, overwriting or merging it based on the<br>strategy.</div><div>Ensures local data aligns with the external source after the sync.</div><div><br></div><div>The relationship between<br>the user and playlists, tracks, and associated data is typically a many-to-many relationship.<br>Users can have multiple playlists, and each playlist can contain multiple tracks. Additionally,<br>a track can belong to multiple playlists.&nbsp;</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.16.36image.png.webp?alt=media&token=32f70d93-a62d-4a38-8f58-eebf37535f35"/></td></tr>
<tr><td> <em>Caption:</em> <p>A button to add the track in the desired playlist -&gt; Track -<br>&quot;Rap God&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.18.01image.png.webp?alt=media&token=55378ef3-362b-4711-8e9e-46028c426f56"/></td></tr>
<tr><td> <em>Caption:</em> <p>Playlists of this user <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.18.37image.png.webp?alt=media&token=fc1a3798-a31b-4570-8bba-9d65b8e2cf56"/></td></tr>
<tr><td> <em>Caption:</em> <p>Party Playlist with the added song for this user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.21.15image.png.webp?alt=media&token=ab261cdd-88d5-4b1c-8a83-263862c17f04"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for listing all the playlists - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.21.31image.png.webp?alt=media&token=bb99a271-df2a-4b09-8868-d61fb43dc6a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for listing all the playlists - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.22.38image.png.webp?alt=media&token=e53b5c9b-d10a-4f34-8d79-405d9ebd1628"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for viewing the playlist - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.23.00image.png.webp?alt=media&token=60f28178-969f-4f64-9b6f-9e88a4e52dcb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for viewing the playlist - 2<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.26.09image.png.webp?alt=media&token=153b0ea7-586b-4b9d-8761-b8ba416bb7a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>View all Playlists<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.26.27image.png.webp?alt=media&token=7862ec49-bfec-44a8-b5ff-a0f908523621"/></td></tr>
<tr><td> <em>Caption:</em> <p>View all Tracks in the particular playlist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/29">https://github.com/Bhavya215/bs635-is601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.29.56image.png.webp?alt=media&token=44491282-1e28-4026-b5dd-f119f7073417"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tracks present in total number of user&#39;s playlists<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.30.31image.png.webp?alt=media&token=28671011-32bd-476e-8456-7ac2123c4711"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tracks not present in any of the user&#39;s playlists<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/29">https://github.com/Bhavya215/bs635-is601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.32.10image.png.webp?alt=media&token=e32cd922-60d3-48e0-aab3-132f1327369b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can add a track to the playlist of any user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.32.54image.png.webp?alt=media&token=4a4d1b61-0feb-47a6-91fa-146bb41d81d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can delete a track from the playlist of any user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/29">https://github.com/Bhavya215/bs635-is601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.34.22image.png.webp?alt=media&token=0197ed86-1f86-4a9e-9b51-9d553eb0e7e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can see all the users<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-12-11T23.34.34image.png.webp?alt=media&token=1a99d9d9-837f-49d6-95f4-a93aa80ddd4c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can view the profile of  all the users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <div>1.List Users Page:</div><div>Purpose: Displays a list of all users.</div><div>Logic:</div><div>Admin navigates to the "List<br>Users" page.</div><div>Backend fetches and displays user details (id, username, email) from the database.</div><div><br></div><div>2.View<br>User Page:</div><div>Purpose: Shows details of a specific user.</div><div>Logic:</div><div>Admin selects a user from the<br>list, navigates to the "View User" page.</div><div>Backend fetches and displays detailed information about<br>the selected user.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/29">https://github.com/Bhavya215/bs635-is601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Issues Faced:</div><div><br></div><div>1. Playlist Creation:</div><div>Encountered difficulties in implementing a seamless playlist creation process.</div><div>Struggled with<br>ensuring data integrity and proper associations between tracks and playlists.</div><div><br></div><div>-Solution for Playlist Creation:</div><div>Implemented<br>a step-by-step form validation to ensure the completeness of playlist information.</div><div>Validated and adjusted<br>the backend logic to establish correct relationships between tracks and playlists in the<br>database.</div><div><br></div><div>2.Admin Access to Playlists:</div><div>Faced challenges in providing admin-exclusive access to view and manage<br>all playlists.</div><div>Needed to ensure proper authorization and visibility control.</div><div><br></div><div>-Solution for Admin Access:</div><div>Implemented role-based<br>access control, ensuring that only admins have access to view, edit, and delete<br>all playlists</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/bs635" target="_blank">Grading</a></td></tr></table>