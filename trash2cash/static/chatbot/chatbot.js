document.addEventListener("DOMContentLoaded", function () {
  // Create the chatbot icon
  const chatbotIcon = document.createElement("div");
  chatbotIcon.id = "chatbot-icon";
  chatbotIcon.innerText = "💬";
  document.body.appendChild(chatbotIcon);

  // Create the chat container
  const chatContainer = document.createElement("div");
  chatContainer.id = "chat-container";
  chatContainer.style.display = "none"; // Hidden by default
  chatContainer.innerHTML = `
      <div id="chat-header">Trash2Cash Bot</div>
      <div id="chat-box"></div>
      <input type="text" id="chat-input" placeholder="Type a message..." />
  `;
  document.body.appendChild(chatContainer);

  // Get elements
  const chatBox = document.getElementById("chat-box");
  const chatInput = document.getElementById("chat-input");

  // Toggle chat visibility on icon click
  chatbotIcon.addEventListener("click", () => {
      if (chatContainer.style.display === "none") {
          chatContainer.style.display = "flex";
      } else {
          chatContainer.style.display = "none";
      }
  });

  // Handle sending messages
  chatInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter" && chatInput.value.trim() !== "") {
          const message = chatInput.value;
          chatInput.value = "";
          appendMessage("You", message);

          fetch("/chat", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify({ message: message }),
          })
              .then((res) => res.json())
              .then((data) => {
                  appendMessage("Bot", data.response);
              })
              .catch((err) => {
                  appendMessage("Bot", "Oops! Something went wrong.");
                  console.error(err);
              });
      }
  });

  function appendMessage(sender, message) {
      const messageDiv = document.createElement("div");
      messageDiv.className = sender === "You" ? "user-msg" : "bot-msg";
      messageDiv.innerText = `${sender}: ${message}`;
      chatBox.appendChild(messageDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
  }
});
