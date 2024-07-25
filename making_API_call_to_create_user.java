const createUser = async (username, password, email, phone) => {
  const response = await fetch('/api/createUser', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      username,
      password,
      email,
      phone
    })
  });

  const data = await response.json();
  console.log(data);
}
