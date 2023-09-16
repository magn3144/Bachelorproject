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
  window.selectionMode = false;
  console.log("popup.js: DOMContentLoaded");
  let startButton = document.getElementById('start');
  startButton.addEventListener('click', function() {
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
  port.onMessage.addListener(function(msg) {
    if (msg !== null) {
      console.log("popup.js: received message: " + msg);
      document.getElementById('html').textContent = msg.html;
      document.getElementById('xpath').textContent = msg.xpath;
    }
  });
}

function checkFlagAndRun() {
  function checkFlag() {
    window.myExtensionHasRun = window.myExtensionHasRun || false;
    return window.myExtensionHasRun;
  }
  
  async function getActiveTabID() {
    let queryOptions = { active: true, currentWindow: true };
    let tabs = await chrome.tabs.query(queryOptions);
    return tabs[0].id;
  }

  // Inject code to check for flag
  let activeTabID = 0;
  getActiveTabID().then((tabIdResult) => {
    activeTabID = tabIdResult;
  }).then(() => {
    chrome.scripting.executeScript({ target: {tabId: activeTabID}, func: checkFlag }, (hasRunResult) => {
      if (chrome.runtime.lastError) {
        console.error(chrome.runtime.lastError);
        return;
      }

      const hasRun = hasRunResult[0].result;
      if (!hasRun) {
        console.log("This is the first time the extension has run on this page");

        function setFlagTrue() {
          window.myExtensionHasRun = true;
        }
  
        // Inject code to set flag
        chrome.scripting.executeScript({ target: {tabId: activeTabID}, func: setFlagTrue });
  
        initializeStartButton();
        initializeMessageListener();
      }
    });
  });
}

const port = chrome.runtime.connect({ name: "popup" });
//port.postMessage("getLatest");
checkFlagAndRun();