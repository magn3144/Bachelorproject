let latestMessage = null;

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  latestMessage = message;
  console.log("background.js: " + message);
});

chrome.runtime.onConnect.addListener(function(port) {
  if (port.name === "popup") {
    port.onMessage.addListener(function(msg) {
      if (msg === "getLatest") {
        port.postMessage(latestMessage);
      }
    });
  }
});