# TESTING REQUEST TOKENS STEPS

- Use your preferred API Client, I'll be using ThunderClient for this test.

- Send a `GET` request to `http://localhost:8000/api/token/`.
  - .If the previous step fails because `GET` is not allowed, copy and use this in your browser address bar and replace the values inside the tags `http://localhost:8000/api/token/?username=<USERNAME>&password=<PASSWORD>`.
  - Use `POST` with the previous step.

- You will recieve `refresh` and `access` tokens.

- Send a `GET` request to `http://localhost:8000/api/v1/chips/<id>`, change the id to the item id you want to check.

- Add `Authorization` Query Parameter with the value of the `access` token.

- You will recieve a `JSON` with chips info as a response.

- You can use the `refresh` token in the same way above.
