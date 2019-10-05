pragma solidity ^0.5.11;
import './SecurityDeposit.sol';

/// @title Refund
/// @author nidheekamble

/*
details imported:
* mappings(accounts, balances), 
* struct: DepositsMade and array,
*/

contract Refund {
    
    // Refund only if name/adddress not in blacklist
    // add require here after o/p of ML algorithm is obtained
    
    account['Harishchandra'] = 0x2f860BF52aF0B67B3EC511027A95cA663c0C841B;

    uint refund = totalDeposits[newsArticlesPublished].amountPayed;
    // 0 = notOkay; 1 = okay. Public variable imported
    
    function RefundAmount(address account['Harishchandra'], uint _amount) public returns void {
        account['Harishchandra'].transfer(_amount);
        balances[account['Harishchandra']] += msg.value;
        balances[address(this)] -= msg.value;
    }
    
    function CheckDeposit(uint256 _amount) payable public returns (uint) {
        require(msg.value == _amount);
        return 1;
    }
    
    function DepositCompletion() public {
        authPublisher = msg.sender;
        if (address(this).balance>=refund) {
            RefundAmount(account['Harishchandra'], refund);
            status = CheckDeposit(refund);
            require(status == 1);
        }
    }
    
}
