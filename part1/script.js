function checkAnswers() {
    // Array of correct answers (make sure these match your questions)
    // All answers here are lowercase for easy comparison
    const correctAnswers = [
        "rose",       // Q1: Mom's favorite flower
        "chicago",    // Q2: Dad's birthplace example
        "marie",      // Q3: Aunt Susan's middle name example
        "fishing",    // Q4: Grandpa's favorite hobby example
        "july",       // Q5: Grandma's birthday month example
        "buddy",      // Q6: Family's first pet example
        "italy",      // Q7: Country immigrated from example
        "doctor",     // Q8: Uncle Tom's profession example
        "blue",       // Q9: Cousin Sarah's favorite color example
        "cabin"       // Q10: Where last Christmas was spent example
    ];

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; // clear previous results

    let allCorrect = true;
    for (let i = 1; i <= 10; i++) {
        const userAnswer = document.getElementById(`answer${i}`).value.trim().toLowerCase();
        const listItem = document.getElementById(`answer${i}`).parentNode; // li element

        // Remove previous feedback classes if any
        listItem.classList.remove('correct', 'incorrect');

        if (userAnswer === correctAnswers[i - 1]) {
            listItem.classList.add('correct');
        } else {
            listItem.classList.add('incorrect');
            allCorrect = false;
        }
    }

    if (allCorrect) {
        resultDiv.classList.remove('incorrect');
        resultDiv.classList.add('correct');
        resultDiv.innerHTML = "🎉 All answers are correct! Proceed to the next step!";
    } else {
        resultDiv.classList.remove('correct');
        resultDiv.classList.add('incorrect');
        resultDiv.innerHTML = "❌ Some answers are incorrect. Please review and try again!";
    }
}
