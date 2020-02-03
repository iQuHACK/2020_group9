
_Organizer's note:_ this project participated in iQuHACK 2020.

---

# quantum-roulette
A quantum game based on quantum teleportation and decoherence.


# Goal
The primary goal of this game is to demonstrate how the fidelity of quantum gates can impact quantum circuits, as well as familiarize the players with a few of the basic gates.


# Rules
Players take turns teleporting a quantum state |ψ⟩, which starts in the |0⟩ state, back and forth between each other. Since quantum hardware is not perfect, however, eventually the state will be lost to either gate failure or decoherence. The first player that fails to send the quantum state loses. While the probability of losing should stay the same, as the previous successful transmissions do not affect the future probability of failure, in the game we act as though each successive transmission requires the entire circuit to be run from the beginning. This reflects the difficulty of creating longer, more complex circuits with current technology.

Additionally, players have the option of performing up to 5 single-qubit operations on |ψ⟩ during their turn. This increases the chance of losing; however, this also increases that player's score, for a maximum of 5 points every turn. If a player reaches 20 points and then successfully sends the signal, they win the game. This demonstrates how the transmitted state can be used for calculations by both players and passed back and forth.

Finally, before teleporting the state over, players have the option to measure the current state |ψ⟩, running the circuit many times to collapse |ψ⟩ to either |0⟩ or |1⟩. If it collapses to |1⟩ more often than |0⟩, the player wins, and if it collapses to |0⟩ more often, that player loses. Additionally, the other player will know how many gates the player used, as well as one random gate they applied. This encourages players to use multiple gates to increase information entropy. It also rewards players that understand the effect of each of the different gates.


# How to Play
Follow the prompts. Input gates as a string with the characters "h", "t", "x", "y", or "z".
