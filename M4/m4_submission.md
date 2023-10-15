<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Bhavya Amish Shah (bs635)</td></tr>
<tr><td> <em>Generated: </em> 10/15/2023 12:46:45 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/bs635" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.02.45image.png.webp?alt=media&token=597951c4-5f4e-4891-a396-1c38ac20c840"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition function code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.04.01image.png.webp?alt=media&token=0e3bba37-9bbf-465b-b59a-cb55af2a0c4d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction function code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.15.40image.png.webp?alt=media&token=dea97bed-a5d1-496b-9578-adc1705e3d36"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.17.45image.png.webp?alt=media&token=0fc60642-aeab-4698-b624-b2850fe0c41c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division Function code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.26.29image.png.webp?alt=media&token=db2c5e90-4149-466d-bd14-87278ac48925"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for num_add_num <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.27.21image.png.webp?alt=media&token=40984d5e-f0a6-425e-95b5-274d5c8afb45"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.27.48image.png.webp?alt=media&token=158a3fc8-e812-490a-964d-fa23761b7d87"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.28.42image.png.webp?alt=media&token=fd27df35-dc5a-4300-af41-041e3de09b45"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for ans_add_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.29.27image.png.webp?alt=media&token=f2c2fc70-97ef-4d05-a22b-6345fa1baede"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.29.44image.png.webp?alt=media&token=91df0a00-b65b-422c-acba-9c49fa340e61"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.30.32image.png.webp?alt=media&token=5fb398db-db61-4e77-833d-a2e39e1edd3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for num_sub_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.31.18image.png.webp?alt=media&token=43cca1e4-f0b9-4e02-99ce-1526b6fde28c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.31.51image.png.webp?alt=media&token=7a9f34bf-8ebe-41d1-b152-fc23822cf0a2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.32.22image.png.webp?alt=media&token=45319593-1660-4469-9a39-b5f1449dafb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for  ans_sub_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.32.57image.png.webp?alt=media&token=6e2eb144-e9fe-49cb-aba3-b2d1c79d9430"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.33.14image.png.webp?alt=media&token=deaa7d08-fb12-4262-9abe-1607038b9f0a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.34.05image.png.webp?alt=media&token=786b9328-ee38-4b1b-8a45-ed39f1d9c321"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for num_mult_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.34.19image.png.webp?alt=media&token=62780a1a-5736-4de8-a905-dd74a6248222"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.34.32image.png.webp?alt=media&token=e4d4a597-33fb-4066-8bb8-f91c6c3558da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.35.44image.png.webp?alt=media&token=63a16c90-0dde-4fc4-bc5e-b2e1f25cbfec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for ans_mult_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.36.00image.png.webp?alt=media&token=10a3a0aa-fb57-4c9b-bd14-8d173b0ed9bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.36.15image.png.webp?alt=media&token=b3f0afa3-b3ca-421b-9572-4cbef4e2f1e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.37.21image.png.webp?alt=media&token=feea9877-2252-4a4f-8942-3e54615411b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for num_div_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.37.34image.png.webp?alt=media&token=d10b053f-d5b3-40d1-ba3c-c662b83389cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.37.45image.png.webp?alt=media&token=f695ea39-577d-46f4-b0b9-0422d3fd1882"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.38.45image.png.webp?alt=media&token=59c7ec6a-34fa-4de1-8641-4e5e9294ce04"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the Test Case for ans_div_num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.38.58image.png.webp?alt=media&token=89dbad0a-baad-48ae-993f-f9808ddb37ff"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.39.13image.png.webp?alt=media&token=cb146a8a-ad61-49a2-9fe7-8f528d402bb3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case Passing - 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fbs635%2F2023-10-15T16.39.26image.png.webp?alt=media&token=2c701648-b286-4f27-b52c-38ef5e3efd45"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of all test case passing<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>From this assignment, I learned to design and implement a calculator class in<br>Python, applying key Object-Oriented Programming (OOP) principles. I gained experience in writing unit<br>tests using parameterized testing, demonstrating the importance of code reliability and error handling..<br>This assignment enhanced my skills in OOP and testing.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>In this assignment, I learned that test cases serve as a critical tool<br>for verifying code functionality. Fixtures, which allow for setting up consistent initial states,<br>became an essential part of creating reliable and controlled testing environments. Parameterized tests,<br>a key feature, enabled efficient testing of multiple scenarios with minimal code duplication,<br>improving test coverage and maintainability. This assignment highlighted the significance of a well-structured<br>testing strategy, encompassing these concepts to ensure code quality and reliability.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Bhavya215/bs635-is601-007/pull/7">https://github.com/Bhavya215/bs635-is601-007/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/bs635" target="_blank">Grading</a></td></tr></table>