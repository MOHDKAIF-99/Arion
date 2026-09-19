// ===== Shared chat helper (used by cosmo.js and eris.js) =====

function addMessage(text, sender) {
  const chatWindow = document.getElementById("chatWindow");
  const bubble = document.createElement("div");
  bubble.classList.add("message", sender === "user" ? "user-message" : "bot-message");
  bubble.textContent = text;
  chatWindow.appendChild(bubble);

  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function getAndClearInput() {
  const input = document.getElementById("chatInput");
  const value = input.value.trim();
  input.value = "";
  return value;
}

function wireChatInput(onSend) {
  const input = document.getElementById("chatInput");
  const sendBtn = document.getElementById("sendBtn");

  const trigger = () => {
    const text = getAndClearInput();
    if (!text) return;
    addMessage(text, "user");
    onSend(text);
  };
  sendBtn.addEventListener("click", trigger);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") trigger();
  });
}