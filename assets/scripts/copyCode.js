const codeHeaders = document.querySelectorAll('.code-header');
const codeBlocks = document.querySelectorAll('.code-header + .highlighter-rouge, .code-header + .highlight');

codeHeaders.forEach((codeHeader, index) => {
  const codeBlock = codeBlocks[index];
  const copyButton = codeHeader.querySelector('.copy-code-button');
  
  // Add click event to copy content
  copyButton.addEventListener('click', () => {
    const code = codeBlock.innerText;
    window.navigator.clipboard.writeText(code);
    const originalText = copyButton.innerText;
    copyButton.innerText = 'Copied!';
    setTimeout(() => {
      copyButton.innerText = originalText;
    }, 2000);
  });
});