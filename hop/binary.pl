sub binary {
	my ($n) = @_;
	
	# if n is 1, binary expansion is 1. if 0, 0.
	return $n if $n == 0 || $n == 1;
	
	# figure out the closest multiple of 2; if it's odd the last bit is 1
	my $k = int($n / 2);
	my $lastBit = $n % 2;
	
	# keep recursing on the rest of it until we get a full expansion
	my $expansion = binary($k);
	
	# concatenate the string
	return $expansion . $lastBit;
}

print binary(37) . "\n";