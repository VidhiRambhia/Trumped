pragma solidity ^0.5.12;

/// @title SecurityDeposit
/// @author nidheekamble

contract SecurityDeposit {
    
    mapping (address => uint) public balances; 
    mapping (string => address) public account;
    
    struct DepositsMade {
        address publisher;
        uint amountPayed; 
    }
    DepositsMade[10] public totalDeposits;
    uint public newsArticlesPublished = 0;

    account['trumped'] = 0x7A5237b1975406F7B7ED4Da82b9221328B7eEa8D;

    uint securityDep = 2;
    uint public status = 0; // 0 = notOkay; 1 = okay
    
    uint private _balance = address(this).balance;  
    
    function DepositAmount(address account['trumped'], uint _amount) public returns void {
        account['trumped'].transfer(_amount);
        balances[account['trumped']] += msg.value;
        balances[address(this)] -= msg.value;
    }
    
    function CheckDeposit(uint256 _amount) payable public returns (uint) {
        require(msg.value == _amount);
        totalDeposits.push(DepositsMade(publisher=address(this), amountPayed=msg.value));
        newsArticlesPublished += 1;
        return 1;
    }
    
    function DepositCompletion() public {
        authPublisher = msg.sender;
        if (address(this).balance>=securityDep) {
            DepositAmount(account['trumped'], securityDep);
            status = CheckDeposit(securityDep);
            require(status == 1);
        }
    }
    
}