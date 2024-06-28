// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

/*
    @author: ES_TAKASUGI
*/

import "./DecentPrimalLotteryPool.sol";
import "./DecentPrimalLotteryUser.sol";
import "./SafeMath.sol";
import "./Ownable.sol";
import "./DecentPrimalLottery.sol";
import "./DecentPrimalLotteryRandHelper.sol";
import "./SafeMath.sol";

contract DecentPrimalLotteryHelper is DecentPrimalLottery, DecentPrimalLotteryRandHelper {
    
    // use the safe math library
    using SafeMath32 for uint32;
    using SafeMath for uint256;

    // once contracts been deployed, following things happens
    constructor() {
        createPool();
    }


    // this function check if the msg sender is the winner, the first user who check this function will trigger the find winner function and shall be rewarded with ether worth of 3 lottery tickets
    function amITheWinner() public validUser() returns(bool) {
        require(block.timestamp < poolLedger[currentPoolIndex - 1].poolEndTime, "The pool does not end yet");
        

        if (keccak256(abi.encodePacked(poolLedger[currentPoolIndex.sub(1)].winnerUserName)) != keccak256(abi.encodePacked(""))) {
            findWinner();
            // reward the first caller
            (bool callSuccess, ) = payable(msg.sender).call{value: lotteryTicketPrice.mul(3)}("");
            require(callSuccess, "Call failed");
        }

        if (addressToUserInfo[msg.sender].isWinnerOfCurrentPool == false){
            return false;
        } else {
            return true;
        }

    }


}