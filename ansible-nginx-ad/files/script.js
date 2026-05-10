const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");
const loadUsersBtn = document.getElementById("loadUsersBtn");
const usersSection = document.getElementById("usersSection");
const usersList = document.getElementById("usersList");
const serverInfo = document.getElementById("serverInfo");

let currentUsername = "";
let currentPassword = "";

function showMessage(text, type) {
    message.textContent = text;
    message.className = "message " + type;
}

async function loadServerInfo() {
    try {
        const response = await fetch("/api/server");
        const data = await response.json();

        serverInfo.textContent = `${data.web_server} | AD: ${data.ad_server} | Dominio: ${data.domain}`;
    } catch (error) {
        serverInfo.textContent = "No se pudo cargar información del servidor.";
    }
}

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (data.success) {
            currentUsername = username;
            currentPassword = password;

            showMessage(`${data.message} Servidor web: ${data.web_server}`, "ok");
            loadUsersBtn.disabled = false;
            usersSection.classList.remove("visible");
            usersList.innerHTML = "";
        } else {
            currentUsername = "";
            currentPassword = "";

            showMessage(data.message, "error");
            loadUsersBtn.disabled = true;
            usersSection.classList.remove("visible");
        }
    } catch (error) {
        showMessage("Error de comunicación con el servidor web.", "error");
    }
});

loadUsersBtn.addEventListener("click", async function () {
    try {
        const response = await fetch("/api/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: currentUsername,
                password: currentPassword
            })
        });

        const data = await response.json();

        usersList.innerHTML = "";

        if (!data.success) {
            showMessage(data.message, "error");
            return;
        }

        data.users.forEach(function (user) {
            const li = document.createElement("li");
            li.textContent = `${user.nombre} | ${user.usuario} | ${user.upn}`;
            usersList.appendChild(li);
        });

        usersSection.classList.add("visible");
        showMessage(`${data.message} Servidor web: ${data.web_server}`, "ok");
    } catch (error) {
        showMessage("Error al consultar usuarios de Active Directory.", "error");
    }
});

loadServerInfo();