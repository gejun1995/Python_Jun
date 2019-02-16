#!/usr/bin/perl
use strict;
use warnings;

my($var, $tf, $gene, @arr, %stat, %hash);
open(FH, "all.txt") || die($!);
while(<FH>){
	chomp;
	@arr = split("\t");
	$stat{$arr[0]} = "$arr[1]\t$arr[2]\t$arr[3]\t$arr[4]\t$arr[5]\t$arr[6]\t$arr[7]\t$arr[8]\t$arr[9]\t$arr[10]\t$arr[11]\t$arr[12]\t$arr[13]\t$arr[14]\t$arr[15]\t$arr[16]\t$arr[17]"; # $stat{$arr[1]} = "$arr[0]\t$arr[2]";
}
close(FH) || die($!);

open(ZY, "chose.txt") || die($!);
open(OUT, ">RESULT.txt") || die($!);
while(<ZY>){
	chomp;
	$gene = $_;
	$var = "${gene}";
	if($stat{$var}){
		print OUT "$var\t$stat{$var}\n";
	}else{
		print OUT "";
	}
}
close(OUT) || die($!);
close(ZY) || die($!);
