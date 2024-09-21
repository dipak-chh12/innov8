// static/script.js
async function sendMessage() {
    const inputText = document.getElementById("input").value;
    document.getElementById("input").value = ''; // Clear input field
    const chatArea = document.getElementById("chat-area");

    chatArea.innerHTML += `<p class="user-message"><strong>User:</strong> ${inputText}</p>`;
    chatArea.scrollTop = chatArea.scrollHeight; // Scroll to the bottom

    try {
        const response = await fetch('http://127.0.0.1:5000/api/generate-text', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify({ prompt: inputText })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        chatArea.innerHTML += `<p class="bot-message"><strong>Bot:</strong> ${data.generated_text}</p>`;
    } catch (error) {
        chatArea.innerHTML += `<p class="bot-message"><strong>Bot:</strong> Error occurred: ${error.message}</p>`;
    }
    
    chatArea.scrollTop = chatArea.scrollHeight; // Scroll to the bottom
}
