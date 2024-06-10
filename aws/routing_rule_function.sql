create function GetEndOfDayEpoch()
returns bigint
begin 
    declare @CurrentDateTime datetime;
    declare @EndOfDay datetime;
    declare #EpochTime bigint;

    -- Get the current time and date
    set @CurrentDateTime = getdate();

    -- Get the end of the day 23:50:00 hrs in epoch time
    set @EndOfDay = dateadd(minute, 1430, cast(cast(@CurrentDateTime as date) as datetime));

    -- Calculate the epoch time for the end of the day
    set @EpochTime = datediff(second, '1970-01-01 00:00:00.000', @EndOfDay);

    return @EpochTime;
end;

unix_timestamp(concat(date_format(ts, '%Y-%m-%d'), '23:50:00')) as ttl_epoch
