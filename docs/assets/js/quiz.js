// Basic Quiz Interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log('Quiz JS loaded');

    // Use event delegation for robustness
    document.body.addEventListener('click', function (e) {
        // Check if clicked element is a quiz option
        const option = e.target.closest('.quiz-option');
        if (!option) return;

        // Prevent if disabled (though we removed the disabled state logic for siblings, 
        // we might want to respect it if added by other means)
        if (option.classList.contains('disabled')) return;

        const parent = option.parentElement;

        // Allow changing answer: Remove state from siblings
        parent.querySelectorAll('.quiz-option').forEach(opt => {
            opt.classList.remove('selected', 'correct', 'incorrect');
            opt.classList.remove('disabled');
        });

        option.classList.add('selected');

        // Check answer
        const isCorrect = option.getAttribute('data-correct') === 'true';
        const feedbackText = option.getAttribute('data-feedback');
        const quizItem = option.closest('.quiz-item') || option.closest('.quiz-container');
        console.log('Quiz Container found:', quizItem);
        const feedbackEl = quizItem ? quizItem.querySelector('.quiz-feedback') : null;
        console.log('Feedback El found:', feedbackEl);

        // Apply visual state to the option
        option.classList.add(isCorrect ? 'correct' : 'incorrect');

        if (feedbackEl) {
            feedbackEl.innerHTML = (isCorrect ? '<strong>Correto!</strong> ' : '<strong>Incorreto.</strong> ') + (feedbackText || '');
            feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'correct' : 'incorrect');
            feedbackEl.style.display = 'block';
        }
    });
});
