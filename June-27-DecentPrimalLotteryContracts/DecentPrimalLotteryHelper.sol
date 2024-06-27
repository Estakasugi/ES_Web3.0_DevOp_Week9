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

contract DecentPrimalLotteryHelper is DecentPrimalLottery {
    
    // once contracts been deployed, following things happens
    constructor() {
        createPool();
    }
}