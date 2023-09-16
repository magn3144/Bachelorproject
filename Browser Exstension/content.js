function getXPath(element) {
    if (element.id !== '') {
      return 'id("' + element.id + '")';
    }
    if (element === document.body) {
      return element.tagName;
    }
    let sibling = element;
    let count = 1;
    while (sibling = sibling.previousElementSibling) {
      if (sibling.tagName === element.tagName) {
        count++;
      }
    }
    return getXPath(element.parentNode) + '/' + element.tagName + '[' + count + ']';
}

function getHTML (event) {
  event.preventDefault();
  const html = event.target.outerHTML;
  const xpath = getXPath(event.target);
  console.log("content.js: " + html);
  console.log("content.js: " + xpath);
  chrome.runtime.sendMessage({html: html, xpath: xpath});
}

function addClickListener() {
  document.addEventListener('click', getHTML);
}

function removeClickListener() {
  document.removeEventListener('click', getHTML);
}

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.message === "start") {
    addClickListener();
  }
  else if (message.message === "stop") {
    removeClickListener();
  }
});