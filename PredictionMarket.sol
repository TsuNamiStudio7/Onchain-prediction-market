// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PredictionMarket {
    struct Bet {
        uint256 amount;
        bool predictedOutcome; // true or false
    }

    mapping(address => Bet) public bets;
    uint256 public totalBets;
    uint256 public totalAmount;
    uint256 public winningOutcome; // 0 = not decided, 1 = true, 2 = false
    address public admin;

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function placeBet(bool _outcome) public payable {
        require(msg.value > 0, "You need to place a bet");
        require(winningOutcome == 0, "The event is already concluded");
        
        Bet storage bet = bets[msg.sender];
        bet.amount += msg.value;
        bet.predictedOutcome = _outcome;

        totalBets += 1;
        totalAmount += msg.value;
    }

    function resolveEvent(bool _outcome) public onlyAdmin {
        require(winningOutcome == 0, "Event is already resolved");
        
        winningOutcome = _outcome ? 1 : 2;
    }

    function distributeRewards() public onlyAdmin {
        require(winningOutcome != 0, "Event is not resolved");
        
        for (address bettor = address(0); bettor <= address(type(uint160).max); bettor++) {
            if (bets[bettor].predictedOutcome == (winningOutcome == 1)) {
                payable(bettor).transfer(bets[bettor].amount * 2);
            }
        }
    }
}
