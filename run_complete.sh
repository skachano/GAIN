file=$(basename "$1")
echo "Started training for file $file"
python3 main_corpy.py --data_path $1 --output_path /data/workload_estimation/Toyota20201008/imputed_data/test/completed_${file} --batch_size 256 --hint_rate 0.6 --alpha 25 --iterations 10000 &
echo "Finished training for file $file"
