function checkAnswers() {
    // Array of correct answers (make sure these match your questions)
    // All answers here are lowercase for easy comparison
    const correctAnswers = [
        "wollfs gate 14",       // Q1: Mom's favorite flower
        "gran canaria",    // Q2: Dad's birthplace example
        "18",      // Q3: Aunt Susan's middle name example
        "d",    // Q4: Grandpa's favorite hobby example
        "e",       // Q5: Grandma's birthday month example
        "f",      // Q6: Family's first pet example
        "g",      // Q7: Country immigrated from example
        "h",     // Q8: Uncle Tom's profession example
        "i",       // Q9: Cousin Sarah's favorite color example
        "j"       // Q10: Where last Christmas was spent example
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
        resultDiv.innerHTML = "🎉 gratulerer, helt riktiiiiig! Tage, sjekk ut denne: youtubelink, ";
    } else {
        resultDiv.classList.remove('correct');
        resultDiv.classList.add('incorrect');
        resultDiv.innerHTML = "❌ Some answers are incorrect. Please review and try again!";
    }
}
