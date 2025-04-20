# শহর এবং রুট সহ গ্রাফ

graph = {
    "Rangpur": [("Dhaka", 1000), ("Khulna", 600),("Bogura", 200)],
    "Khulna": [("Dhaka", 200)],
    "Dhaka": [("Chottagram", 600),("Khulna", 200)],
    "Chottagram": [("Dhaka", 600)],
    "Bogura": [("Dhaka", 500),("Rajshahi", 200)],
     "Dinajpur": [("Dhaka", 800),("Bogura", 100)],
     "Rajshahi": [("Dhaka", 700)],
}



budget = 600
min_cost = float('inf')
best_path = []

def dfs(current, destination, path, cost):
    global min_cost, best_path

    if cost > budget:
        return

    if current == destination:
        if cost < min_cost:
            min_cost = cost
            best_path = path.copy()
        return

    for neighbor, edge_cost in graph.get(current, []):
        if neighbor not in path:
            path.append(neighbor)
            dfs(neighbor, destination, path, cost + edge_cost)
            path.pop()

# শুধুমাত্র Rangpur → Dhaka
dfs("Dinajpur", "Dhaka", ["Dinajpur"], 0)

# ফলাফল দেখাও
print("🔍 Finding Best Path from Rangpur to Dhaka")
if best_path:
    print("✅ Best Path:", " -> ".join(best_path))
    print("💰 Total Cost:", min_cost, "BDT")
else:
    print("❌ No available path within BDT")
