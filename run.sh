for alpha in 1 5 25 125 625; do
	for hint in 0.2 0.4 0.6 0.8; do
		for batch in 256; do
			for iteration in 100000; do
				echo "Started training for alpha=$alpha, hint=$hint, batch=$batch, iteration=$iteration"
				(python3 main_letter_spam.py --data_name ../data.csv --miss_rate 0.1 --batch_size $batch --hint_rate $hint --alpha $alpha --iterations $iteration) |& tee ./time/time_a${alpha}_h${hint}_b${batch}_${iteration}.txt &
				echo "Finished training for alpha=$alpha, hint=$hint, batch=$batch, iteration=$iteration"
			done
		done
	done
done
