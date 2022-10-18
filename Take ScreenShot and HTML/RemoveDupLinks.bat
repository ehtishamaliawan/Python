PS H:\> $hash = @{}      # define a new empty hash table
PS H:\> gc c:\rawlist.txt | 
>> %{if($hash.$_ -eq $null) { $_ }; $hash.$_ = 1} > 
>> c:\newlist.txt