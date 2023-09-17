function sendStartMessage() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    let activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { "message": "start" });
  });
}

function sendStopMessage() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    let activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { "message": "stop" });
  });
}

function initializeStartButton() {
  console.log("popup.js: initializing start button");
  let selectionMode = localStorage.getItem('selectionMode');
  console.log("popup.js: selection mode 1: " + selectionMode);
  if (selectionMode === null) {
    localStorage.setItem('selectionMode', false);
    selectionMode = false;
  }
  else {
    selectionMode = (selectionMode === 'true');  // Convert string to boolean
  }
  console.log("popup.js: selection mode 2: " + selectionMode);
  let startButton = document.getElementById('start');
  startButton.addEventListener('click', function() {
    console.log("popup.js: selection mode 3: " + selectionMode);
    if (selectionMode) {
      // If already in selection mode, and the button is clicked, then stop selection mode
      startButton.textContent = "Start Selecting";
      sendStopMessage();
      selectionMode = false;
    }
    else {
      // If not in selection mode, and the button is clicked, then start selection mode
      startButton.textContent = "Stop Selecting";
      sendStartMessage();
      selectionMode = true;
    }
    console.log("popup.js: selection mode 4: " + selectionMode);
    localStorage.setItem('selectionMode', selectionMode);
  });
}

function initializeMessageListener() {
  console.log("popup.js: initializing message listener");
  const port = chrome.runtime.connect({ name: "popup" });
  port.postMessage("getLatest");
  port.onMessage.addListener(function(msg) {
    if (msg !== null) {
      console.log("popup.js: received message: " + msg);
      document.getElementById('html').textContent = msg.html;
      document.getElementById('xpath').textContent = msg.xpath;
    }
  });
}

initializeStartButton();
initializeMessageListener();