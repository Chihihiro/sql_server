import datetime as dt
from pandas.tseries.offsets import CustomBusinessDay


class Const:
    holidays_chn = [
        dt.date(2004, 1, 1),
        dt.date(2004, 1, 22),
        dt.date(2004, 1, 23),
        dt.date(2004, 1, 24),
        dt.date(2004, 1, 25),
        dt.date(2004, 1, 26),
        dt.date(2004, 1, 27),
        dt.date(2004, 1, 28),
        dt.date(2004, 5, 1),
        dt.date(2004, 5, 2),
        dt.date(2004, 5, 3),
        dt.date(2004, 5, 4),
        dt.date(2004, 5, 5),
        dt.date(2004, 5, 6),
        dt.date(2004, 5, 7),
        dt.date(2004, 10, 1),
        dt.date(2004, 10, 2),
        dt.date(2004, 10, 3),
        dt.date(2004, 10, 4),
        dt.date(2004, 10, 5),
        dt.date(2004, 10, 6),
        dt.date(2004, 10, 7),
        dt.date(2005, 1, 1),
        dt.date(2005, 1, 2),
        dt.date(2005, 1, 3),
        dt.date(2005, 2, 9),
        dt.date(2005, 2, 10),
        dt.date(2005, 2, 11),
        dt.date(2005, 2, 12),
        dt.date(2005, 2, 13),
        dt.date(2005, 2, 14),
        dt.date(2005, 2, 15),
        dt.date(2005, 5, 1),
        dt.date(2005, 5, 2),
        dt.date(2005, 5, 3),
        dt.date(2005, 5, 4),
        dt.date(2005, 5, 5),
        dt.date(2005, 5, 6),
        dt.date(2005, 5, 7),
        dt.date(2005, 10, 1),
        dt.date(2005, 10, 2),
        dt.date(2005, 10, 3),
        dt.date(2005, 10, 4),
        dt.date(2005, 10, 5),
        dt.date(2005, 10, 6),
        dt.date(2005, 10, 7),
        dt.date(2006, 1, 1),
        dt.date(2006, 1, 2),
        dt.date(2006, 1, 3),
        dt.date(2006, 1, 29),
        dt.date(2006, 1, 30),
        dt.date(2006, 1, 31),
        dt.date(2006, 2, 1),
        dt.date(2006, 2, 2),
        dt.date(2006, 2, 3),
        dt.date(2006, 2, 4),
        dt.date(2006, 5, 1),
        dt.date(2006, 5, 2),
        dt.date(2006, 5, 3),
        dt.date(2006, 5, 4),
        dt.date(2006, 5, 5),
        dt.date(2006, 5, 6),
        dt.date(2006, 5, 7),
        dt.date(2006, 10, 1),
        dt.date(2006, 10, 2),
        dt.date(2006, 10, 3),
        dt.date(2006, 10, 4),
        dt.date(2006, 10, 5),
        dt.date(2006, 10, 6),
        dt.date(2006, 10, 7),
        dt.date(2007, 1, 1),
        dt.date(2007, 1, 2),
        dt.date(2007, 1, 3),
        dt.date(2007, 2, 18),
        dt.date(2007, 2, 19),
        dt.date(2007, 2, 20),
        dt.date(2007, 2, 21),
        dt.date(2007, 2, 22),
        dt.date(2007, 2, 23),
        dt.date(2007, 2, 24),
        dt.date(2007, 5, 1),
        dt.date(2007, 5, 2),
        dt.date(2007, 5, 3),
        dt.date(2007, 5, 4),
        dt.date(2007, 5, 5),
        dt.date(2007, 5, 6),
        dt.date(2007, 5, 7),
        dt.date(2007, 10, 1),
        dt.date(2007, 10, 2),
        dt.date(2007, 10, 3),
        dt.date(2007, 10, 4),
        dt.date(2007, 10, 5),
        dt.date(2007, 10, 6),
        dt.date(2007, 10, 7),
        dt.date(2007, 12, 30),
        dt.date(2007, 12, 31),
        dt.date(2008, 1, 1),
        dt.date(2008, 2, 6),
        dt.date(2008, 2, 7),
        dt.date(2008, 2, 8),
        dt.date(2008, 2, 9),
        dt.date(2008, 2, 10),
        dt.date(2008, 2, 11),
        dt.date(2008, 2, 12),
        dt.date(2008, 4, 4),
        dt.date(2008, 4, 5),
        dt.date(2008, 4, 6),
        dt.date(2008, 5, 1),
        dt.date(2008, 5, 2),
        dt.date(2008, 5, 3),
        dt.date(2008, 6, 7),
        dt.date(2008, 6, 8),
        dt.date(2008, 6, 9),
        dt.date(2008, 9, 13),
        dt.date(2008, 9, 14),
        dt.date(2008, 9, 15),
        dt.date(2008, 9, 29),
        dt.date(2008, 9, 30),
        dt.date(2008, 10, 1),
        dt.date(2008, 10, 2),
        dt.date(2008, 10, 3),
        dt.date(2008, 10, 4),
        dt.date(2008, 10, 5),
        dt.date(2009, 1, 1),
        dt.date(2009, 1, 2),
        dt.date(2009, 1, 3),
        dt.date(2009, 1, 25),
        dt.date(2009, 1, 26),
        dt.date(2009, 1, 27),
        dt.date(2009, 1, 28),
        dt.date(2009, 1, 29),
        dt.date(2009, 1, 30),
        dt.date(2009, 1, 31),
        dt.date(2009, 4, 4),
        dt.date(2009, 4, 5),
        dt.date(2009, 4, 6),
        dt.date(2009, 5, 1),
        dt.date(2009, 5, 2),
        dt.date(2009, 5, 3),
        dt.date(2009, 5, 28),
        dt.date(2009, 5, 29),
        dt.date(2009, 5, 30),
        dt.date(2009, 10, 1),
        dt.date(2009, 10, 2),
        dt.date(2009, 10, 3),
        dt.date(2009, 10, 4),
        dt.date(2009, 10, 5),
        dt.date(2009, 10, 6),
        dt.date(2009, 10, 7),
        dt.date(2009, 10, 8),
        dt.date(2010, 1, 1),
        dt.date(2010, 1, 2),
        dt.date(2010, 1, 3),
        dt.date(2010, 2, 13),
        dt.date(2010, 2, 14),
        dt.date(2010, 2, 15),
        dt.date(2010, 2, 16),
        dt.date(2010, 2, 17),
        dt.date(2010, 2, 18),
        dt.date(2010, 2, 19),
        dt.date(2010, 4, 3),
        dt.date(2010, 4, 4),
        dt.date(2010, 4, 5),
        dt.date(2010, 5, 1),
        dt.date(2010, 5, 2),
        dt.date(2010, 5, 3),
        dt.date(2010, 6, 14),
        dt.date(2010, 6, 15),
        dt.date(2010, 6, 16),
        dt.date(2010, 9, 22),
        dt.date(2010, 9, 23),
        dt.date(2010, 9, 24),
        dt.date(2010, 10, 1),
        dt.date(2010, 10, 2),
        dt.date(2010, 10, 3),
        dt.date(2010, 10, 4),
        dt.date(2010, 10, 5),
        dt.date(2010, 10, 6),
        dt.date(2010, 10, 7),
        dt.date(2011, 1, 1),
        dt.date(2011, 1, 2),
        dt.date(2011, 1, 3),
        dt.date(2011, 2, 2),
        dt.date(2011, 2, 3),
        dt.date(2011, 2, 4),
        dt.date(2011, 2, 5),
        dt.date(2011, 2, 6),
        dt.date(2011, 2, 7),
        dt.date(2011, 2, 8),
        dt.date(2011, 4, 3),
        dt.date(2011, 4, 4),
        dt.date(2011, 4, 5),
        dt.date(2011, 4, 30),
        dt.date(2011, 5, 1),
        dt.date(2011, 5, 2),
        dt.date(2011, 6, 4),
        dt.date(2011, 6, 6),
        dt.date(2011, 9, 10),
        dt.date(2011, 9, 11),
        dt.date(2011, 9, 12),
        dt.date(2011, 10, 1),
        dt.date(2011, 10, 2),
        dt.date(2011, 10, 3),
        dt.date(2011, 10, 4),
        dt.date(2011, 10, 5),
        dt.date(2011, 10, 6),
        dt.date(2011, 10, 7),
        dt.date(2012, 1, 1),
        dt.date(2012, 1, 2),
        dt.date(2012, 1, 3),
        dt.date(2012, 1, 22),
        dt.date(2012, 1, 23),
        dt.date(2012, 1, 24),
        dt.date(2012, 1, 25),
        dt.date(2012, 1, 26),
        dt.date(2012, 1, 27),
        dt.date(2012, 1, 28),
        dt.date(2012, 4, 2),
        dt.date(2012, 4, 3),
        dt.date(2012, 4, 4),
        dt.date(2012, 4, 29),
        dt.date(2012, 4, 30),
        dt.date(2012, 5, 1),
        dt.date(2012, 6, 22),
        dt.date(2012, 6, 24),
        dt.date(2012, 9, 30),
        dt.date(2012, 10, 1),
        dt.date(2012, 10, 2),
        dt.date(2012, 10, 3),
        dt.date(2012, 10, 4),
        dt.date(2012, 10, 5),
        dt.date(2012, 10, 6),
        dt.date(2012, 10, 7),
        dt.date(2013, 1, 1),
        dt.date(2013, 1, 2),
        dt.date(2013, 1, 3),
        dt.date(2013, 2, 9),
        dt.date(2013, 2, 10),
        dt.date(2013, 2, 11),
        dt.date(2013, 2, 12),
        dt.date(2013, 2, 13),
        dt.date(2013, 2, 14),
        dt.date(2013, 2, 15),
        dt.date(2013, 4, 4),
        dt.date(2013, 4, 5),
        dt.date(2013, 4, 6),
        dt.date(2013, 4, 29),
        dt.date(2013, 4, 30),
        dt.date(2013, 5, 1),
        dt.date(2013, 6, 10),
        dt.date(2013, 6, 11),
        dt.date(2013, 6, 12),
        dt.date(2013, 9, 19),
        dt.date(2013, 9, 20),
        dt.date(2013, 9, 21),
        dt.date(2013, 10, 1),
        dt.date(2013, 10, 2),
        dt.date(2013, 10, 3),
        dt.date(2013, 10, 4),
        dt.date(2013, 10, 5),
        dt.date(2013, 10, 6),
        dt.date(2013, 10, 7),
        dt.date(2014, 1, 1),
        dt.date(2014, 1, 31),
        dt.date(2014, 2, 1),
        dt.date(2014, 2, 2),
        dt.date(2014, 2, 3),
        dt.date(2014, 2, 4),
        dt.date(2014, 2, 5),
        dt.date(2014, 2, 6),
        dt.date(2014, 4, 5),
        dt.date(2014, 4, 6),
        dt.date(2014, 4, 7),
        dt.date(2014, 5, 1),
        dt.date(2014, 5, 2),
        dt.date(2014, 5, 3),
        dt.date(2014, 6, 2),
        dt.date(2014, 9, 8),
        dt.date(2014, 10, 1),
        dt.date(2014, 10, 2),
        dt.date(2014, 10, 3),
        dt.date(2014, 10, 4),
        dt.date(2014, 10, 5),
        dt.date(2014, 10, 6),
        dt.date(2014, 10, 7),
        dt.date(2015, 1, 1),
        dt.date(2015, 1, 2),
        dt.date(2015, 1, 3),
        dt.date(2015, 2, 18),
        dt.date(2015, 2, 19),
        dt.date(2015, 2, 20),
        dt.date(2015, 2, 21),
        dt.date(2015, 2, 22),
        dt.date(2015, 2, 23),
        dt.date(2015, 2, 24),
        dt.date(2015, 4, 5),
        dt.date(2015, 4, 6),
        dt.date(2015, 5, 1),
        dt.date(2015, 6, 20),
        dt.date(2015, 6, 22),
        dt.date(2015, 9, 3),
        dt.date(2015, 9, 4),
        dt.date(2015, 9, 27),
        dt.date(2015, 10, 1),
        dt.date(2015, 10, 2),
        dt.date(2015, 10, 3),
        dt.date(2015, 10, 4),
        dt.date(2015, 10, 5),
        dt.date(2015, 10, 6),
        dt.date(2015, 10, 7),
        dt.date(2016, 1, 1),
        dt.date(2016, 2, 7),
        dt.date(2016, 2, 8),
        dt.date(2016, 2, 9),
        dt.date(2016, 2, 10),
        dt.date(2016, 2, 11),
        dt.date(2016, 2, 12),
        dt.date(2016, 2, 13),
        dt.date(2016, 4, 4),
        dt.date(2016, 5, 1),
        dt.date(2016, 5, 2),
        dt.date(2016, 6, 9),
        dt.date(2016, 6, 10),
        dt.date(2016, 6, 11),
        dt.date(2016, 9, 15),
        dt.date(2016, 9, 16),
        dt.date(2016, 9, 17),
        dt.date(2016, 10, 1),
        dt.date(2016, 10, 2),
        dt.date(2016, 10, 3),
        dt.date(2016, 10, 4),
        dt.date(2016, 10, 5),
        dt.date(2016, 10, 6),
        dt.date(2016, 10, 7),
        dt.date(2017, 1, 1),
        dt.date(2017, 1, 2),
        dt.date(2017, 1, 27),
        dt.date(2017, 1, 28),
        dt.date(2017, 1, 29),
        dt.date(2017, 1, 30),
        dt.date(2017, 1, 31),
        dt.date(2017, 2, 1),
        dt.date(2017, 2, 2),
        dt.date(2017, 4, 2),
        dt.date(2017, 4, 3),
        dt.date(2017, 4, 4),
        dt.date(2017, 5, 1),
        dt.date(2017, 5, 28),
        dt.date(2017, 5, 29),
        dt.date(2017, 5, 30),
        dt.date(2017, 10, 1),
        dt.date(2017, 10, 2),
        dt.date(2017, 10, 3),
        dt.date(2017, 10, 4),
        dt.date(2017, 10, 5),
        dt.date(2017, 10, 6),
        dt.date(2017, 10, 7),
        dt.date(2017, 10, 8),
        dt.date(2018, 1, 1),
        dt.date(2018, 2, 15),
        dt.date(2018, 2, 16),
        dt.date(2018, 2, 17),
        dt.date(2018, 2, 18),
        dt.date(2018, 2, 19),
        dt.date(2018, 2, 20),
        dt.date(2018, 2, 21),
        dt.date(2018, 4, 5),
        dt.date(2018, 4, 6),
        dt.date(2018, 4, 7),
        dt.date(2018, 4, 29),
        dt.date(2018, 4, 30),
        dt.date(2018, 5, 1),
        dt.date(2018, 6, 18),
        dt.date(2018, 9, 24),
        dt.date(2018, 10, 1),
        dt.date(2018, 10, 2),
        dt.date(2018, 10, 3),
        dt.date(2018, 10, 4),
        dt.date(2018, 10, 5),
        dt.date(2018, 10, 6),
        dt.date(2018, 10, 7)
    ]  # 2004 ~ 2018
    weekmask_chn = "Mon Tue Wed Thu Fri"


# should set normalize to True, so each time element will
# start from midnight, otherwise it will start from 8:00 a.m.
bday_chn = CustomBusinessDay(holidays=Const.holidays_chn, weekmask=Const.weekmask_chn, normalize=True)