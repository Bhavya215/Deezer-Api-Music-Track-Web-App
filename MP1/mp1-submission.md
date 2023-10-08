<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Bhavya Amish Shah (bs635)</td></tr>
<tr><td> <em>Generated: </em> 10/4/2023 3:52:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/bs635" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.02.05image.png.webp?alt=media&token=3ad81034-7b7b-402a-b45a-d4360c59c795"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code for add_task function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.03.53image.png.webp?alt=media&token=325febad-4940-43b6-b567-88525f302157"/></td></tr>
<tr><td> <em>Caption:</em> <p>The output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.05.23image.png.webp?alt=media&token=2a060461-744b-4a4a-bc34-326de925f9ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Just a preview that the task is added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.07.02image.png.webp?alt=media&token=752b7eb5-f126-4791-9051-583f553ba001"/></td></tr>
<tr><td> <em>Caption:</em> <p>The success message - &quot;Task added successfully&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.08.04image.png.webp?alt=media&token=d282fcf0-fab8-4f25-bbb4-4a685f57b798"/></td></tr>
<tr><td> <em>Caption:</em> <p>The failure message with the appropriate error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Update lastActivity: </b>Used&nbsp; `task['lastActivity'] = datetime.now()`<br></div><div><br></div><div><b>Assigning the values inserted by the user</b></div><div>2.<br>Set name: `task['name'] = name`</div><div>3. Set description: `task['description'] = description`</div><div>4. Set due date:<br>`task['due'] = str_to_datetime(due)`</div><div><b><br></b></div><div><b>Validating the due date format using the function</b></div><div>5. Validate due date<br>format: Checked within `str_to_datetime(due)`</div><div><b><br></b></div><div><b>6. Add task to tasks list: </b>used `tasks.append(task)` to append<br>the new task to the list of tasks</div><div><b>7. Output confirmation:</b> `print("Task added successfully!")`<br>or `print(f"Task addition failed: {e}")`, also used try, except to find the exact<br>error if the add_task fails</div><div><b>8. Call `save()`:</b> it is clearly seen in the<br>screenshot attached above</div><div><b>9.&nbsp;</b><b>Include Comments:</b>&nbsp;I included comments with the UCID "bs635" and the date<br>of implementation, "Date: 1 October, 2023," for documentation.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.16.13image.png.webp?alt=media&token=5f9a9020-2ad7-480e-85e6-a627024487e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code for process_update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-01T23.19.27image.png.webp?alt=media&token=c2fd7dd4-2d69-4d69-9e7d-66989ddf908b"/></td></tr>
<tr><td> <em>Caption:</em> <p>The exisiting values are displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Get task by index: </b>Used `task = tasks[index]`<br></div><div><b>2. Consider index out of<br>bounds:</b> Checked within `if 0 &lt;= index &lt; len(tasks):` and displayed an appropriate<br>message if it was out of bound</div><div><b>3. Show existing values: </b>Displayed existing values<br>for name, description, and due date where TODOs are marked -&gt; Screenshot is<br>attached above</div><div><b>4.&nbsp;</b><b>Include Comments:</b>&nbsp;I included comments with the UCID "bs635" and the date of<br>implementation, "Date: 1 October, 2023," for documentation.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.34.13Screenshot%202023-10-04%20153304.png.webp?alt=media&token=26fa6edd-fe29-40dd-b8b7-7a65d18a857c"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.36.31image.png.webp?alt=media&token=8117c748-805b-445d-b7e9-5300b7234f16"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.37.05image.png.webp?alt=media&token=2bb65710-43b4-4613-b717-740fdc44df99"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure-1 : Invalid task number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.39.44image.png.webp?alt=media&token=3b2b405e-4d82-45f7-93b8-ba2cc6dad636"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure-2: Format error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>1.Find Task</b>: I found the task by its index using `tasks[index].copy()`.</div><div><br></div><div><b>2. Handle Invalid<br>Index: </b>I checked if the index is valid (within bounds) and provided an<br>appropriate error message if it wasn't valid.</div><div><br></div><div><b>3. Update Incoming Task Data</b>: I updated<br>the incoming task data if it was provided, ensuring that if a property<br>wasn't provided, I used the original task property value.</div><div><br></div><div><b>4. Update lastActivity:</b> I updated<br>the `lastActivity` property with the current datetime value.</div><div><br></div><div><b>5. Output Task Update:</b> I printed<br>a message indicating that the task was updated if any items were changed;<br>otherwise, I mentioned that the task was not updated.</div><div><br></div><div><b>6. Call save()</b>: I ensured<br>that the `save()` function was called at the end of the function to<br>save any changes made to the tasks list.</div><div><br></div><div><b>7. Include Comments:</b> I included comments<br>with the UCID "bs635" and the date of implementation, "Date: 1 October, 2023,"<br>for documentation.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T18.58.32image.png.webp?alt=media&token=bc32c57b-d8f1-458b-83c0-dd912a641e09"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T19.00.31image.png.webp?alt=media&token=a90b8e57-4ac9-433c-a668-451e0ea1a995"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message -&gt; datetime() updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T19.01.30image.png.webp?alt=media&token=b6bce74f-17a4-4eb7-8338-51085e5edd8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>1. <b>Find Task:</b> The task was found from the list by its index<br>using `tasks[index].copy()`.</div><div><br></div><div>2. <b>Handle Invalid Index:</b>&nbsp;I checked if the index is valid (within bounds)<br>and provided an appropriate error message if it wasn't valid. I used if..else<br>for handling it</div><div><br></div><div>3. <b>Record Completion Time:</b> If the task was not marked as<br>done (`task['done'] == False`), I recorded the current datetime as the completion time<br>using `task['done'] = datetime.now()`.</div><div><br></div><div>4. <b>Check for Completed Task: </b>I<b>&nbsp;</b>checked if the task was<br>already marked as done (`task['done'] == True`) and printed a message indicating that<br>it's already been completed.</div><div><br></div><div>5. <b>Call save():</b>&nbsp;I ensured that the `save()` function was called<br>at the end of the function to save any changes made to the<br>tasks list.</div><div><br></div><div>6.<b> Include Comments:</b> I included comments with your UCID, "bs635," and the<br>date of implementation, "Date: 1 October, 2023," for documentation.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T19.13.56image.png.webp?alt=media&token=cffecab0-bb78-4e04-a371-1150ed1bdcac"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T19.15.01image.png.webp?alt=media&token=e2740291-01a4-4605-a5d5-52bae6ddc4fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-02T19.15.37image.png.webp?alt=media&token=737f851a-36ef-45ca-bbe5-efcc3c572a8d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.23.58image.png.webp?alt=media&token=fea1e4b8-6545-40ac-a54a-e9aae8383163"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mixed status tasks - complete and incomplete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.27.05image.png.webp?alt=media&token=92801353-15d9-4908-8c21-1111f0cd8c50"/></td></tr>
<tr><td> <em>Caption:</em> <p>All incomplete tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.47.09image.png.webp?alt=media&token=8e4d862e-d135-4165-bb55-55f359ed50bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>All completed tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.49.35image.png.webp?alt=media&token=ca9a721b-df5a-4a8b-a48f-f0e3d4424fe9"/></td></tr>
<tr><td> <em>Caption:</em> <p>No tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.28.37image.png.webp?alt=media&token=bea4bcd5-86d6-4f85-9df4-dd5761950baa"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code for delete_task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.30.52image.png.webp?alt=media&token=79de7bf5-a3ae-4c99-8ea8-9d0b27d8e5b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful delete task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.30.04image.png.webp?alt=media&token=ae815670-42ea-4985-b319-4bfc1530258c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure message for delete task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>Find Task by Index:</b> It finds the task from the list by its<br>index using tasks[index].copy()</div><div>deleted_task = tasks.pop(index)</div><div><br></div><div><b>Handle Invalid Index:</b> The function checks if the index<br>is valid (within bounds) and provides an appropriate error message if it isn't<br>valid</div><div>if 0 &lt;= index &lt; len(tasks): and print("Task not deleted! -&gt; Enter a<br>valid task number")</div><div><br></div><div><b>Show Success or Failure Message:</b> It prints a message indicating whether<br>the task was deleted successfully or not</div><div>print(f"Task '{deleted_task['name']}' deleted successfully.") and print("Task not<br>deleted! -&gt; Enter a valid task number")</div><div><br></div><div><b>Call save(): </b>The delete_task function ensures that<br>the save() function is called at the end to save any changes made<br>to the tasks list</div><div><br></div><div><b>Include Comments:</b>&nbsp;I included comments with the UCID "bs635" and the<br>date of implementation, "Date: 1 October, 2023," for documentation</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T17.43.47image.png.webp?alt=media&token=968c8071-acab-4b9a-a3ac-e53baf52047a"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T18.57.11image.png.webp?alt=media&token=cf2ba344-2e34-4b5d-a9ec-acb575a9cf9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message - All incomplete tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T18.59.54image.png.webp?alt=media&token=a2a1be4c-882c-4cbb-b69a-c78bc395c1be"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure message - No tasks pending<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Generate a list of tasks where the task is not done:</b><br></div><div>In this<br>step, I create a new list called _incomplete_tasks, which contains tasks that are<br>not marked as done (task['done'] == False).<br></div><div><br></div><div><b>2. Pass that list into list_tasks():</b></div><div>After generating<br>the list of incomplete tasks, I pass this list to the list_tasks() function,<br>which displays the details of these incomplete tasks.<br></div><div><br></div><div><b>Include Comments:</b> I included&nbsp; comments with<br>the UCID "bs635" and the date of implementation, "Date: 1 October, 2023," for<br>documentation.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.05.35image.png.webp?alt=media&token=61e707e6-8db8-4834-a674-d6b7436c3836"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.09.47image.png.webp?alt=media&token=0a70f3ee-e2b4-49b1-972b-505a6d4110bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message - overdue tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.10.56image.png.webp?alt=media&token=dd31979f-149e-45c4-a731-b6911bb0c2ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure message - No overdue tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Generate a list of tasks that are overdue:</b></div><div>In this step, I create<br>a new list called _overdue_tasks, which contains tasks that are not marked as<br>done (task['done'] == False) and have a due date that is in the<br>past (task['due'] &lt; time).</div><div><br></div><div><b>2. Pass that list into list_tasks():</b></div><div>After generating the list of<br>overdue tasks, I pass this list to the list_tasks() function, which displays the<br>details of these overdue tasks.<br></div><div><br></div><div><b>3. Include Comments: </b>I included comments with the UCID<br>"bs635" and the date of implementation, "Date: 1 October, 2023," for documentation.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.13.31image.png.webp?alt=media&token=8d5e2885-62b3-449e-89b0-8835da3cc4fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.16.00image.png.webp?alt=media&token=5be3f758-4d50-4207-bdd8-ca2b32010fb8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure - overdue time<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.16.38image.png.webp?alt=media&token=19e816fc-de28-4626-8180-d04a48c96ab8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success - Remaining time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Get the task by index:</b></div><div>&nbsp; In this step, I retrieve the task<br>from the list of tasks by its index using `task = tasks[index].copy()`.</div><div><br></div><div><b>2. Consider<br>index out of bounds scenarios and include appropriate message(s) for an invalid index:</b></div><div>&nbsp;I<br>check whether the index is within valid bounds (`0 &lt;= index &lt; len(tasks)`)<br>and include appropriate error messages if the index is invalid.</div><div><br></div><div><b>3. Get the days,<br>hours, minutes, seconds between the due date and now:</b></div><div>&nbsp;I calculate the time difference<br>between the due date and the current time, obtaining the number of days,<br>hours, minutes, and seconds remaining using `time_difference.total_seconds()` and appropriate divisions.</div><div><br></div><div><div><b>4. Display the remaining<br>time via print in a clear format showing X days, X hours, X<br>minutes, X seconds (time components must be clearly separated):</b></div><div>I display the remaining time<br>in a clear format by formatting and printing the number of days, hours,<br>minutes, and seconds as requested.</div><div><br></div><div><b>5. If the due date is in the past,<br>print out how many days, hours, minutes, and seconds the task is overdue<br>(clearly note that it's overdue, values should be positive):</b></div><div>&nbsp;If the calculated time difference<br>is negative (indicating the due date is in the past), I print a<br>message indicating that the task is overdue and display the positive values for<br>days, hours, minutes, and seconds.</div><div><br></div><div><b>6. Include Comments:</b>&nbsp;</div><div>I included comments with the UCID "bs635"<br>and the date of implementation, "Date: 1 October, 2023," for documentation.</div><div><br></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.23.55image.png.webp?alt=media&token=e9e3c19c-c5bb-4e5c-bf61-f52c771d71fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Git Bash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.25.35image.png.webp?alt=media&token=c257c275-d0cd-480b-965d-dd7b1bbd533b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.26.29Screenshot%202023-10-04%20132519.png.webp?alt=media&token=7b342d30-6986-415a-b6dd-3025dbb86bc2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Image-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-04T19.27.03Screenshot%202023-10-04%20132531.png.webp?alt=media&token=65c2d915-4740-47d7-a8d0-4bac5aa0364b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Image-2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div>I encountered two significant challenges during the project. The first issue arose when<br>reading the "due" attribute from the JSON file, which was initially stored as<br>a string but needed to be converted to a datetime object. This experience<br>taught me that JSON files primarily support three data types: integers, floats, and<br>strings, highlighting the importance of proper data type management.</div><div><br></div><div>The second challenge emerged when<br>I attempted to update a task. I realized that I was modifying a<br>local copy of the task instead of the global task list, leading to<br>errors. This situation deepened my understanding of global and local variables, emphasizing the<br>significance of correctly managing variable scope. Overall, the project provided valuable insights and<br>was a stimulating learning experience.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/5">https://github.com/Bhavya215/bs635-is601-007/pull/5</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/bs635" target="_blank">Grading</a></td></tr></table>