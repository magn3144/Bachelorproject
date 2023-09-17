function sendStartMessage() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        let activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { "message": "start" });
    });
}

function sendStopMessage() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        let activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { "message": "stop" });
    });
}

function initializeStartButton() {
    const port = chrome.runtime.connect({ name: "popup" });
    port.postMessage("getLatest");
    console.log("popup.js: initializing start button");
    window.selectionMode = false;
    console.log("popup.js: DOMContentLoaded");
    let startButton = document.getElementById('start');
    startButton.addEventListener('click', function () {
        console.log("popup.js: start button clicked");
        if (window.selectionMode) {
            // If already in selection mode, and the button is clicked, then stop selection mode
            startButton.textContent = "Start Selecting";
            sendStopMessage();
            window.selectionMode = false;
        }
        else {
            // If not in selection mode, and the button is clicked, then start selection mode
            startButton.textContent = "Stop Selecting";
            sendStartMessage();
            window.selectionMode = true;
        }
    });
}

function initializeMessageListener() {
    console.log("popup.js: initializing message listener");
    port.onMessage.addListener(function (msg) {
        if (msg !== null) {
            console.log("popup.js: received message: " + msg);
            document.getElementById('html').textContent = msg.html;
            document.getElementById('xpath').textContent = msg.xpath;
        }
    });
}

const urlParams = new URLSearchParams(window.location.search);
const tabId = urlParams.get('tabId');
const tabUrl = urlParams.get('tabUrl');
const targetTabId = parseInt(tabId);
console.log("popup.js: tabId: " + tabId);
console.log("popup.js: tabUrl: " + tabUrl);
console.log("popup.js: targetTabId: " + targetTabId);

initializeStartButton();
initializeMessageListener();