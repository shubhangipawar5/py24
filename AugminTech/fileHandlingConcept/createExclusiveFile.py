#it will create a file once only, later if you have to w,r,a then use the specific mode
"""
f=open('xclusiveFile','x')
f.write('creating exclusive file')
f.close()
#if you try to create same file again it will give error -> FileExistsError: [Errno 17] File exists: 'xclusiveFile'
"""


f=open('xclusiveFile','w')
f.write("How are u Aayu?")
f.close()
