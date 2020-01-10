In order to run the app, you can:
```
$ cd server/
$ python app.py
```

Then, you can run either of the clients (under /client) in another terminal
```
$ cd client
$ python pingPong.py
```
or
```
$ cd client
$ python filePingPong.py
```

If you look in server/app.py, there are 3 HTTP endpoints:
 - / Just returns "Hello World". This can be tested by going to http://localhost:5000/ on your browser while the app is running.
 - /pingPayload Expects a request containing a single integer. Adds 1 to the integer, and returns it
 - /filePingPayload Expects a request containing a file upload. The file should just contain a single integer. The server then saves the file to its own disk, adds 1 to the integer in the file, and returns the file back to the client.

Inside client/, there are two python files:

 - client/pingPayload.py Calls the /pingPayload endpoint with a starting number to get the next number. It then keeps doing this forever. If it starts at 1, it will get 2, then 3, then 4, etc... on each requestclient
- /filePingPayload.py Does exactly the same as client/pingPayload.py, except it transfers data to the server using a file upload. Concretely, it initializes a file on the client's disk called "number.txt" with the number "1" as its contents. Then, it sends it to the server at the /filePingPayload endpoint and receives a new file back as a download (which will contain "2"), and writes this file to disk. It sends the next request with the file it just received and continues this loop forever.
