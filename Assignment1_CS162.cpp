/* Basic program algo
1. Generate Random number (1-50)
2. Diplay number
3. Ask user for guess on whether number is APD
4. Calulate APDness of random number
5. If user guess is correct, add 1 to user score
6. Ask user if they wish to play a second game
	7a. If score <10 and yes, start a new game
	7b. If no, exit program
*/

#include <iostream> // Standard I/O
#include <random>  // Needed for radom number generator
#include <time.h> // Used in the random number generator, to provide greater entropy
#include <math.h> // Required for basic math functions
#include <conio.h> // Provides getch/pause functionality


using namespace std;

void start_game(); // Primary game function
class Game; // Game elements

class Game {
	int rand_num;
	int user_guess;
	int determination;
	int score;
	void increment();
	void display();
public:
	Game();
	~Game();
	void random_number();
	void guess();
	void number_state(int);
	void display_results();
	int get_score();
	int get_rand();
};


int main() {
	srand((unsigned int)time(0)); // Seed random number generator
	start_game();
	return 0;
}

void start_game() {
	// General game control
	Game playtime;
	char replay;

	// Loops through the game functions while user desires to play
	do {
		playtime.random_number();
		playtime.guess();
		playtime.number_state(playtime.get_rand());
		playtime.display_results();
		do {
			cout << "Would you like to play again? [y/n]: ";
			cin >> replay;
			cin.clear();
			cin.ignore(256, '\n');
		} while ((toupper(replay) != 'N') && (toupper(replay) != 'Y')); // Control for non-y/n answers
	} while ((toupper(replay)=='Y') && (playtime.get_score() < 10)); // Repeat as long as players says yes, or until 10pts
}

void Game::random_number() {
	// Display a random number between 1 and 50
	rand_num = 1 + (rand() % 50);
}

void Game::number_state(int rand) {
	// Determine whether number is Deficient, Perfect, or Abundant
	// Return state of number: Deficient (1), Perfect (2) or Abundant (3)
	int divisors[50] = {0};
	int divisor_sum=0;
	for (int i = 1; i < rand; i++) {
		if (rand % i == 0) {
			divisors[i] = i;
		} else {
			divisors[i]=0;
		}
	}

	// Displays the proper divisors of the random number
	cout << "Divisors of " << rand_num << " are: ";
	for (int i = 0; i < 50; i++) {
		if (divisors[i] != 0) {
			divisor_sum += divisors[i];
			cout << divisors[i] << " ";
		}
	}
	cout << "and their sum is: " << divisor_sum << endl;

	// Set determination of APDness
	if (divisor_sum < rand_num) {
		determination = 1;
	} else if (divisor_sum == rand_num) {
		determination = 2;
	} else if (divisor_sum > rand_num) {
		determination = 3;
	} else {
		cout << "Unknown error";
	}
}

void Game::display_results() {
	// Show results
	if (user_guess == determination) {
		cout << "You win!" << endl;
		increment();
	} else {
		cout << "Wrong again, Louie..." << endl;
	}
	display();
}


Game::Game() {
	// Default constructor; generates random number and sets appropriate inital values
	random_number();
	user_guess = '\0';
	score=0;
}

Game::~Game() {
	// Default destructor; pauses at the end of the session
	cout << "Game over...";
	_getch();
}

void Game::guess() {
	// Have user guess whether number is Deficient, Perfect, or Abundant
	cout << "Is " << rand_num << " Deficient, Perfect, or Abundant?" << endl;
	cout << "1. Deficient" << endl;
	cout << "2. Perfect" << endl;
	cout << "3. Abundant" << endl;
	
	// Loop for appropriate input
	do {
		cout << "My guess: ";
		cin >> user_guess;
		cin.clear();
		cin.ignore(1024, '\n');
		} while ((user_guess < 1) || (user_guess > 3));
}


void Game::display() {
	// Displays score, until score = 10
	cout << "Your score is " << score << endl;
	if ( score >= 10 ) {
		cout << "You're too good for me. I quit!" << endl;
		main();
	}
}

void Game::increment() {
	// Increments score
	score++;
}

int Game::get_score() {
	// Returns score value
	return score;
}

int Game::get_rand() {
	// Returns random number generated
	return rand_num;
}