

/* -------- Create Customer Table --------*/
CREATE TABLE IF NOT EXISTS `customer` (

  `Phone` varchar(45) NOT NULL,
  `Namez` varchar(100) NOT NULL,
  
  PRIMARY KEY (`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* -------- Create policy details Table --------*/
CREATE TABLE IF NOT EXISTS `policydetails` (

  `policyNumber` varchar(100) NOT NULL,
  `policyName` varchar(100) NOT NULL,
  `policyStatus` varchar(100) NOT NULL,
  `surrenderValue` varchar(100) DEFAULT NULL,
  `fundValue` varchar(100) DEFAULT NULL,
  `neftStatus` varchar(100) NOT NULL,
  `renewalStatus` varchar(100) DEFAULT NULL,
  `maturityBenefit` varchar(100) DEFAULT NULL,
  `revivalAmount` varchar(100) DEFAULT NULL,
  `premiumDiff` varchar(100) DEFAULT NULL,
  `premiumStatus` varchar(100) DEFAULT NULL,
  `prevPremium` varchar(100) DEFAULT NULL,
  
  PRIMARY KEY (`policyNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* -------- Insert policy Sample --------*/
INSERT INTO `policydetails` 
VALUES ('12345678','Raksha','Active','20000','10000','Enabled','Lapsed','100000','10000','2000','Due/Not Recieved','4000')
,('12345679','Cancer Shield','Not Active','50000','30000','Disabled','Renewed','50000','10000','4000','Received','2000');

