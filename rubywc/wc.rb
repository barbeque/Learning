#!/usr/bin/ruby

path = ARGV[0]
if path == nil
	print "Argument must point to a file to read the lines of."
else
	lines = 0
	File.open(path).each { |line| lines = lines + 1 }
	print lines, " lines"
end
