/**
 * Rock Paper Scissors (rps)
 * 
 * Create a getComputerChoice function
 *      Function takes no parameters
 *      Function returns a random rock, paper, or scissors
 *          Generate a random number from 0 to 2 (0, 1, or 2)
 *          If 0, return "rock"
 *          If 1, return paper
 *          If 2, return scissors
 *      
 * Create a playRound function
 *      Function takes two parameters
 *          playerSelection - string, player's choice of RPS in any case
 *          computerSelection - string, takes getComputerChoice output
 *      Set playerSelection to lowercase.
 *      If playerSelection equals computerSelection, return "A tie!"
 *          Else, Switch(computerSelection)
 *              rock, if player chose paper, return "You win! Paper beats Rock."
 *                  else, return "You lose! Rock beats Scissors."
 *              paper, if player chose scissors, return "You win! Scissors beats Paper."
 *                  else, return "You lose! Paper beats Rock."
 *              scissors, if player chose rock, return "You win! Rock beats Scissors."
 *                  else, return "You lose! Scissors beats Paper."
 * 
 * Create a game function.
 *      Function takes no parameters
 *      Call playRound() five times.
 *          Declare what move the player chose.
 *          Declare what move the comuter chose.
 *          Declare the winner of the round.
 *          Print score.
 */

/**
 * Returns a randomly generated rock, paper, or scissors.
 * 
 * @returns {string} Randomly generated output for rock paper scissors.
 */
function getComputerChoice() {
    let computerChoice = Math.floor( Math.random() * 3 );     // Generates random number between 0 and 2
    switch (computerChoice) {                                 // Returns randomly generated computer choice
        case 0:
            return "rock"
        case 1:
            return "paper"
        case 2:
            return "scissors"
    }
}

/**
 * Returns the results of a round of Rock Paper Scissors.
 * 
 * @param {string} playerSelection Player's input for round.
 * @param {string} computerSelection Computer's input for round.
 * @returns {string} Results of a round of Rock Paper Scissors.
 */
function playRound(playerSelection, computerSelection) {
    playerChoice = playerSelection.toLowerCase();           // Converts player's choice to lowercase

    if (playerChoice == computerSelection) {                // Check for tie
        return [0, "A tie!"]
    }

    switch (computerSelection) {                            // Check depends on computer choice
    case "rock":
            if (playerChoice == "paper") {
                return [1, "You win! Paper beats Rock."]
            } else {
                return [-1, "You lose! Rock beats Scissors."]
            }
        case "paper":
            if (playerChoice == "scissors") {
                return [1, "You win! Scissors beats Paper."]
            } else {
                return [-1, "You lose! Paper beats Rock."]
            }
        case "scissors":
            if (playerChoice == "rock") {
                return [1, "You win! Rock beats Scissors."]
            } else {
                return [-1, "You lose! Scissors beats Paper."]
            }
    }
}

/**
 * Returns the results of five games of rock paper scissors.
 * 
 * @returns {string} Results of five games of rock paper scissors.
 */
function game() {
    let playerScore = 0;        // Set initial player score
    let computerScore = 0;      // Set initial computer score

    for (i = 0; i < 5; i++) {
        const playerSelection = String(window.prompt("Enter rock paper scissors choice:"));     // Prompt user for choice
        const computerSelection = getComputerChoice();                                          // Acquire computer choice

        const [gamePoints, gameMessage] = playRound(playerSelection, computerSelection);
        console.log(gameMessage);   // Print round specific results

        if (gamePoints == 1) {      // Tally score for round
            playerScore += 1;
        } else if (gamePoints == -1) {
            computerScore += 1;
        }
    }

    if (playerScore > computerScore) {          // Print game results
        return "Player wins best out of five rounds!"
    } else if (playerScore < computerScore) {
        return "Computer wins best out of five rounds!"
    } else {
        return "Player and Computer tie!"
    }
}

console.log(game());