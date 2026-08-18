async function getUsers() {

    const response = await fetch(
        "https://api.example.com/users"
    );

    const data = await response.json();

    return data;
}


async function getUserById(userId) {

    const response = await fetch(
        "https://api.example.com/users/" + userId
    );

    const data = await response.json();

    return data;
}