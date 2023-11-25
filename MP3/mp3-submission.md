<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Bhavya Amish Shah (bs635)</td></tr>
<tr><td> <em>Generated: </em> 11/25/2023 1:06:20 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/bs635" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.02.51image.png.webp?alt=media&token=ae1a930c-01b2-47b0-80a5-c318baa7d9e4"/></td></tr>
<tr><td> <em>Caption:</em> <p>The Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.03.38image.png.webp?alt=media&token=6e865e9c-651a-46c0-acd1-e24b7f084f74"/></td></tr>
<tr><td> <em>Caption:</em> <p>The Code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.04.22image.png.webp?alt=media&token=75584e5b-442c-406d-bb67-4d429d02437e"/></td></tr>
<tr><td> <em>Caption:</em> <p>The page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.05.54image.png.webp?alt=media&token=7c8499c4-ac9e-49ae-a3cb-8314ad242591"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.08.27image.png.webp?alt=media&token=c8617551-7d8a-4bbd-8960-6a2f76373ec9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.09.26image.png.webp?alt=media&token=bd94a4d0-155a-49f2-8821-d5142fc0fdac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.10.38image.png.webp?alt=media&token=d63e95d3-98e8-4545-8210-7e4fcf5d4fb5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task-3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.11.44image.png.webp?alt=media&token=22174c33-7a3a-42cd-bede-cfd02dd8e4a2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task - 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.13.16image.png.webp?alt=media&token=e5ed93bb-e39b-4c4f-bbff-125890ef4d73"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task-5,6,7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.14.00image.png.webp?alt=media&token=32c073c5-b0e6-4908-8600-d30425819c3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task-8<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.16.04image.png.webp?alt=media&token=69b6dd5c-6717-4d96-8bb3-644267c72fbd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create View with empty fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.16.51image.png.webp?alt=media&token=d990dda2-9339-4cbe-99a4-d230ff630f36"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit View with prefilled fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.19.02image.png.webp?alt=media&token=37ad657e-bdf4-4115-8e62-03018e0b29ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot - 1<br>Manage_donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.19.27image.png.webp?alt=media&token=058ba10c-cda7-492e-abde-badaa69a278c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot -2<br>Manage_donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.20.36image.png.webp?alt=media&token=23093c98-8b5b-4f3e-b190-42a63ecc93fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot -3<br>Manage_donations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.21.56image.png.webp?alt=media&token=f100989a-a4e7-45e5-af0f-43fa6f01f023"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page with filter of specific organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.22.10image.png.webp?alt=media&token=786df4d9-5ee8-4f76-a94b-be96eff8763f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page with donations without any filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.23.47image.png.webp?alt=media&token=fc89d231-74f0-4ed3-9a2c-de765e30be86"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot - 1 list_donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.24.07image.png.webp?alt=media&token=989051fb-e2df-40ae-9840-fefbd0d0aa52"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot -2 list_donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.24.24image.png.webp?alt=media&token=9a711341-4efe-4fa8-93ec-49cc5187aa04"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot - 3 list_donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.24.48image.png.webp?alt=media&token=41cd4f55-596c-46f4-9d20-cbc8a0511876"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot - 4 list_donations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.27.10image.png.webp?alt=media&token=b05a34bf-1c89-444b-953f-30b68021d8e1"/></td></tr>
<tr><td> <em>Caption:</em> <p>search-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.28.26image.png.webp?alt=media&token=b20dc171-c0be-481c-bbc8-b80e60b254b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.29.06image.png.webp?alt=media&token=75f85306-c50c-4bb4-b855-7fa0fe06d860"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-3,4,5,6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.31.10image.png.webp?alt=media&token=6c7b1cc7-9447-4d96-a33d-9a835f16294b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-7,8,9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.32.03image.png.webp?alt=media&token=e3c84cf1-3560-4552-90e1-7e211ab6d1cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.33.45image.png.webp?alt=media&token=a582b174-f377-465d-9a4a-73e1bde2f90c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.35.00image.png.webp?alt=media&token=bdff2bab-b061-42e7-98fd-26eec6f70a25"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.35.32image.png.webp?alt=media&token=06aba04f-75fa-4723-bbee-edb0255e40e6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-2,3,4,4a,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.36.45image.png.webp?alt=media&token=c3f24a81-03e1-4c75-8b63-ae44dfd4769f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-6,7,8,9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.37.33image.png.webp?alt=media&token=5ad8bea2-21f4-4414-a9ea-7b4f869d08b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-11,7<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.39.09image.png.webp?alt=media&token=a73f0c3b-c0a1-47e8-bf14-c1dd496a0811"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.39.39image.png.webp?alt=media&token=f06c341c-a51a-4934-8e41-ee1a26ad3800"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-2,3,4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.40.27image.png.webp?alt=media&token=533c073d-e2aa-45f0-b087-359206a78351"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-5,5a,6,7,8,9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.41.19image.png.webp?alt=media&token=3338c7cc-959c-442c-9bee-3345e5bc0510"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-10,11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.41.38image.png.webp?alt=media&token=3a4c3873-f146-4642-8713-6ab5a381b8b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-12<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.42.26image.png.webp?alt=media&token=17850819-0a9a-4c59-8a76-da083421db3c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.44.36image.png.webp?alt=media&token=557c3a0a-a885-4a9a-b04c-f7e375b084df"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-22T01.45.48image.png.webp?alt=media&token=0a3f97fa-c3a4-4d66-a199-0ef4883aa839"/></td></tr>
<tr><td> <em>Caption:</em> <p>The Delete on website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.27.56image.png.webp?alt=media&token=a04140da-c4b7-4a7d-8a2d-ee7b9578ebf1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Organization Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.28.39image.png.webp?alt=media&token=7688ffaf-cbcf-43c4-b088-978dfc438483"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Organization Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.29.33image.png.webp?alt=media&token=b4e34bb2-b91f-4fa2-a98e-570f8e6a91fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code - 1<br>Manage_organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.29.52image.png.webp?alt=media&token=a9a9f166-f832-4ee0-8dab-8da064207367"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code - 2<br>Manage_organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.31.50image.png.webp?alt=media&token=bda2c8b4-a845-475b-827e-77dac93da3b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Page without any filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.32.35image.png.webp?alt=media&token=3ec539c0-88e6-4a7e-baf8-711591291cd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Page with filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.33.14image.png.webp?alt=media&token=98dc9a1f-dea2-42fc-b1e2-eb857840b1c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code-1<br>List_organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.33.27image.png.webp?alt=media&token=d3dc881a-29df-436f-998e-68546b294979"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code-2<br>List_organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.33.45image.png.webp?alt=media&token=cf711d92-b4fe-4977-9172-b0ad45c5fa57"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code-3<br>List_organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.34.00image.png.webp?alt=media&token=b405d11c-a485-478a-bf46-9040a1ffc37e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code-4<br>List_organizations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.44.34image.png.webp?alt=media&token=d29ee816-cd5d-433f-813e-63a06bdfa379"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.44.56image.png.webp?alt=media&token=4662206f-9ef7-4816-b34a-d9bfa290a70d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-2,3,4,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.45.54image.png.webp?alt=media&token=e30052ee-9a6e-4d16-a445-ab0132c06a07"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search-6,7,8,9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.47.04image.png.webp?alt=media&token=bb3680b2-e5cb-461f-8894-8a445096a513"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.48.35image.png.webp?alt=media&token=2cb05acf-493b-447c-9a75-db3466039e4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-4,5,5a,6,6a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.48.57image.png.webp?alt=media&token=647f7173-14f0-4177-843a-3cf6f1549be1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-7,8,9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.50.37image.png.webp?alt=media&token=4043baa8-b3a5-4d85-b3d0-5312502e30c2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add-10,11<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.51.34image.png.webp?alt=media&token=cd415b9c-9b8a-4efc-a279-aa616ed5df76"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.51.53image.png.webp?alt=media&token=eb5125c1-c23b-4e97-9d1c-2c5141d388c1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-4,5,6,6a,7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.52.45image.png.webp?alt=media&token=30fb768d-1357-410f-8569-52db3a1ab2e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-7a,8,9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.53.04image.png.webp?alt=media&token=683248c5-0efa-4943-ae0f-025b509e2eb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-10,11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.54.03image.png.webp?alt=media&token=b2af3317-d026-46ee-988b-8746529b7a41"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit-12,13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.54.46image.png.webp?alt=media&token=555b7aed-b1a2-483d-b8f4-c57b6d078b62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete-1,2,3,4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.55.11image.png.webp?alt=media&token=1cb68c2a-1509-452d-badb-96529f60f1c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete-4,5<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.58.50image.png.webp?alt=media&token=aac06add-3bf1-4ad6-b02c-270070139fec"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases passing with summary<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T17.59.21image.png.webp?alt=media&token=6875e0b3-cc2b-47c3-acf2-865b2dc58853"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T18.00.25image.png.webp?alt=media&token=41b81697-a4a4-44b8-a5ff-ac4d2e40bd77"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T18.01.05image.png.webp?alt=media&token=c92592ae-34df-4bd4-94bd-fc204e067a27"/></td></tr>
<tr><td> <em>Caption:</em> <p>All Test cases passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>Yes, all test cases passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/24">https://github.com/Bhavya215/bs635-is601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T18.02.34image.png.webp?alt=media&token=8e6676f6-acd3-46de-9cd4-8c8c68d99965"/></td></tr>
<tr><td> <em>Caption:</em> <p>9 commits in total<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T18.03.51image.png.webp?alt=media&token=dd4d7082-8eb7-49d3-9035-17d022070aa8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wakatime-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-11-25T18.04.15image.png.webp?alt=media&token=1b426810-ca52-4ddd-87e8-af67872e2d46"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wakatime-2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-bs635-td-37cefe7f6b65.herokuapp.com/">https://is601-007-bs635-td-37cefe7f6b65.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/bs635" target="_blank">Grading</a></td></tr></table>