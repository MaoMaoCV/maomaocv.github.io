// Styles for the copy button
// Styles for the copy button
const buttonStyles = "position: absolute; top: 10px; right: 10px; background-color: #2d2d2d; border: none; color: white; padding: 5px 10px; cursor: pointer; transition: background-color 0.3s ease;";
const buttonHoverStyles = "background-color: #1a1a1a;";

// Targeting both .highlighter-rouge and .highlight blocks
const codeBlocks = document.querySelectorAll('.code-header + .highlighter-rouge, .highlight');

codeBlocks.forEach((codeBlock) => {
  // Create the copy button
  const copyButton = document.createElement('button');
  copyButton.innerText = 'Copy';
  copyButton.style.cssText = buttonStyles;
  
  // Add hover effect
  copyButton.addEventListener('mouseover', () => {
    copyButton.style.backgroundColor = '#1a1a1a';
  });
  copyButton.addEventListener('mouseout', () => {
    copyButton.style.backgroundColor = '#2d2d2d';
  });
  
  // Add click event to copy content
  copyButton.addEventListener('click', () => {
    const code = codeBlock.innerText;
    window.navigator.clipboard.writeText(code);
    copyButton.innerText = 'Copied!';
    setTimeout(() => {
      copyButton.innerText = 'Copy';
    }, 2000);
  });
  
  // Embed the button inside the code block
  codeBlock.style.position = 'relative';
  codeBlock.appendChild(copyButton);
});

// // This assumes that you're using Rouge; if not, update the selector
// const codeBlocks = document.querySelectorAll('.code-header + .highlighter-rouge, .highlight');
// const copyCodeButtons = document.querySelectorAll('.copy-code-button');

// copyCodeButtons.forEach((copyCodeButton, index) => {
//   const code = codeBlocks[index].innerText;

//   copyCodeButton.addEventListener('click', () => {
//     // Copy the code to the user's clipboard
//     window.navigator.clipboard.writeText(code);

//     // Update the button text visually
//     const { innerText: originalText } = copyCodeButton;
//     copyCodeButton.innerText = 'Copied! Thank you for using maomaocv.github.io!';

//     // (Optional) Toggle a class for styling the button
//     copyCodeButton.classList.add('copied');

//     // After 2 seconds, reset the button to its initial UI
//     setTimeout(() => {
//       copyCodeButton.innerText = originalText;
//       copyCodeButton.classList.remove('copied');
//     }, 2000);
//   });
// });
