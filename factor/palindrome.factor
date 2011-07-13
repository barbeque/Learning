! Copyright (C) 2011 mike stedman.
! See http://factorcode.org/license.txt for BSD license.
USING: kernel sequences ascii ;
IN: palindrome

! Strips out everything that's not a letter and lowercases the bitch
: normalize ( str -- newstr ) [ Letter? ] filter >lower ;

! Tells us if a given random string is a palindrome.
: palindrome? ( string -- ? ) normalize dup reverse = ;