// Custom Termynal
console.log('Termynal loaded');

document.addEventListener("DOMContentLoaded", function () {
    // Find all termynal blocks
    const termynals = document.querySelectorAll(".termy");
    console.log("Found termynals:", termynals.length);

    termynals.forEach(termynal => {
        const addCopyButton = () => {
            if (termynal.querySelector('.termynal-copy-button')) return;

            // Create copy button
            const button = document.createElement("button");
            button.className = "termynal-copy-button";
            button.innerHTML = `
                <span class="termynal-copy-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 21H8V7h11m0-2H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2m-3-4H4a2 2 0 0 0-2 2v14h2V3h12V1z"/></svg>
                </span>
                <span class="termynal-copy-feedback">Copied!</span>
            `;
            button.setAttribute("aria-label", "Copy to clipboard");

            // Add button to terminal
            termynal.appendChild(button);

            // Handle click
            button.addEventListener("click", () => {
                // Extract text: only lines with data-ty="input"
                const inputLines = termynal.querySelectorAll('[data-ty="input"]');
                const lines = [];

                inputLines.forEach(line => {
                    let text = line.textContent;
                    // Remove generic prompt if present (naive check)
                    if (text.startsWith("$ ")) {
                        text = text.substring(2);
                    }
                    // Termynal might use data-ty-prompt, handle that:
                    const prompt = line.getAttribute("data-ty-prompt") || "$";
                    if (line.textContent.startsWith(prompt)) {
                        // Usually termynal keeps prompt in css/attr, not textContent, but check just in case
                    }

                    lines.push(text);
                });
                let textToCopy = lines.join("\\n");

                // Fallback: if no input lines found or empty, copy everything that looks like code
                if (!textToCopy) {
                    textToCopy = termynal.textContent;
                }

                // Copy to clipboard
                navigator.clipboard.writeText(textToCopy.trim()).then(() => {
                    button.classList.add("copied");
                    setTimeout(() => {
                        button.classList.remove("copied");
                    }, 2000);
                }).catch(err => {
                    console.error("Failed to copy:", err);
                });
            });
        };

        // Initial add
        addCopyButton();

        // Observer to re-add on restart (which clears innerHTML)
        const observer = new MutationObserver((mutations) => {
            addCopyButton();
        });

        observer.observe(termynal, { childList: true });
    });
});
