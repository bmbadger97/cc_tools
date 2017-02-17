import cc_dat_utils
import cc_json_utils
import sys

#default input bbadger_testdata...json
input_json_file = "data/bbadger_cc1.json"
output_dat_file = "data/bbadger_cc1.dat"
#default output bbadger_....dat

if len(sys.argv) == 3:
    input_json_file = argv[1]
    output_dat_file = argv[2]
else:
    print("Invalid arguments. Using default values: " + input_json_file + " " + output_dat_file)
json_data = cc_json_utils.make_cc_dat_from_json(input_json_file)
cc_dat_utils.write_cc_data_to_dat(json_data, output_dat_file)
dat_data = cc_dat_utils.make_cc_data_from_dat(output_dat_file)
print(dat_data)