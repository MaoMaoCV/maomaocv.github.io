var codeBlocks = document.querySelectorAll('pre.highlight');

var copyButton = document.createElement('button');
copyButton.type = 'button';
copyButton.ariaLabel = 'Copy code to clipboard';
copyButton.innerText = 'Copy';

codeBlock.append(copyButton);
pre.highlight > button {
  opacity: 0;
}
pre.highlight:hover > button {
  opacity: 1;
}
pre.highlight > button:active,
pre.highlight > button:focus {
  opacity: 1;
}
codeBlocks.forEach(function (codeBlock) {
  // ...
  copyButton.addEventListener('click', function () {
    var code = codeBlock.querySelector('code').innerText.trim();
    window.navigator.clipboard.writeText(code);
  });
});
copyButton.innerText = 'Copied';
var fourSeconds = 4000;

setTimeout(function () {
  copyButton.innerText = 'Copy';
}, fourSeconds);