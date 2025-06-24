import React, { useEffect, useState } from "react";

const API_URL = "/tasks";

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("");
  const [form, setForm] = useState({ description: "", category: "" });
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    setLoading(true);
    try {
      const res = await fetch(API_URL);
      const data = await res.json();
      setTasks(data);
      setError("");
    } catch (e) {
      setError("Failed to load tasks");
    }
    setLoading(false);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.description.trim()) return;
    try {
      if (editId) {
        await fetch(`${API_URL}/${editId}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        });
      } else {
        await fetch(API_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        });
      }
      setForm({ description: "", category: "" });
      setEditId(null);
      fetchTasks();
    } catch (e) {
      setError("Failed to save task");
    }
  };

  const handleEdit = (task) => {
    setForm({ description: task.description, category: task.category });
    setEditId(task.id);
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this task?")) return;
    try {
      await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      fetchTasks();
    } catch (e) {
      setError("Failed to delete task");
    }
  };

  const filteredTasks = tasks.filter((t) => {
    const matchesSearch =
      t.description.toLowerCase().includes(search.toLowerCase()) ||
      t.category.toLowerCase().includes(search.toLowerCase());
    const matchesFilter = filter ? t.category === filter : true;
    return matchesSearch && matchesFilter;
  });

  const categories = Array.from(new Set(tasks.map((t) => t.category).filter(Boolean)));

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>To-Do List</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", gap: 8, marginBottom: 16 }}>
        <input
          name="description"
          value={form.description}
          onChange={handleChange}
          placeholder="Task description"
          style={{ flex: 2 }}
          required
        />
        <input
          name="category"
          value={form.category}
          onChange={handleChange}
          placeholder="Category"
          style={{ flex: 1 }}
        />
        <button type="submit">{editId ? "Update" : "Add"}</button>
        {editId && (
          <button type="button" onClick={() => { setEditId(null); setForm({ description: "", category: "" }); }}>
            Cancel
          </button>
        )}
      </form>
      <div style={{ marginBottom: 16 }}>
        <input
          value={search}
          onChange={e => setSearch(e.target.value)}
          placeholder="Search..."
          style={{ width: "60%", marginRight: 8 }}
        />
        <select value={filter} onChange={e => setFilter(e.target.value)}>
          <option value="">All Categories</option>
          {categories.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : (
        <ul style={{ listStyle: "none", padding: 0 }}>
          {filteredTasks.map(task => (
            <li key={task.id} style={{
              background: "#f9f9f9",
              marginBottom: 8,
              padding: 12,
              borderRadius: 6,
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between"
            }}>
              <span>
                <strong>{task.description || <em>(No description)</em>}</strong>
                {task.category && (
                  <span style={{
                    background: "#e0e0e0",
                    borderRadius: 4,
                    padding: "2px 8px",
                    marginLeft: 8,
                    fontSize: 12
                  }}>{task.category}</span>
                )}
              </span>
              <span>
                <button onClick={() => handleEdit(task)} style={{ marginRight: 8 }}>Edit</button>
                <button onClick={() => handleDelete(task.id)} style={{ color: "red" }}>Delete</button>
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
