#!/bin/tcsh

foreach ac (`awk '{print $2}' $argv[1]`)
	echo "$ac"
	set size = `grep $ac $argv[1] | awk '{print $3}'`
	set chr = `grep $ac $argv[1] | awk '{print $1}'`
	set cov = 10
	set length = 75
	set ins = 8000
	set stddev = 800

	#foreach set (A B C D E F G H)
	foreach cov ( 2 4 6 8 )
	foreach length ( 50 75 100 36 )
	foreach ins ( 500 2000 8000 20000 40000 )

		set stddev = `dc -e "$ins 5 / p"`
	
        	set reads = `dc -e "$size $cov * $length 2 * / p"`
		set header = $ac-Illumina-R${length}-I$ins-C$cov

		if (-e $header.fasta) then
			echo "$header.fasta exists"		
		else
			echo $ac \(${size}bp\) x $cov = $reads ${length}bp reads '->' $header.fasta
			echo /catalina/sarah/bin/metasim/MetaSim cmd -r $reads -m \
				-g /catalina/sarah/bin/metasim/examples/errormodel-${length}bp.mconf \
				-2 /catalina/sarah/bin/metasim/examples/errormodel-${length}bp.mconf \
				--empirical-pe-probability 100 --clones-mean $ins --clones-param2 $stddev \
				/catalina/sarah/references/rice/chr${chr}.fasta #>> metasim.log
			#/catalina/sarah/bin/scripts/clean_fasta.pl chr*-Empirical.fna | sed 's/r/'"$ac"'./' > $header.fasta
			rm chr*-Empirical.fna
		endif
	end
	end
	end
end

