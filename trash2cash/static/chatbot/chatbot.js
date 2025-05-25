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
        <div id="chat-header">Trash2Cash Bot <span id="close-chat" style="cursor:pointer; float:right;">&times;</span></div>
        <div id="chat-box" style="flex: 1; overflow-y: auto; padding: 10px;"></div>
        <input type="text" id="chat-input" placeholder="Type a message..." style="width: 100%; padding: 8px;" />
    `;
    document.body.appendChild(chatContainer);
  
    // Add basic styles (optional but improves display)
    const style = document.createElement("style");
    style.textContent = `
        #chatbot-icon {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #007bff;
            color: white;
            padding: 10px 15px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 24px;
            z-index: 1000;
        }
        #chat-container {
            position: fixed;
            bottom: 70px;
            right: 20px;
            width: 300px;
            height: 400px;
            background: white;
            border: 1px solid #ccc;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            z-index: 1000;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        #chat-header {
            background: #007bff;
            color: white;
            padding: 10px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            font-weight: bold;
        }
        .user-msg {
            text-align: right;
            margin: 5px;
            color: #007bff;
        }
        .bot-msg {
            text-align: left;
            margin: 5px;
            color: #444;
        }
    `;
    document.head.appendChild(style);
  
    // Get elements
    const chatBox = chatContainer.querySelector("#chat-box");
    const chatInput = chatContainer.querySelector("#chat-input");
    const closeBtn = chatContainer.querySelector("#close-chat");
  
    // Toggle chat visibility on icon click
    chatbotIcon.addEventListener("click", () => {
      chatContainer.style.display =
        chatContainer.style.display === "none" ? "flex" : "none";
    });
  
    // Close button inside chat header
    closeBtn.addEventListener("click", () => {
      chatContainer.style.display = "none";
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
  