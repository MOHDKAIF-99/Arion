// ===== Eris (General Assistant) logic =====

const ERIS_API_BASE = "http://localhost:5000/api/eris";

document.querySelectorAll(".quick-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const action = btn.dataset.action;
    const prompts = {
      weather: "What's the weather today?",
      calculator: "Calculate: ",
      youtube: "Play a video about ",
      music: "Play some music",
    };
    const input = document.getElementById("chatInput");
    input.value = prompts[action] || "";
    input.focus();
  });
});

wireChatInput(async (userText) => {
  addMessage("Let me check...", "bot");

  try {
    const response = await fetch(`${ERIS_API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userText }),
    });

    const data = await response.json();
    addMessage(data.reply || "I couldn't find an answer for that.", "bot");
  } catch (err) {
    addMessage("Couldn't reach Eris's backend. Is the server running?", "bot");
    console.error("Eris API error:", err);
  }
});