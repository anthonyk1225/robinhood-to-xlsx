PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS splits (
      'id' INTEGER PRIMARY KEY,
      'symbol' TEXT NOT NULL,
      'date' TEXT NOT NULL,
      'from_factor' INTEGER NOT NULL,
      'to_factor' INTEGER NOT NULL
    );
INSERT INTO "splits" VALUES(1,'AAPL','2020-08-31',1,4);
INSERT INTO "splits" VALUES(2,'AAPL','2014-06-09',1,7);
INSERT INTO "splits" VALUES(3,'TSLA','2020-08-31',1,5);
INSERT INTO "splits" VALUES(4,'GE','2019-02-26',100,104);
INSERT INTO "splits" VALUES(5,'AAL','2013-12-09',1,0);
INSERT INTO "splits" VALUES(6,'ACB','2020-05-11',12,1);
INSERT INTO "splits" VALUES(7,'NFLX','2015-07-15',1,7);
INSERT INTO "splits" VALUES(8,'SBUX','2015-04-09',1,2);
INSERT INTO "splits" VALUES(9,'INO','2014-06-06',4,1);
INSERT INTO "splits" VALUES(10,'VOO','2013-10-24',2,1);
INSERT INTO "splits" VALUES(11,'WKHS','2015-12-11',10,1);
INSERT INTO "splits" VALUES(12,'GUSH','2020-03-24',40,1);
INSERT INTO "splits" VALUES(13,'GUSH','2019-11-22',10,1);
INSERT INTO "splits" VALUES(14,'GUSH','2017-05-01',1,2);
INSERT INTO "splits" VALUES(15,'GUSH','2017-04-28',1,1);
INSERT INTO "splits" VALUES(16,'GUSH','2016-03-24',10,1);
INSERT INTO "splits" VALUES(17,'USO','2020-04-29',8,1);
INSERT INTO "splits" VALUES(18,'UCO','2020-04-21',25,1);
INSERT INTO "splits" VALUES(19,'UCO','2017-01-12',2,1);
INSERT INTO "splits" VALUES(20,'UCO','2015-05-20',5,1);
INSERT INTO "splits" VALUES(21,'GOOGL','2014-04-03',1000,1998);
INSERT INTO "splits" VALUES(22,'PENN','2013-11-04',1000,4423);
INSERT INTO "splits" VALUES(23,'NRZ','2014-10-20',2,1);
INSERT INTO "splits" VALUES(24,'NKE','2015-12-24',1,2);
INSERT INTO "splits" VALUES(25,'V','2015-03-19',1,4);
INSERT INTO "splits" VALUES(26,'IBIO','2018-06-11',10,1);
INSERT INTO "splits" VALUES(27,'SRNE','2013-08-01',25,1);
INSERT INTO "splits" VALUES(28,'FCEL','2019-05-09',12,1);
INSERT INTO "splits" VALUES(29,'FCEL','2015-12-04',12,1);
INSERT INTO "splits" VALUES(30,'ET','2015-07-27',1,2);
INSERT INTO "splits" VALUES(31,'ET','2014-01-27',1,2);
INSERT INTO "splits" VALUES(32,'NVAX','2019-05-10',20,1);
INSERT INTO "splits" VALUES(33,'AZN','2015-07-27',1,2);
INSERT INTO "splits" VALUES(34,'AAPL','2020-08-31',1,4);
INSERT INTO "splits" VALUES(35,'AAPL','2014-06-09',1,7);
INSERT INTO "splits" VALUES(36,'FSK','2020-06-16',4,1);
INSERT INTO "splits" VALUES(37,'APRN','2019-06-17',15,1);
INSERT INTO "splits" VALUES(38,'AHT','2020-07-16',10,1);
INSERT INTO "splits" VALUES(39,'AHT','2019-10-28',1000,1012);
INSERT INTO "splits" VALUES(40,'AHT','2014-11-13',1000,1059);
INSERT INTO "splits" VALUES(41,'AHT','2013-11-20',100,149);
INSERT INTO "splits" VALUES(42,'HMNY','2018-07-25',250,1);
INSERT INTO "splits" VALUES(43,'SQQQ','2020-08-18',5,1);
INSERT INTO "splits" VALUES(44,'SQQQ','2019-05-24',4,1);
INSERT INTO "splits" VALUES(45,'SQQQ','2017-01-12',4,1);
INSERT INTO "splits" VALUES(46,'SQQQ','2014-01-24',4,1);
COMMIT;