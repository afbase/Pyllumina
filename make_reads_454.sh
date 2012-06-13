#!/bin/tcsh

foreach ac (`awk '{print $2}' $argv[1]`)

        set size = `grep $ac $argv[1] | awk '{print $3}'`
        set chr = `grep $ac $argv[1] | awk '{print $1}'`
        set cov = 10
        set ins = 0
        set length = 500
	set set = ""

	foreach cov ( 2 4 6 8 10)
		if ( $cov < 10 ) then
			set sets = "1"
		else
			set sets = "-A -B -C -D -E -F -G -H"
		endif

	foreach set ( $sets )
	#foreach ins (0 500 2000 8000 20000 40000)
	foreach ins (0)	
		if ( $cov < 10 ) then
			set set = ""
		endif

		if ($ins == 0) then 
			echo "Fragments ($ins)..."
	        	set reads = `dc -e "$size $cov * $length 2 * / p"`
        		set header = $ac-454-R$length-I$ins-C${cov}$set
			set cycles = `dc -e "$length 0.4 x* p" | sed 's/\..*//'` 
			echo $ac \(${size}bp\) x $cov = $reads ${length}bp reads \($cycles cycles\) '->' $header.fasta
			~/bin/metasim/MetaSim cmd -r $reads --454 --454-cycles $cycles ~/references/rice/chr${chr}.fasta >> metasim.log
		        sed 's/>r\(.*\)\.1 |.*/>$chr_fragment_\1/' chr{$chr}-454.fna > x
                        ~/bin/scripts/clean_fasta.pl x > $header.fasta
		else
			echo "Paired ($ins)..."
			set stddev = `dc -e "$ins 5 / p"`
			set reads = `dc -e "$size $cov * $length 50 - 2 * / p"`
	        	set header = $ac-454-R$length-I$ins-C${cov}$set
			set cycles = `dc -e "$length 0.4 x* p" | sed 's/\..*//'` 
			set pair_len = `dc -e "$length 50 - 2 / p 0 k"`
			echo $ac \(${size}bp\) x $cov = $reads ${length}bp reads, $pair_len pairs \($cycles cycles\) '->' $header.fasta
			~/bin/metasim/MetaSim cmd -r $reads --454 --454-cycles $cycles --454-mate-probability 100 --454-paired-read-length $pair_len --454-remove-linker --clones-mean $ins --clones-param2 $stddev ~/references/rice/chr${chr}.fasta >> metasim.log 

			sed 's/>\(r.*1\)\ |SOURCES=.*/>\1/'  chr{$chr}-454.fna > $header.fasta
			~/bin/scripts/clean_fasta.pl $header.fasta > x
			mv x $header.fasta
		endif
	
		rm chr{$chr}-454.fna
	end
	end
end

	#foreach library (A B C D E F G H I J)
		#echo $library
		#~/bin/metasim/MetaSim cmd -r $reads -m -g ~/bin/metasim/examples/ErrorModelSolexaPerfect100bp.mconf -2 ~/bin/metasim/examples/ErrorModelSolexaPerfect100bp.mconf --empirical-pe-probability 100 --clones-mean 500 --clones-param2 50 ~/references/rice/chr${chr}.fasta
		#cp chr12-Empirical.fna rice-Illumina-500bp-5x.fna
		#rm x
		#mv rice-Illumina-500bp-5x.fna rice-chr12-Illumina-500bp-2x.$library.fna
	#end

	#2.5kb
	
	#8kb
	#~/bin/metasim/MetaSim cmd -r $reads --454 --454-cycles 200 --454-mate-probability 100 --454-paired-read-length 200 --454-remove-linker --clones-mean 8000 --clones-param2 800 ~/references/rice/chr${chr}.fasta
	#cat chr*-454.fna > rice-454-8kb-5x.fna

	#20kb
        #foreach library (A B C D E F G H I J)
                #echo $library
		#~/bin/metasim/MetaSim cmd -r $reads -m -g ~/bin/metasim/examples/ErrorModelSolexaPerfect100bp.mconf -2 ~/bin/metasim/examples/ErrorModelSolexaPerfect100bp.mconf --empirical-pe-probability 100 --clones-mean 20000 --clones-param2 2000 ~/references/rice/chr${chr}.fasta	
                #cp chr12-Empirical.fna rice-Illumina-20kb-2x.fna
                #sed 's/>r\(.*\)\.1 |.*/>2x20kb'"${library}"'_\1_1 library=2x20kb'"${library}"' dir=F template=2x20kb'"${library}"'_\1/' rice-Illumina-20kb-2x.fna > x
                #sed 's/>r\(.*\)\.2 |.*/>2x20kb'"${library}"'_\1_2 library=2x20kb'"${library}"' dir=R template=2x20kb'"${library}"'_\1/' x > rice-chr12-Illumina-20kb-2x.$library.fna
                #rm x
        #end

	#~/bin/metasim/MetaSim cmd -r $reads --454 --454-cycles 200 --454-mate-probability 100 --454-paired-read-length 200 --454-remove-linker --clones-mean 20000 --clones-param2 1000 ~/references/rice/chr${chr}.fasta
	#cp chr12-Empirical.fna rice-Illumina-20kb-5x.fna
	#sed 's/>r\(.*\)\.1 |.*/>5x20kb1_\1_1 library=5x20kb1 dir=F template=5x20kb1_\1/' rice-Illumina-20kb-5x.fna > x
	#sed 's/>r\(.*\)\.2 |.*/>5x20kb1_\1_2 library=5x20kb1 dir=R template=5x20kb1_\1/' x > rice-Illumina-20kb-5x.fna 	
	#rm x

	#40kb
	#~/bin/metasim/MetaSim cmd -r $reads --454 --454-cycles 200 --454-mate-probability 100 --454-paired-read-length 200 --454-remove-linker --clones-mean 40000 --clones-param2 2500 ~/references/rice/chr${chr}.fasta


#rm chr*

#sed 's/>\(.*\)_1/>\1_1 template=\1 dir=F library=5x2/' rice-454-5x-Fragments.2.fna > x
#mv x rice-454-5x-Fragments.2.fna 

#sed 's/>r\(.*\) |.*/>5x2_\1/' rice-454-8kb-5x.1.fna | sed 's/\./_/' > x
#mv x rice-454-8kb-5x.1.fna
#sed 's/>\(.*\)_1/>\1_1 template=\1 dir=F library=5x2/' rice-454-5x-Fragments.2.fna > x
#mv x rice-454-8kb-5x.1.fna

#sed 's/>r\(.*\) |.*/>5x2_\1/' rice-454-20kb-5x.1.fna | sed 's/\./_/' > x
#mv x rice-454-20kb-5x.1.fna
