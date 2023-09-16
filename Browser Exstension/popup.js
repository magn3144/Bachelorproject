let selectionMode = false;

// function executeContentScript() {
//   selectionMode = true;
//   chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     var tab = tabs[0];
//     chrome.scripting.executeScript({
//       target: {tabId: tab.id},
//       files: ['content.js']
//     });
//   });
// }

function sendStartMessage() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { "message": "start" });
  });
}

function sendStopMessage() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { "message": "stop" });
  });
}

document.addEventListener('DOMContentLoaded', function () {
  var startButton = document.getElementById('start');
  startButton.addEventListener('click', function() {
    if (selectionMode) {
      // If already in selection mode, and the button is clicked, then stop selection mode
      startButton.textContent = "Start";
      sendStopMessage();
      selectionMode = false;
    }
    else {
      // If not in selection mode, and the button is clicked, then start selection mode
      startButton.textContent = "Stop";
      sendStartMessage();
      selectionMode = true;
    }
  });
});

const port = chrome.runtime.connect({ name: "popup" });
port.postMessage("getLatest");
port.onMessage.addListener(function(msg) {
  document.getElementById('html').textContent = msg.html;
  document.getElementById('xpath').textContent = msg.xpath;
});