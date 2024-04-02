use v5.34;
print "Hello, world!\n";
say "Bye, world!";

my @lines = `perldoc -u -f atan2`;
foreach (@lines) {
  s/\w<(.+?)>/\U$1/g;
  print;
}