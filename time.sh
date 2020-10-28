for iteration in 100000; do
	for batch in 256; do
		for alpha in  1 5 25 125 625; do
			for hint in 0.2 0.4 0.6 0.8; do
				f="./time/time_a${alpha}_h${hint}_b${batch}_${iteration}.txt"
				rmse=$(tail -n 1 $f | cut -d ' ' -f 3)
				echo -n "${rmse},";
			done
			echo ""
		done
	done
done
