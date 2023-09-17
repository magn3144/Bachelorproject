document.addEventListener('DOMContentLoaded', function () {
    // Query active tab (only in the current window)
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const tab = tabs[0];
        const tabId = tab.id;
        const tabUrl = tab.url;

        const extensionURL = `extension_window.html?tabId=${tabId}&tabUrl=${tabUrl}`;
        chrome.tabs.create({ 'url': extensionURL });
    });
});