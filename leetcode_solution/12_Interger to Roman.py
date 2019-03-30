class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        numOfM = num // 1000;
        num = num % 1000;

        numOfCM = num // 900;
        num = num % 900;

        numOfD = num // 500;
        num = num % 500;

        numOfCD = num // 400;
        num = num % 400;

        numOfC = num // 100;
        num = num % 100;

        numOfXC = num // 90;
        num = num % 90;

        numOfL = num // 50;
        num = num % 50;

        numOfXL = num // 40;
        num = num % 40;

        numOfX = num // 10;
        num = num % 10;

        numOfIX = num // 9;
        num = num % 9;

        numOfV = num // 5;
        num = num % 5;

        numOfIV = num // 4;
        num = num % 4;

        numOfI = num;


        RomanString = 'M' * numOfM + 'CM' * numOfCM + 'D' * numOfD + 'CD' * numOfCD + 'C' * numOfC + 
                        'XC' * numOfXC + 'L' * numOfL + 'XL' * numOfXL + 'X' * numOfX + 'IX' * numOfIX + 'V' * numOfV + 
                        'IV' * numOfIV + 'I' * numOfI;

        return RomanString;
