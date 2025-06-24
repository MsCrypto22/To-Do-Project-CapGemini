import express from "express";
import cors from "cors";
import fs from "fs";
import path from "path";

const app = express();
const PORT = 3001;
const DATA_PATH = path.resolve("../data/test_data.json");

app.use(cors());
app.use(express.json());

function readTasks() {
  return JSON.parse(fs.readFileSync(DATA_PATH, "utf-8"));
}

function writeTasks(tasks) {
  fs.writeFileSync(DATA_PATH, JSON.stringify(tasks, null, 2));
}

app.get("/tasks", (req, res) => {
  res.json(readTasks());
});

app.post("/tasks", (req, res) => {
  const tasks = readTasks();
  const newTask = req.body;
  newTask.id = tasks.length ? Math.max(...tasks.map(t => t.id)) + 1 : 1;
  tasks.push(newTask);
  writeTasks(tasks);
  res.status(201).json(newTask);
});

app.put("/tasks/:id", (req, res) => {
  const tasks = readTasks();
  const id = parseInt(req.params.id);
  const idx = tasks.findIndex(t => t.id === id);
  if (idx === -1) return res.status(404).json({ error: "Task not found" });
  tasks[idx] = { ...tasks[idx], ...req.body, id };
  writeTasks(tasks);
  res.json(tasks[idx]);
});

app.delete("/tasks/:id", (req, res) => {
  let tasks = readTasks();
  const id = parseInt(req.params.id);
  const idx = tasks.findIndex(t => t.id === id);
  if (idx === -1) return res.status(404).json({ error: "Task not found" });
  const deleted = tasks[idx];
  tasks = tasks.filter(t => t.id !== id);
  writeTasks(tasks);
  res.json(deleted);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
}); 