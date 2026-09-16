import json

transcript_path = r"C:\Users\elitebook840g89319\.gemini\antigravity-ide\brain\6eeba121-71ca-46d4-8459-b37ec5fe642f\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        if d.get("type") in ["USER_INPUT", "PLANNER_RESPONSE"] and d.get("content"):
            text = d['content'][:250].encode('ascii', 'backslashreplace').decode('ascii')
            print(f"{d['type']}: {text}")
            print("-" * 50)
