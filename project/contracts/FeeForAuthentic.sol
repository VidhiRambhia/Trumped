pragma solidity ^0.5.12;

/// @title FeeForAuthentic
/// @author nidheekamble

contract FeeForAuthentic {
    
    mapping (address => uint) private balances; // address: etherLeft
    mapping (string => address) private account; // name: address
    address public authPublisher;
    account['Harishchandra'] = 0x2f860BF52aF0B67B3EC511027A95cA663c0C841B;

    uint amount = 0.5;
    uint status = 0;
    
    uint private _balance = address(this).balance;  
    
    function PayFee(address account['Harishchandra'], uint _amount) public returns void {
        account['Harishchandra'].transfer(_amount);
        balances[account['Harishchandra']] += msg.value;
        balances[address(this)] -= msg.value;
    }
    
    function VerifyPayment(uint256 _amount) payable public returns (uint) {
        require(msg.value == _amount);
        return 1;
    }
    
    function PaymentCompletion() public {
        authPublisher = msg.sender;
        if (address(this).balance>=amount) {
            PayFee(account['Harishchandra'], amount);
            status = VerifyPayment(amount);
            require(status == 1);
        }
    }
    
}