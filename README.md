# Onchain Prediction Market

A decentralized prediction market where users can place bets on various events and receive rewards based on the outcome. Admins can resolve the event and distribute rewards automatically.

## Features

- Users can place bets with ETH on specific outcomes.
- Admin can resolve events by choosing the winning outcome.
- Rewards are distributed to users who predicted the correct outcome.

---

## How to Use

### 1. Deploy Contract
Run the `deploy_contract.py` script to deploy the `PredictionMarket.sol` contract to the blockchain.

### 2. Place a Bet
Use `place_bet.py` to place a bet on an outcome. Bet with ETH on a true/false prediction.

### 3. Resolve the Event
After the event occurs, an admin can resolve it using the `resolve_event.py` script.

### 4. Distribute Rewards
Once the event is resolved, the admin can run `distribute_rewards.py` to send ETH to the users who predicted correctly.

---

## Setup

1. Compile `PredictionMarket.sol` using Remix or Hardhat.
2. Run `deploy_contract.py` to deploy the contract.
3. Use `place_bet.py` to place your bet on a true or false outcome.
4. Resolve the event using `resolve_event.py` after the event is concluded.
5. Distribute rewards to correct predictors using `distribute_rewards.py`.

---

## Roles

- **Admin**: Can resolve events and distribute rewards.
- **User**: Can place bets on event outcomes.

---

## ⚖️ Notes

- Only the admin can resolve the event and distribute rewards.
- Rewards are sent to correct bettors automatically.
