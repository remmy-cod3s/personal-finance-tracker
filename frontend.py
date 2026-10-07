PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title> Remon's Finance Tracker</title>
<style>
/* ================================
   GLOBAL STYLES
================================ */

* {
  box-sizing: border-box;
}
#warning-message {
  text-align: center;
  font-weight: bold;
}

#warning-message {
  text-align: center;
  font-weight: bold;
  font-size: 17px;
}

:root {
  --black: #080808;
  --dark: #101010;
  --dark-2: #151515;
  --border: #333;
  --red: #ed1c2e;
  --red-dark: #b90f1e;
  --white: #f5f5f5;
  --gray: #a5a5a5;
}

body {
  margin: 0;
  padding: 0 3.5%;
  background: var(--black);
  color: var(--white);
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  min-height: 100vh;
}


/* ================================
   HEADER
================================ */

body > h1 {
  margin: 0 -3.8% 35px;
  padding: 28px 3.8%;
  background: linear-gradient(90deg, #0c0c0c, #111);
  border-bottom: 3px solid var(--red);

  font-size: 32px;
  font-weight: 700;
  color: white;
}

body > h1::first-letter {
  color: var(--red);
}

body > p:first-of-type {
  color: var(--gray);
  margin-top: -15px;
  margin-bottom: 25px;
}


/* ================================
   AUTH SECTION
================================ */

#auth-section {
  max-width: 550px;
  margin: 50px auto;
  padding: 35px;
  background: var(--dark);
  border: 1px solid #3a0b10;
  border-radius: 12px;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5);
}

#auth-section h2 {
  color: white;
  margin-top: 10px;
  margin-bottom: 18px;
}

#auth-section h2::before {
  content: "●";
  color: var(--red);
  margin-right: 10px;
  font-size: 14px;
}

#auth-section input {
  width: 100%;
  margin-bottom: 12px;
}


/* ================================
   INPUTS
================================ */

input,
select {
  background: #0d0d0d;
  color: white;
  border: 1px solid #3a3a3a;
  border-radius: 6px;
  padding: 12px 14px;
  font-size: 15px;
  outline: none;
  transition: 0.2s ease;
}

input::placeholder {
  color: #888;
}

input:focus,
select:focus {
  border-color: var(--red);
  box-shadow: 0 0 0 2px rgba(237, 28, 46, 0.12);
}

select {
  cursor: pointer;
}


/* ================================
   BUTTONS
================================ */

button {
  background: var(--red);
  color: white;
  border: 1px solid var(--red);
  border-radius: 6px;
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s ease;
}

button:hover {
  background: #ff2638;
  border-color: #ff2638;
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0);
}


/* ================================
   LOGGED-IN MESSAGE
================================ */

#app-section > p:first-child {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 8px;

  margin: -15px 0 30px;
  color: var(--gray);
}

#who {
  color: var(--red);
}

#app-section > p:first-child button {
  background: transparent;
  border-color: var(--red);
  color: var(--red);
  padding: 7px 14px;
}

#app-section > p:first-child button:hover {
  background: var(--red);
  color: white;
}


/* ================================
   MAIN SECTIONS
================================ */

#app-section > h2,
#form-title {
  color: white;
}

#app-section > h2::before {
  color: var(--red);
}


/* Add Expense Card */

#app-section > h2:nth-of-type(1) {
  display: none;
}

#form-title {
  margin: 0;
  padding: 0;
}

#form-title::before {
  content: "+";
  display: inline-flex;
  align-items: center;
  justify-content: center;

  width: 28px;
  height: 28px;
  margin-right: 12px;

  background: var(--red);
  border-radius: 50%;
  color: white;
}

#form-title,
#form-title ~ input,
#form-title ~ button {
  /* handled by the expense form layout */
}


/* ================================
   EXPENSE FORM
================================ */

#form-title {
  margin-bottom: 18px;
}

#form-title ~ input {
  margin-right: 12px;
}

#exp-amount {
  width: 24%;
}

#exp-category {
  width: 24%;
}

#exp-description {
  width: 39%;
}

#save-btn {
  min-width: 100px;
}

#cancel-btn {
  background: transparent;
  color: var(--red);
}


/* ================================
   CARDS
================================ */

#form-title,
#overall-total,
#summary-rows,
#expense-rows {
  position: relative;
}

#app-section {
  padding-bottom: 50px;
}


/* Add expense section */

#form-title {
  margin-top: 0;
}

#form-title,
#form-title ~ input,
#form-title ~ button {
  /* visual grouping */
}


/* Create card-like sections using the headings */

#form-title {
  background: linear-gradient(90deg, #0d0d0d, #111);
  border: 1px solid #551019;
  border-radius: 10px 10px 0 0;
  padding: 22px;
}


/* ================================
   SPENDING SUMMARY
================================ */

#app-section > h2:nth-of-type(2) {
  margin-top: 45px;
  padding: 22px 22px 5px;

  background: #0d0d0d;
  border-left: 1px solid #551019;
  border-right: 1px solid #551019;
  border-top: 1px solid #551019;

  border-radius: 10px 10px 0 0;
}

#overall-total {
  display: inline-block;
  margin-bottom: 15px;
  color: var(--red);
  font-size: 22px;
}


/* ================================
   TABLES
================================ */

table {
  width: 100%;
  border-collapse: collapse;
  background: #0c0c0c;
  border: 1px solid #333;
  color: white;
}

th {
  background: linear-gradient(90deg, #c80f20, #ed1c2e);
  color: white;
  text-align: left;
  padding: 13px 15px;
  font-weight: 700;
}

td {
  padding: 13px 15px;
  border: 1px solid #282828;
}

tbody tr {
  transition: background 0.2s ease;
}

tbody tr:hover {
  background: #171717;
}


/* ================================
   SUMMARY TABLE
================================ */

#summary-rows {
  display: table-row-group;
}


/* ================================
   YOUR EXPENSES
================================ */

#app-section > h2:nth-of-type(3) {
  margin-top: 45px;
  padding: 22px 22px 15px;

  background: #0d0d0d;
  border: 1px solid #551019;
  border-bottom: none;

  border-radius: 10px 10px 0 0;
}

#filter {
  margin-left: 8px;
  min-width: 150px;
}

#total {
  color: var(--red);
  font-size: 20px;
}

#count {
  color: #ccc;
}


/* ================================
   EXPENSE TABLE
================================ */

#expense-rows td:last-child {
  white-space: nowrap;
  text-align: center;
}

#expense-rows button {
  margin: 0 3px;
  padding: 7px 13px;
}

#expense-rows button:first-child {
  background: transparent;
  color: white;
  border-color: var(--red);
}

#expense-rows button:first-child:hover {
  background: var(--red);
}

#expense-rows button:last-child {
  background: var(--red);
}


/* ================================
   STATUS MESSAGE
================================ */

#message {
  margin: 20px 0;
  color: #aaa;
  font-style: italic;
}

#message:not(:empty) {
  color: #ddd;
}


/* ================================
   MOBILE RESPONSIVENESS
================================ */

@media (max-width: 900px) {

  body {
    padding: 0 20px;
  }

  body > h1 {
    margin-left: -20px;
    margin-right: -20px;
    padding-left: 20px;
    padding-right: 20px;
    font-size: 26px;
  }

  #exp-amount,
  #exp-category,
  #exp-description {
    width: 100%;
    margin: 5px 0;
  }

  #save-btn,
  #cancel-btn {
    margin-top: 8px;
  }

  table {
    display: block;
    overflow-x: auto;
    white-space: nowrap;
  }

  #app-section > p:first-child {
    justify-content: flex-start;
    flex-wrap: wrap;
  }
}


@media (max-width: 600px) {

  body {
    font-size: 14px;
  }

  body > h1 {
    font-size: 22px;
  }

  #auth-section {
    padding: 22px;
  }

  th,
  td {
    padding: 10px;
  }

  #filter {
    margin-left: 0;
    margin-top: 8px;
  }
}
#toast-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: min(360px, calc(100vw - 40px));
}

.toast {
  background: #151515;
  color: var(--white);
  border: 1px solid #333;
  border-left: 4px solid var(--gray);
  border-radius: 6px;
  padding: 12px 16px;
  font-size: 15px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
  animation: toast-in 0.2s ease;
}

.toast.error { border-left-color: var(--red); }
.toast.success { border-left-color: #2ecc71; }

.toast.leaving {
  opacity: 0;
  transform: translateX(20px);
  transition: 0.25s ease;
}

@keyframes toast-in {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: none; }
}

@media (prefers-reduced-motion: reduce) {
  .toast, .toast.leaving { animation: none; transition: none; }
}

</style>


</head>
<body>
<h1>Remon's personal Finance Tracker</h1>
<p id="warning-message"> Finance Tracker for Majestic 6'4 kings</p>



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
  <h2 id="form-title">Add expense</h2>
    <input id="exp-amount" type="number" step="0.01" placeholder="Amount">
    <input id="exp-category" placeholder="Category">
    <input id="exp-description" placeholder="Description">
    <button id="save-btn" onclick="saveExpense()">Add</button>
    <button id="cancel-btn" onclick="cancelEdit()" style="display:none">Cancel</button>

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
    <thead><tr><th>Date</th><th>Category</th><th>Amount</th><th>Description</th><th></th></tr></thead>
    <tbody id="expense-rows"></tbody>
  </table>
</div>

<p id="toast-container"></p>

<script>
let token = null;
let editingId = null;
function show(msg, type = "info") {
  if (!msg) return;
  const container = document.getElementById("toast-container");
  while (container.children.length >= 3) container.firstChild.remove();
  const toast = document.createElement("div");
  toast.className = "toast " + type;
  toast.setAttribute("role", type === "error" ? "alert" : "status");
  toast.textContent = msg;
  container.appendChild(toast);
  setTimeout(() => {
    toast.classList.add("leaving");
    setTimeout(() => toast.remove(), 300);
  }, type === "error" ? 6000 : 3500);
}
async function api(path, method = "GET", body = null) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = "Bearer " + token;
  let res;
  try {
    res = await fetch(path, {
      method: method,
      headers: headers,
      body: body ? JSON.stringify(body) : null
    });
  } catch (err) {
    return { ok: false, data: { error: "Could not reach the server. Check your connection." } };
  }
  let data;
  try {
    data = await res.json();
  } catch (err) {
    data = { error: "Server returned status " + res.status };
  }
  if (res.status === 401 && token) {
    logout();
    return { ok: false, data: { error: "Your session expired. Please log in again." } };
  }
  return { ok: res.ok, data: data };
}
async function register() {
  const r = await api("/api/register", "POST", {
    username: document.getElementById("reg-username").value,
    email: document.getElementById("reg-email").value,
    password: document.getElementById("reg-password").value
  });
  if (r.ok) show("Account created. You can now log in.", "success");
  else show(r.data.error || "Registration failed.", "error");
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
    show("Welcome back, " + username + ".", "success");
    refresh();
  } else {
    show(r.data.error || "Login failed.", "error");
  }
}
function logout() {
  token = null;
  resetForm();
  document.getElementById("auth-section").style.display = "block";
  document.getElementById("app-section").style.display = "none";
  document.getElementById("expense-rows").innerHTML = "";
  document.getElementById("summary-rows").innerHTML = "";
  document.getElementById("filter").value = "";
}
function formatDate(value) {
  return value ? value.slice(0, 10) : "";
}
async function loadExpenses() {
  const category = document.getElementById("filter").value;
  const path = category
    ? "/api/expenses/category/" + encodeURIComponent(category)
    : "/api/expenses";
  const r = await api(path);
  if (!r.ok) { show(r.data.error || r.data.msg, "error"); return; }
  const tbody = document.getElementById("expense-rows");
  tbody.innerHTML = "";
  for (const e of r.data.expenses) {
    const tr = document.createElement("tr");
    for (const text of [formatDate(e.date), e.category, e.amount, e.description]) {
      const td = document.createElement("td");
      td.textContent = text;
      tr.appendChild(td);
    }
    const td = document.createElement("td");
    const btn = document.createElement("button");
    btn.textContent = "Delete";
    btn.onclick = () => deleteExpense(e.id);
    const editBtn = document.createElement("button");
    editBtn.textContent = "Edit";
    editBtn.onclick = () => startEdit(e);
    td.appendChild(editBtn);
    td.appendChild(btn);
    tr.appendChild(td);
    tbody.appendChild(tr);
  }
  document.getElementById("total").textContent = r.data.total;
  document.getElementById("count").textContent = r.data.count;
}
function startEdit(e) {
  editingId = e.id;
  document.getElementById("exp-amount").value = e.amount;
  document.getElementById("exp-category").value = e.category;
  document.getElementById("exp-description").value = e.description;
  document.getElementById("form-title").textContent = "Edit expense";
  document.getElementById("save-btn").textContent = "Save";
  document.getElementById("cancel-btn").style.display = "inline";
  window.scrollTo(0, 0);
}
function resetForm() {
  editingId = null;
  for (const id of ["exp-amount", "exp-category", "exp-description"]) {
    document.getElementById(id).value = "";
  }
  document.getElementById("form-title").textContent = "Add expense";
  document.getElementById("save-btn").textContent = "Add";
  document.getElementById("cancel-btn").style.display = "none";
}
function cancelEdit() {
  resetForm();
}
async function saveExpense() {
  const body = {
    amount: document.getElementById("exp-amount").value,
    category: document.getElementById("exp-category").value,
    description: document.getElementById("exp-description").value
  };
  const wasEditing = editingId !== null;
  const r = wasEditing
    ? await api("/api/expenses/" + editingId, "PUT", body)
    : await api("/api/expenses", "POST", body);
  if (r.ok) {
    show(wasEditing ? "Expense updated." : "Expense added.", "success");
    resetForm();
    refresh();
  } else {
    show(r.data.error || r.data.msg, "error");
  }
}
async function deleteExpense(id) {
  if (editingId === id) resetForm();
  const r = await api("/api/expenses/" + id, "DELETE");
  if (r.ok) {
    show("Expense deleted.", "success");
    refresh();
  } else {
    show(r.data.error || r.data.msg, "error");
  }
}
async function loadSummary() {
  const r = await api("/api/expenses/summary");
  if (!r.ok) { show(r.data.error || r.data.msg, "error"); return; }
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
"""