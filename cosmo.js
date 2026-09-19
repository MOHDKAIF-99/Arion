// ===== Cosmo (Email Companion) logic =====

const COSMO_API_URL = "http://localhost:5000/api/cosmo/draft";

wireChatInput(async (userText) => {
  addMessage("Working on your draft...", "bot");

  try {
    const response = await fetch(COSMO_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: userText }),
    });

    const data = await response.json();

    if (data.success) {
      addMessage(data.message || "Draft created successfully.", "bot");
      showNotification();
    } else {
      addMessage(data.message || "Something went wrong creating the draft.", "bot");
    }
  } catch (err) {
    addMessage("Couldn't reach Cosmo's backend. Is the server running?", "bot");
    console.error("Cosmo API error:", err);
  }
});

function showNotification() {
  const banner = document.getElementById("notifyBanner");
  banner.hidden = false;
  setTimeout(() => {
    banner.hidden = true;
  }, 6000);
}