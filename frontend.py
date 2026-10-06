PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Remon's Finance Tracker</title>
</head>
<body>
<h1>Remon's personal Finance Tracker</h1>
<p> If you arent Remon leave 🤬</p>

<div id="auth-section">
  <h2>Register</h2>
  <input id="reg-username" placeholder="Username">
  <input id="reg-email" placeholder="Email">
  <input id="reg-password" type="password" placeholder="Password">
  <button onclick="register()">Register</button>

  <h2>Login</h2>
  <input id="login-username" placeholder="Username">
  <input id="login-password" type="password" placeholder="Password">
  <button onclick="login()">Login</button>
</div>

<div id="app-section" style="display:none">
  <p>Logged in as <b id="who"></b> <button onclick="logout()">Log out</button></p>

  <h2>Add expense</h2>
  <input id="exp-amount" type="number" step="0.01" placeholder="Amount">
  <input id="exp-category" placeholder="Category">
  <input id="exp-description" placeholder="Description">
  <button onclick="addExpense()">Add</button>

  <h2>Spending summary</h2>
<p>Overall total: <b id="overall-total">0</b></p>
<table border="1" cellpadding="6">
  <thead><tr><th>Category</th><th>Total</th><th>Count</th></tr></thead>
  <tbody id="summary-rows"></tbody>
</table>

  <h2>Your expenses</h2>
  <label>Filter by category:
    <select id="filter" onchange="loadExpenses()">
      <option value="">All</option>
    </select>
  </label>
  <p>Total: <b id="total">0</b> (<span id="count">0</span> items)</p>
  <table border="1" cellpadding="6">
    <thead><tr><th>Category</th><th>Amount</th><th>Description</th><th></th></tr></thead>
    <tbody id="expense-rows"></tbody>
  </table>
</div>

<p id="message"></p>

<script>
let token = null;

function show(msg) {
  document.getElementById("message").textContent = msg;
}

async function api(path, method = "GET", body = null) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = "Bearer " + token;
  const res = await fetch(path, {
    method: method,
    headers: headers,
    body: body ? JSON.stringify(body) : null
  });
  const data = await res.json();
  return { ok: res.ok, data: data };
}

async function register() {
  const r = await api("/api/register", "POST", {
    username: document.getElementById("reg-username").value,
    email: document.getElementById("reg-email").value,
    password: document.getElementById("reg-password").value
  });
  show(r.ok ? "Registered! Now log in." : r.data.error);
}

async function login() {
  const username = document.getElementById("login-username").value;
  const r = await api("/api/login", "POST", {
    username: username,
    password: document.getElementById("login-password").value
  });
  if (r.ok) {
    token = r.data.access_token;
    document.getElementById("who").textContent = username;
    document.getElementById("auth-section").style.display = "none";
    document.getElementById("app-section").style.display = "block";
    show("");
    refresh();
  } else {
    show(r.data.error);
  }
}

function logout() {
  token = null;
  document.getElementById("auth-section").style.display = "block";
  document.getElementById("app-section").style.display = "none";
  show("");
  document.getElementById("expense-rows").innerHTML = "";
}
async function loadExpenses() {
  const category = document.getElementById("filter").value;
const path = category
  ? "/api/expenses/category/" + encodeURIComponent(category)
  : "/api/expenses";
const r = await api(path);
  if (!r.ok) { show(r.data.error || r.data.msg); return; }

  const tbody = document.getElementById("expense-rows");
  tbody.innerHTML = "";
  for (const e of r.data.expenses) {
    const tr = document.createElement("tr");
    for (const text of [e.category, e.amount, e.description]) {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    }
    const td = document.createElement("td");
    const btn = document.createElement("button");
    btn.textContent = "Delete";
    btn.onclick = () => deleteExpense(e.id);
    td.appendChild(btn);
    tr.appendChild(td);
    tbody.appendChild(tr);
  }
  document.getElementById("total").textContent = r.data.total;
  document.getElementById("count").textContent = r.data.count;
}

async function addExpense() {
  const r = await api("/api/expenses", "POST", {
    amount: document.getElementById("exp-amount").value,
    category: document.getElementById("exp-category").value,
    description: document.getElementById("exp-description").value
  });
  if (r.ok) {
    for (const id of ["exp-amount", "exp-category", "exp-description"]) {
      document.getElementById(id).value = "";
    }
    show("Expense added.");
    refresh();
  } else {
    show(r.data.error || r.data.msg);
  }
}

async function deleteExpense(id) {
  const r = await api("/api/expenses/" + id, "DELETE");
  show(r.ok ? "Expense deleted." : (r.data.error || r.data.msg));
  if (r.ok) refresh();
}
async function loadSummary() {
  const r = await api("/api/expenses/summary");
  if (!r.ok) { show(r.data.error || r.data.msg); return; }

  const select = document.getElementById("filter");
  const previous = select.value;
  select.innerHTML = "";
  const all = document.createElement("option");
  all.value = "";
  all.textContent = "All";
  select.appendChild(all);

  const tbody = document.getElementById("summary-rows");
  tbody.innerHTML = "";
  for (const [category, info] of Object.entries(r.data.summary)) {
    const tr = document.createElement("tr");
    for (const text of [category, info.total, info.count]) {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    }
    tbody.appendChild(tr);

    const opt = document.createElement("option");
    opt.value = category;
    opt.textContent = category;
    select.appendChild(opt);
  }

  select.value = previous;
  if (select.selectedIndex === -1) select.value = "";
  document.getElementById("overall-total").textContent = r.data.overall_total;
}

async function refresh() {
  await loadSummary();
  await loadExpenses();
}
</script>
</body>
</html>"""